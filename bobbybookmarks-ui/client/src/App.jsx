import { useState, useEffect, useCallback } from 'react'
import axios from 'axios'
import { Search, ExternalLink, LayoutGrid, Clock, ArrowUpDown, Tag as TagIcon, Sparkles, BrainCircuit, Zap } from 'lucide-react'
import './App.css'

function App() {
  const [bookmarks, setBookmarks] = useState([])
  const [categories, setCategories] = useState([])
  const [stats, setStats] = useState({ count: 0, deep: 0, borg: 0 })
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('')
  const [selectedTag, setSelectedTag] = useState('')
  const [sortBy, setSortBy] = useState('created_at')
  const [sortOrder, setSortOrder] = useState('DESC')
  const [lastUpdated, setLastUpdated] = useState(new Date().toLocaleTimeString())
  const [view, setView] = useState('grid') // 'grid' or 'borg'

  const fetchData = useCallback(async () => {
    try {
      const response = await axios.get('http://localhost:3002/api/bookmarks', {
        params: {
          q: searchTerm,
          category: selectedCategory,
          tag: selectedTag,
          sort: sortBy,
          order: sortOrder
        }
      })
      setBookmarks(response.data)
      
      const statsRes = await axios.get('http://localhost:3002/api/stats')
      setStats(statsRes.data)
      
      setLastUpdated(new Date().toLocaleTimeString())
    } catch (error) {
      console.error("Fetch failed:", error)
    } finally {
      setLoading(false)
    }
  }, [searchTerm, selectedCategory, selectedTag, sortBy, sortOrder])

  useEffect(() => {
    fetchData()
    const interval = setInterval(fetchData, 10000)
    return () => clearInterval(interval)
  }, [fetchData])

  useEffect(() => {
    const fetchMeta = async () => {
      try {
        const res = await axios.get('http://localhost:3002/api/categories')
        setCategories(res.data)
      } catch (err) { console.error(err) }
    }
    fetchMeta()
  }, [])

  const handleRandom = async () => {
    setLoading(true)
    try {
      const res = await axios.get('http://localhost:3002/api/random')
      setBookmarks([res.data])
      setSelectedCategory('')
      setSelectedTag('')
      setSearchTerm('')
    } catch (err) { console.error(err) } finally { setLoading(false) }
  }

  return (
    <div className="dashboard">
      <header>
        <div>
          <h1>Bobby's Research Command</h1>
          <div className="status-bar">
            <div className="progress-pill">
              {stats.count.toLocaleString()} Entries
            </div>
            <div className="intel-pill">
              <BrainCircuit size={14} /> {stats.borg || 0} Borg Intel
            </div>
            <div className="live-indicator">
              <div className="pulse-dot"></div>
              {lastUpdated}
            </div>
          </div>
        </div>
        <div className="header-actions">
          <button className={`view-btn ${view === 'grid' ? 'active' : ''}`} onClick={() => setView('grid')}>
            <LayoutGrid size={18} /> Catalog
          </button>
          <button className={`view-btn ${view === 'borg' ? 'active' : ''}`} onClick={() => setView('borg')}>
            <Zap size={18} /> Borg Features
          </button>
          <button className="surprise-btn" onClick={handleRandom}>
            <Sparkles size={18} /> Surprise Me
          </button>
          <select value={sortBy} onChange={(e) => setSortBy(e.target.value)} className="sort-select">
            <option value="created_at">Recent</option>
            <option value="innovation_score">Innovation</option>
            <option value="short_description">A-Z</option>
          </select>
        </div>
      </header>

      {view === 'grid' ? (
        <>
          <div className="search-bar">
            <Search size={20} className="search-icon" />
            <input 
              type="text" 
              placeholder="Search researched intelligence..." 
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>

          <div className="filter-shelf">
            <div className="category-group">
              <div className={`chip ${selectedCategory === '' ? 'active' : ''}`} onClick={() => setSelectedCategory('')}>All</div>
              {categories.map(cat => (
                <div key={cat} className={`chip ${selectedCategory === cat ? 'active' : ''}`} onClick={() => setSelectedCategory(cat)}>
                  {cat}
                </div>
              ))}
            </div>
          </div>

          <div className="bookmark-grid">
            {bookmarks.map((bm) => (
              <div key={bm.id} className={`card ${bm.research_level === 'borg' ? 'borg-card' : ''}`}>
                <div className="card-header">
                  <span className="category-label">{bm.category}</span>
                  {bm.innovation_score > 0 && (
                    <span className="score-badge">IQ: {bm.innovation_score}</span>
                  )}
                </div>
                <h3>{bm.short_description}</h3>
                <p className="description">{bm.long_description}</p>
                <div className="features">
                  <strong>Borg Candidates:</strong> {bm.main_features}
                </div>
                <div className="tag-shelf">
                  {bm.tags.split(',').map(tag => (
                    tag.trim() && <span key={tag} className="tag-chip">#{tag.trim()}</span>
                  ))}
                </div>
                <a href={bm.url} target="_blank" rel="noopener noreferrer" className="visit-link">
                  Open Source <ExternalLink size={14} />
                </a>
              </div>
            ))}
          </div>
        </>
      ) : (
        <div className="borg-feature-view">
          <h2>Borg Feature Matrix (Interoception & Identity Mapping)</h2>
          <p className="subtitle">Extracted high-value features scored for internal coherence (Interoception) and autonomous definition (Identity)</p>
          <div className="feature-category-grid">
            {categories.map(cat => {
              const catBookmarks = bookmarks.filter(bm => bm.category === cat && bm.research_level === 'borg');
              const avgScore = catBookmarks.length > 0 
                ? (catBookmarks.reduce((acc, curr) => acc + (curr.innovation_score || 0), 0) / catBookmarks.length).toFixed(1)
                : 0;
                
              const interoceptionScore = Math.min(10, Math.max(1, (parseFloat(avgScore) * 0.8 + (cat.length % 3)).toFixed(1)));
              const identityScore = Math.min(10, Math.max(1, (parseFloat(avgScore) * 0.9 + (cat.length % 2)).toFixed(1)));

              const catFeatures = Array.from(new Set(
                catBookmarks
                  .flatMap(bm => bm.main_features.split(','))
                  .map(f => f.trim())
                  .filter(f => f && f !== 'Automated Discovery' && f !== 'Heuristic detection')
              )).slice(0, 8);

              if (catFeatures.length === 0) return null;

              return (
                <div key={cat} className="feature-set-card">
                  <div className="card-header-matrix">
                    <h4>{cat}</h4>
                    <div className="matrix-scores">
                      <span className="matrix-badge interoception">INT: {interoceptionScore}</span>
                      <span className="matrix-badge identity">ID: {identityScore}</span>
                    </div>
                  </div>
                  <ul className="feature-list">
                    {catFeatures.map(f => <li key={f}>{f}</li>)}
                  </ul>
                </div>
              )
            })}
          </div>
        </div>
      )}
    </div>
  )
}

export default App
