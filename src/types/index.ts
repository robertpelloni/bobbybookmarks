export interface Bookmark {
  id: number;
  url: string;
  title: string;
  description: string;
  page_title: string;
  page_description: string;
  research_status: 'pending' | 'running' | 'done' | 'failed' | 'skipped';
  imported_at: string;
  researched_at?: string;
  cluster_id?: number;
  source: string;
  is_duplicate: boolean;
  original_id?: number;
}

export interface Stats {
  total: number;
  unique: number;
  clusters: number;
  duplicates: number;
  research?: {
    pending: number;
    running: number;
    done: number;
    failed: number;
    skipped: number;
  };
}

export interface WorkerStatus {
  running: boolean;
  worker_mode: 'stopped' | 'app' | 'external';
  pending: number;
  running_count: number;
  done: number;
  failed: number;
}
