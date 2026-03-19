import { useState, useEffect } from 'react'
import axios from 'axios'
import { Search, ExternalLink, Tag as TagIcon, LayoutGrid } from 'lucide-react'
import './App.css'

function App() {
  const [bookmarks, setBookmarks] = useState([])
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCategory, setSelectedCategory] = useState(null)

  const [lastUpdated, setLastUpdated] = useState(new Date().toLocaleTimeString())

  useEffect(() => {
    fetchData()
    fetchCategories()
    const interval = setInterval(() => {
      fetchData(searchTerm, selectedCategory)
      setLastUpdated(new Date().toLocaleTimeString())
    }, 10000) // Refresh every 10s
    return () => clearInterval(interval)
  }, [searchTerm, selectedCategory])

  const fetchData = async (q = '', cat = null) => {
    setLoading(true)
    try {
      let url = 'http://localhost:3001/api/bookmarks'
      const params = {}
      if (q) params.q = q
      if (cat) params.category = cat
      
      const response = await axios.get(url, { params })
      setBookmarks(response.data)
    } catch (error) {
      console.error("Error fetching bookmarks:", error)
    } finally {
      setLoading(false)
    }
  }

  const fetchCategories = async () => {
    try {
      const response = await axios.get('http://localhost:3001/api/categories')
      setCategories(response.data)
    } catch (error) {
      console.error("Error fetching categories:", error)
    }
  }

  const handleSearch = (e) => {
    const value = e.target.value
    setSearchTerm(value)
    fetchData(value, selectedCategory)
  }

  const toggleCategory = (cat) => {
    const newCat = selectedCategory === cat ? null : cat
    setSelectedCategory(newCat)
    fetchData(searchTerm, newCat)
  }

  // Fallback parsing for raw lines if needed
  const renderDescription = (bookmark) => {
    if (bookmark.short_description) return bookmark.short_description
    // If our server parsing was too simple, we can try to extract from raw line here
    return "Click to view details"
  }

  return (
    <div className="dashboard">
      <header>
        <div>
          <h1>Bobby's Bookmark Research</h1>
          <div style={{ display: 'flex', gap: '1rem', alignItems: 'center', marginTop: '0.5rem' }}>
            <p style={{ color: 'var(--text-muted)', margin: 0 }}>
              {bookmarks.length} Research-Backed Links
            </p>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.75rem', color: '#10b981' }}>
              <div className="pulse-dot"></div>
              Live Processing (Last sync: {lastUpdated})
            </div>
          </div>
        </div>
        <LayoutGrid color="var(--accent-color)" size={32} />
      </header>

      <div className="search-container">
        <div style={{ position: 'relative', flex: 1 }}>
          <Search 
            size={20} 
            color="var(--text-muted)" 
            style={{ position: 'absolute', left: '1rem', top: '50%', transform: 'translateY(-50%)' }} 
          />
          <input 
            type="text" 
            placeholder="Search through researched content..." 
            value={searchTerm}
            onChange={handleSearch}
            style={{ paddingLeft: '3rem' }}
          />
        </div>
      </div>

      <div className="category-filters">
        <div 
          className={`category-tag ${selectedCategory === null ? 'active' : ''}`}
          onClick={() => toggleCategory(null)}
        >
          All
        </div>
        {categories.map(cat => (
          <div 
            key={cat} 
            className={`category-tag ${selectedCategory === cat ? 'active' : ''}`}
            onClick={() => toggleCategory(cat)}
          >
            {cat}
          </div>
        ))}
      </div>

      {loading ? (
        <div className="loading">Analyzing codebases...</div>
      ) : (
        <div className="bookmark-grid">
          {bookmarks.map((bm, index) => (
            <div key={index} className="bookmark-card">
              <h3>{bm.short_description || "Project Reference"}</h3>
              <a href={bm.url} target="_blank" rel="noopener noreferrer" className="bookmark-url">
                {bm.url} <ExternalLink size={12} style={{ marginLeft: '4px' }} />
              </a>
              <div className="bookmark-desc">
                {/* Attempt to show more info if it exists in raw_content */}
                {bm.raw_content.split(', ').slice(3, 4)}
              </div>
              <div className="bookmark-footer">
                <div className="tag" style={{ background: 'rgba(129, 140, 248, 0.1)', color: '#818cf8' }}>
                  {bm.category}
                </div>
                {/* Extract tags from raw_content if they are in the expected column */}
                {bm.raw_content.split(', ').slice(4, 5).join('').split(',').map(tag => (
                  tag.trim() && <div key={tag} className="tag">{tag.trim()}</div>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App
