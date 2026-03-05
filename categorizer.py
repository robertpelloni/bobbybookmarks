import logging
from collections import Counter
from typing import Optional

import numpy as np

logger = logging.getLogger(__name__)


def cluster_bookmarks(bookmarks: list, n_clusters: Optional[int] = None) -> list[dict]:
    """
    Cluster bookmarks by their tags using TF-IDF + K-Means.

    Parameters
    ----------
    bookmarks : list of Bookmark model instances
    n_clusters : int or None – if None, auto-determine using silhouette score

    Returns
    -------
    list of dicts: {id, name, bookmark_ids, top_tags}
    """
    # Filter bookmarks that have tags and are not duplicates
    tagged = [bm for bm in bookmarks if bm.tags and not bm.is_duplicate]

    if len(tagged) < 2:
        logger.info("Not enough tagged bookmarks to cluster (%d)", len(tagged))
        return []

    # Build tag documents (one string per bookmark)
    docs = [" ".join(bm.tags) for bm in tagged]

    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.cluster import KMeans
        from sklearn.exceptions import ConvergenceWarning
        import warnings

        vectorizer = TfidfVectorizer(
            min_df=1,
            max_df=0.95,
            ngram_range=(1, 2),
            sublinear_tf=True,
        )
        matrix = vectorizer.fit_transform(docs)

        max_possible = min(len(tagged), 50)
        if n_clusters is None:
            n_clusters = auto_n_clusters(matrix, min_k=2, max_k=min(max_possible, 20))

        n_clusters = max(2, min(n_clusters, len(tagged)))

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ConvergenceWarning)
            km = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
            labels = km.fit_predict(matrix)

        # Build cluster summaries
        clusters = {}
        for bm, label in zip(tagged, labels):
            label = int(label)
            if label not in clusters:
                clusters[label] = {"bookmark_ids": [], "all_tags": []}
            clusters[label]["bookmark_ids"].append(bm.id)
            clusters[label]["all_tags"].extend(bm.tags or [])

        result = []
        for label, info in sorted(clusters.items()):
            tag_counts = Counter(info["all_tags"])
            top_tags = [t for t, _ in tag_counts.most_common(5)]
            name = ", ".join(top_tags[:3]) if top_tags else f"Cluster {label + 1}"
            result.append({
                "id": label,
                "name": name,
                "bookmark_ids": info["bookmark_ids"],
                "top_tags": top_tags,
            })

        return result

    except Exception as exc:
        logger.error("Clustering failed: %s", exc)
        return []


def auto_n_clusters(matrix, min_k: int = 2, max_k: int = 20) -> int:
    """
    Find the optimal number of clusters using silhouette score.
    Falls back to a heuristic if sklearn is unavailable or there are too few samples.
    """
    n_samples = matrix.shape[0]
    max_k = min(max_k, n_samples - 1)
    if max_k < min_k:
        return min_k

    try:
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score
        import warnings
        from sklearn.exceptions import ConvergenceWarning

        best_k = min_k
        best_score = -1.0

        for k in range(min_k, max_k + 1):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", ConvergenceWarning)
                km = KMeans(n_clusters=k, random_state=42, n_init=10)
                labels = km.fit_predict(matrix)
            try:
                score = silhouette_score(matrix, labels, sample_size=min(500, n_samples))
                if score > best_score:
                    best_score = score
                    best_k = k
            except Exception:
                continue

        logger.debug("auto_n_clusters: best_k=%d (score=%.4f)", best_k, best_score)
        return best_k

    except ImportError:
        # Heuristic: sqrt(n/2)
        return max(min_k, min(max_k, int((n_samples / 2) ** 0.5)))
