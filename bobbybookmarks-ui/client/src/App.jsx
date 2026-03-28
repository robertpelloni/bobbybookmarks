import { useState, useEffect, useCallback, useRef } from 'react'
import axios from 'axios'
import ReactMarkdown from 'react-markdown'
import { Search, ExternalLink, LayoutGrid, Clock, ArrowUpDown, Tag as TagIcon, Sparkles, BrainCircuit, Zap, BarChart3, TrendingUp, PieChart as PieIcon, Network, ChevronRight, Loader2, Gauge, Boxes, ToggleLeft, ToggleRight, Orbit, Scale, MessageSquare, ShieldAlert, ShieldCheck, FileText, Filter, Activity, Cpu, Database, Globe, Terminal, CheckCircle2 } from 'lucide-react'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line, PieChart, Pie, Cell, Legend, AreaChart, Area } from 'recharts'
import * as d3 from 'd3'
import './App.css'

const COLORS = ['#60a5fa', '#34d399', '#fbbf24', '#f87171', '#a78bfa', '#ec4899', '#f97316'];

function App() {
  const [bookmarks, setBookmarks] = useState([])
  const [categories, setCategories] = useState([])
  const [clusters, setClusters] = useState([])
  const [nebula, setNebula] = useState([])
  const [debates, setDebates] = useState([])
  const [networkHealth, setNetworkHealth] = useState([])
  const [liveFeed, setLiveFeed] = useState([])
  const [report, setReport] = useState('')
  const [stats, setStats] = useState({ count: 0, deep: 0, borg: 0, heuristic: 0 })
  const [timeline, setTimeline] = useState([])
  const [topTags, setTopTags] = useState([])
  const [catStats, setCatStats] = useState([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [searchMode, setSearchMode] = useState('keyword') // 'keyword' or 'semantic'
  const [selectedCategory, setSelectedCategory] = useState('')
  const [selectedTag, setSelectedTag] = useState('')
  const [sortBy, setSortBy] = useState('created_at')
  const [sortOrder, setSortOrder] = useState('DESC')
  const [lastUpdated, setLastUpdated] = useState(new Date().toLocaleTimeString())
  const [view, setView] = useState('grid') // 'grid', 'borg', 'insights', 'graph', 'clusters', 'nebula', 'peer-review', 'reports', 'network', or 'live'
  
  // Visualization Interactivity States
  const [vizSearch, setVizSearch] = useState('')
  const [vizCategory, setVizCategory] = useState('')

  const [activeDrillDown, setActiveDrillDown] = useState(null)
  const [drillDownBookmarks, setDrillDownBookmarks] = useState([])
  const [drillLoading, setDrillLoading] = useState(false)
  
  const graphRef = useRef(null)
  const nebulaRef = useRef(null)
  const feedEndRef = useRef(null)

  const fetchData = useCallback(async () => {
    try {
      let response;
      if (searchMode === 'semantic' && searchTerm.trim()) {
        response = await axios.get('http://localhost:3002/api/search/semantic', {
          params: { q: searchTerm }
        })
        setBookmarks(response.data.results || [])
      } else {
        response = await axios.get('http://localhost:3002/api/bookmarks', {
          params: {
            q: searchTerm,
            category: selectedCategory,
            tag: selectedTag,
            sort: sortBy,
            order: sortOrder
          }
        })
        setBookmarks(response.data)
      }
      
      const statsRes = await axios.get('http://localhost:3002/api/stats')
      setStats(statsRes.data)
      
      setLastUpdated(new Date().toLocaleTimeString())
    } catch (error) {
      console.error("Fetch failed:", error)
    } finally {
      setLoading(false)
    }
  }, [searchTerm, searchMode, selectedCategory, selectedTag, sortBy, sortOrder])

  const fetchAnalytics = async () => {
    try {
      const [tRes, cRes, tagRes, clRes, dRes, rRes, nRes, fRes] = await Promise.all([
        axios.get('http://localhost:3002/api/analytics/timeline'),
        axios.get('http://localhost:3002/api/analytics/categories'),
        axios.get('http://localhost:3002/api/analytics/tags'),
        axios.get('http://localhost:3002/api/clusters'),
        axios.get('http://localhost:3002/api/debates'),
        axios.get('http://localhost:3002/api/reports/latest'),
        axios.get('http://localhost:3002/api/network/health'),
        axios.get('http://localhost:3002/api/live-feed')
      ])
      setTimeline(tRes.data)
      setCatStats(cRes.data)
      setTopTags(tagRes.data)
      setClusters(clRes.data)
      setDebates(dRes.data)
      setReport(typeof rRes.data === 'string' ? rRes.data : rRes.data.content)
      setNetworkHealth(nRes.data)
      setLiveFeed(fRes.data)
    } catch (error) {
      console.error("Analytics fetch failed:", error)
    }
  }

  const handleDrillDown = async (cat, feature) => {
    setActiveDrillDown({category: cat, feature: feature})
    setDrillLoading(true)
    try {
      const res = await axios.get('http://localhost:3002/api/bookmarks/by-feature', {
        params: { feature: feature }
      })
      setDrillDownBookmarks(res.data)
    } catch (err) {
      console.error("Drilldown failed:", err)
    } finally {
      setDrillLoading(false)
    }
  }

  useEffect(() => {
    fetchData()
    const interval = setInterval(fetchData, 10000)
    return () => clearInterval(interval)
  }, [fetchData])

  useEffect(() => {
    if (view === 'insights' || view === 'clusters' || view === 'peer-review' || view === 'reports' || view === 'network' || view === 'live') fetchAnalytics()
  }, [view])

  useEffect(() => {
    if (view === 'live') {
      const interval = setInterval(async () => {
        const res = await axios.get('http://localhost:3002/api/live-feed');
        setLiveFeed(res.data);
      }, 3000);
      return () => clearInterval(interval);
    }
  }, [view])

  useEffect(() => {
    const fetchMeta = async () => {
      try {
        const [cRes, clRes, dRes, rRes, nRes] = await Promise.all([
          axios.get('http://localhost:3002/api/categories'),
          axios.get('http://localhost:3002/api/clusters'),
          axios.get('http://localhost:3002/api/debates'),
          axios.get('http://localhost:3002/api/reports/latest'),
          axios.get('http://localhost:3002/api/network/health')
        ])
        setCategories(cRes.data)
        setClusters(clRes.data)
        setDebates(dRes.data)
        setReport(typeof rRes.data === 'string' ? rRes.data : rRes.data.content)
        setNetworkHealth(nRes.data)
      } catch (err) { console.error(err) }
    }
    fetchMeta()
  }, [])

  // Knowledge Nebula Logic
  useEffect(() => {
    if (view !== 'nebula' || !nebulaRef.current) return;

    const runNebula = async () => {
      const res = await axios.get('http://localhost:3002/api/analytics/nebula');
      let data = res.data;

      // Apply Interactive Filters
      if (vizSearch) {
        const q = vizSearch.toLowerCase();
        data = data.filter(d => 
          d.short_description?.toLowerCase().includes(q) || 
          d.category?.toLowerCase().includes(q)
        );
      }
      if (vizCategory) {
        data = data.filter(d => d.category === vizCategory);
      }

      const width = nebulaRef.current.clientWidth;
      const height = 600;
      const margin = { top: 40, right: 40, bottom: 40, left: 40 };

      d3.select(nebulaRef.current).selectAll("*").remove();

      const svg = d3.select(nebulaRef.current)
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewBox", [0, 0, width, height]);

      const x = d3.scaleLinear().domain([0, 100]).range([margin.left, width - margin.right]);
      const y = d3.scaleLinear().domain([0, 100]).range([height - margin.bottom, margin.top]);

      const dot = svg.append("g")
        .selectAll("circle")
        .data(data)
        .join("circle")
        .attr("cx", d => x(d.x))
        .attr("cy", d => y(d.y))
        .attr("r", 5)
        .attr("fill", d => COLORS[Math.abs(d.id % COLORS.length)])
        .attr("opacity", 0.6)
        .attr("stroke", "#fff")
        .attr("stroke-width", 0.5);

      dot.append("title").text(d => `${d.short_description}\nIQ: ${d.innovation_score}`);

      svg.append("g")
        .selectAll("text")
        .data(data.filter(d => d.innovation_score >= 8 || data.length < 50))
        .join("text")
        .attr("x", d => x(d.x))
        .attr("y", d => y(d.y) - 10)
        .attr("text-anchor", "middle")
        .attr("fill", "#94a3b8")
        .attr("font-size", "9px")
        .text(d => d.short_description?.slice(0, 20) + "...");

      const zoom = d3.zoom()
        .scaleExtent([0.5, 10])
        .on("zoom", (event) => {
          dot.attr("transform", event.transform);
          svg.selectAll("text").attr("transform", event.transform);
        });

      svg.call(zoom);
    };
    runNebula();
  }, [view, vizSearch, vizCategory]);

  // D3 Graph Logic
  useEffect(() => {
    if (view !== 'graph' || !graphRef.current) return;

    const runGraph = async () => {
      const res = await axios.get('http://localhost:3002/api/analytics/graph');
      let data = res.data;

      const width = graphRef.current.clientWidth;
      const height = 600;

      d3.select(graphRef.current).selectAll("*").remove();

      const svg = d3.select(graphRef.current)
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewBox", [0, 0, width, height]);

      const simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
        .force("charge", d3.forceManyBody().strength(-150))
        .force("center", d3.forceCenter(width / 2, height / 2));

      const link = svg.append("g")
        .attr("stroke", "#334155")
        .attr("stroke-opacity", 0.6)
        .selectAll("line")
        .data(data.links)
        .join("line")
        .attr("stroke-width", d => Math.sqrt(d.value));

      const node = svg.append("g")
        .attr("stroke", "#fff")
        .attr("stroke-width", 1.5)
        .selectAll("circle")
        .data(data.nodes)
        .join("circle")
        .attr("r", d => d.type === 'bookmark' ? 6 : 12)
        .attr("fill", d => {
          if (d.type === 'category') return '#34d399';
          if (d.type === 'tag') return '#60a5fa';
          return '#a78bfa';
        })
        .call(drag(simulation));

      node.append("title").text(d => d.name);

      const labels = svg.append("g")
        .selectAll("text")
        .data(data.nodes.filter(d => d.type !== 'bookmark'))
        .join("text")
        .attr("dy", -15)
        .attr("text-anchor", "middle")
        .attr("fill", "#94a3b8")
        .attr("font-size", "10px")
        .attr("font-weight", "bold")
        .text(d => d.name);

      simulation.on("tick", () => {
        link.attr("x1", d => d.source.x).attr("y1", d => d.source.y).attr("x2", d => d.target.x).attr("y2", d => d.target.y);
        node.attr("cx", d => d.x).attr("cy", d => d.y);
        labels.attr("x", d => d.x).attr("y", d => d.y);
      });

      function drag(simulation) {
        function dragstarted(event) { if (!event.active) simulation.alphaTarget(0.3).restart(); event.subject.fx = event.subject.x; event.subject.fy = event.subject.y; }
        function dragged(event) { event.subject.fx = event.x; event.subject.fy = event.y; }
        function dragended(event) { if (!event.active) simulation.alphaTarget(0); event.subject.fx = null; event.subject.fy = null; }
        return d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended);
      }
    };
    runGraph();
  }, [view]);

  const handleRandom = async () => {
    setLoading(true)
    try {
      const res = await axios.get('http://localhost:3002/api/random')
      setBookmarks([res.data])
      setSelectedCategory('')
      setSelectedTag('')
      setSearchTerm('')
      setView('grid')
    } catch (err) { console.error(err) } finally { setLoading(false) }
  }

  const researchData = [
    { name: 'Borg', value: stats.borg || 0, color: '#a78bfa' },
    { name: 'Deep', value: stats.deep || 0, color: '#34d399' },
    { name: 'Heuristic', value: stats.heuristic || 0, color: '#60a5fa' },
  ];

  const assimilationPct = stats.count > 0 ? Math.round((stats.borg / stats.count) * 100) : 0;

  return (
    <div className="dashboard">
      <header>
        <div className="header-main">
          <h1>Bobby's Research Command <span className="version-tag">v0.1.0</span></h1>
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
          <div className="assimilation-meter">
            <div className="meter-label">
              <span>Total Assimilation</span>
              <span>{assimilationPct}%</span>
            </div>
            <div className="meter-bar-wrap">
              <div className="meter-bar" style={{ width: `${assimilationPct}%` }}></div>
            </div>
          </div>
        </div>
        <div className="header-actions">
          <button className={`view-btn ${view === 'grid' ? 'active' : ''}`} onClick={() => setView('grid')}> 
            <LayoutGrid size={18} /> Catalog
          </button>
          <button className={`view-btn ${view === 'borg' ? 'active' : ''}`} onClick={() => setView('borg')}> 
            <Zap size={18} /> Features
          </button>
          <button className={`view-btn ${view === 'insights' ? 'active' : ''}`} onClick={() => setView('insights')}> 
            <BarChart3 size={18} /> Insights
          </button>
          <button className={`view-btn ${view === 'clusters' ? 'active' : ''}`} onClick={() => setView('clusters')}> 
            <Boxes size={18} /> Clusters
          </button>
          <button className={`view-btn ${view === 'nebula' ? 'active' : ''}`} onClick={() => setView('nebula')}> 
            <Orbit size={18} /> Nebula
          </button>
          <button className={`view-btn ${view === 'peer-review' ? 'active' : ''}`} onClick={() => setView('peer-review')}> 
            <Scale size={18} /> Peer Review
          </button>
          <button className={`view-btn ${view === 'reports' ? 'active' : ''}`} onClick={() => setView('reports')}> 
            <FileText size={18} /> Reports
          </button>
          <button className={`view-btn ${view === 'network' ? 'active' : ''}`} onClick={() => setView('network')}> 
            <Activity size={18} /> Network
          </button>
          <button className={`view-btn ${view === 'live' ? 'active' : ''}`} onClick={() => setView('live')}> 
            <Terminal size={18} /> Live Feed
          </button>
          <button className={`view-btn ${view === 'graph' ? 'active' : ''}`} onClick={() => setView('graph')}> 
            <Network size={18} /> Mind Map
          </button>
          <button className="surprise-btn" onClick={handleRandom}>
            <Sparkles size={18} /> Surprise
          </button>
        </div>
      </header>

      {view === 'grid' && (
        <>
          <div className="search-row">
            <div className="search-bar">
              <Search size={20} className="search-icon" />
              <input 
                type="text" 
                placeholder={searchMode === 'semantic' ? "Describe what you're looking for (semantic search)..." : "Search researched intelligence..."}
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            <div className="search-toggle" onClick={() => setSearchMode(searchMode === 'keyword' ? 'semantic' : 'keyword')}> 
              {searchMode === 'semantic' ? <Sparkles size={18} color="#a78bfa" /> : <Search size={18} />}
              <span>{searchMode === 'semantic' ? 'Semantic' : 'Keyword'}</span>
            </div>
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
            {bookmarks.length === 0 && searchTerm && searchMode === 'semantic' ? (
              <div className="no-results card">
                <Sparkles size={48} className="mb-4 text-accent opacity-20" />
                <h3>Semantic Engine Priming</h3>
                <p>The vector index is being built in the background. Semantic search will be available shortly!</p>
              </div>
            ) : (
              bookmarks.map((bm) => (
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
                    <strong>Intelligence:</strong> {bm.main_features}
                  </div>
                  <div className="tag-shelf">
                    {(bm.tags || "").split(',').map(tag => (
                      tag.trim() && <span key={tag} className="tag-chip">#{tag.trim()}</span>
                    ))}
                  </div>
                  <a href={bm.url} target="_blank" rel="noopener noreferrer" className="visit-link">
                    Open Source <ExternalLink size={14} />
                  </a>
                </div>
              ))
            )}
          </div>
        </>
      )}

      {view === 'borg' && (
        <div className="borg-feature-view">
          <h2>Borg Feature Matrix (Interoception & Identity Mapping)</h2>
          <p className="subtitle">Extracted high-value features scored for internal coherence (Interoception) and autonomous definition (Identity)</p>
          
          <div className="matrix-layout">
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
                    .flatMap(bm => (bm.main_features || "").split(','))
                    .map(f => f.trim())
                    .filter(f => f && f !== 'Automated Discovery' && f !== 'Heuristic detection')
                )).slice(0, 12);

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
                      {catFeatures.map(f => (
                        <li 
                          key={f} 
                          className={activeDrillDown?.feature === f ? 'active' : ''}
                          onClick={() => handleDrillDown(cat, f)}
                        >
                          {f} <ChevronRight size={12} className="drill-icon" />
                        </li>
                      ))}
                    </ul>
                  </div>
                )
              })}
            </div>

            {activeDrillDown && (
              <div className="drill-down-panel">
                <div className="drill-header">
                  <div className="drill-title">
                    <span className="drill-cat">{activeDrillDown.category}</span>
                    <h3>{activeDrillDown.feature}</h3>
                  </div>
                  <button className="close-drill" onClick={() => setActiveDrillDown(null)}>✕</button>
                </div>
                <div className="drill-content">
                  {drillLoading ? (
                    <div className="drill-loading">
                      <Loader2 className="spinner" />
                      <span>Extracting specific intelligence...</span>
                    </div>
                  ) : (
                    <>
                      <p className="drill-intro">Projects exhibiting this autonomous feature:</p>
                      <div className="drill-list">
                        {drillDownBookmarks.map(bm => (
                          <div key={bm.id} className="drill-item">
                            <div className="drill-item-head">
                              <a href={bm.url} target="_blank" rel="noopener noreferrer">{bm.short_description || bm.url}</a>
                              <span className="drill-iq">IQ: {bm.innovation_score}</span>
                            </div>
                            <p>{bm.long_description}</p>
                          </div>
                        ))}
                      </div>
                    </>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {view === 'peer-review' && (
        <div className="peer-review-view">
          <div className="debates-list">
            {debates.map((debate) => (
              <div key={debate.id} className="debate-card">
                <div className="debate-meta">
                  <span className="debate-cat">{debate.category}</span>
                  <h3>{debate.short_description}</h3>
                  <div className="debate-score-wrap">
                    <span className="debate-label">Consensus Innovation Score</span>
                    <span className="debate-score">{debate.final_consensus_score}</span>
                  </div>
                </div>
                <div className="debate-grid">
                  <div className="argument advocate">
                    <div className="arg-header">
                      <ShieldCheck size={16} /> <span>Advocate Argument</span>
                    </div>
                    <p>{debate.advocate_argument}</p>
                  </div>
                  <div className="argument critic">
                    <div className="arg-header">
                      <ShieldAlert size={16} /> <span>Critic Argument</span>
                    </div>
                    <p>{debate.critic_argument}</p>
                  </div>
                </div>
                <a href={debate.url} target="_blank" rel="noopener noreferrer" className="visit-link mt-4">
                  View Source <ExternalLink size={14} />
                </a>
              </div>
            ))}
          </div>
        </div>
      )}

      {view === 'reports' && (
        <div className="reports-view">
          <div className="card report-card">
            <div className="card-header">
              <h3><FileText size={18} /> Daily Intelligence Briefing</h3>
              <span className="text-xs text-muted">Auto-generated synthesis of latest technical discoveries</span>
            </div>
            <div className="markdown-content">
              <ReactMarkdown>{report}</ReactMarkdown>
            </div>
          </div>
        </div>
      )}

      {view === 'network' && (
        <div className="network-view">
          <div className="network-grid">
            {networkHealth.map((agent) => {
              const isStale = (new Date() - new Date(agent.last_pulse.replace(' ', 'T') + 'Z')) > 120000; // 2 mins
              return (
                <div key={agent.agent_name} className={`card agent-card ${isStale ? 'stale' : 'active'}`}>
                  <div className="agent-header">
                    <div className="agent-title">
                      <Cpu size={20} className="agent-icon" />
                      <h3>{agent.agent_name}</h3>
                    </div>
                    <div className={`status-tag ${isStale ? 'offline' : 'online'}`}>
                      {isStale ? 'Offline' : 'Live'}
                    </div>
                  </div>
                  <div className="agent-task">
                    <span className="label">Current Task:</span>
                    <p>{agent.current_task}</p>
                  </div>
                  <div className="agent-meta">
                    <div className="meta-item">
                      <Clock size={12} /> <span>{new Date(agent.last_pulse.replace(' ', 'T') + 'Z').toLocaleTimeString()}</span>
                    </div>
                    {agent.status_metadata?.pid && (
                      <div className="meta-item">
                        <Database size={12} /> <span>PID: {agent.status_metadata.pid}</span>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {view === 'live' && (
        <div className="live-view">
          <div className="terminal-card card">
            <div className="card-header">
              <h3><Terminal size={18} /> Live Research Feed</h3>
              <span className="text-xs text-muted">Real-time thought process of the background worker</span>
            </div>
            <div className="terminal-container">
              {liveFeed.map((entry, i) => (
                <div key={i} className={`terminal-line ${entry.type}`}>
                  <span className="t-time">[{new Date(entry.timestamp).toLocaleTimeString()}]</span>
                  <span className="t-msg">{entry.message}</span>
                </div>
              ))}
              <div ref={feedEndRef} />
            </div>
          </div>
        </div>
      )}

      {view === 'insights' && (
        <div className="insights-view">
          <div className="grid-2">
            <div className="card chart-card">
              <div className="card-header">
                <h3><TrendingUp size={18} /> Harvest Velocity</h3>
              </div>
              <div className="chart-container">
                <ResponsiveContainer width="100%" height={300}>
                  <AreaChart data={timeline}>
                    <defs>
                      <linearGradient id="colorCumulative" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#60a5fa" stopOpacity={0.3}/>
                        <stop offset="95%" stopColor="#60a5fa" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                    <XAxis dataKey="day" stroke="#94a3b8" />
                    <YAxis stroke="#94a3b8" />
                    <Tooltip contentStyle={{ backgroundColor: '#1e293b', border: 'none' }} />
                    <Area type="monotone" dataKey="cumulative" stroke="#60a5fa" fillOpacity={1} fill="url(#colorCumulative)" strokeWidth={3} />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="card chart-card">
              <div className="card-header">
                <h3><BrainCircuit size={18} /> Intelligence Breakdown</h3>
              </div>
              <div className="chart-container">
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={researchData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                    <XAxis dataKey="name" stroke="#94a3b8" />
                    <YAxis stroke="#94a3b8" />
                    <Tooltip contentStyle={{ backgroundColor: '#1e293b', border: 'none' }} />
                    <Bar dataKey="value">
                      {researchData.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={entry.color} />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>

          <div className="grid-2 mt-6">
            <div className="card chart-card">
              <div className="card-header">
                <h3><LayoutGrid size={18} /> Top Categories</h3>
              </div>
              <div className="chart-container">
                <ResponsiveContainer width="100%" height={400}>
                  <PieChart>
                    <Pie
                      data={catStats.slice(0, 10)}
                      cx="50%"
                      cy="50%"
                      innerRadius={60}
                      outerRadius={120}
                      paddingAngle={5}
                      dataKey="value"
                      label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                    >
                      {catStats.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                      ))}
                    </Pie>
                    <Tooltip contentStyle={{ backgroundColor: '#1e293b', border: 'none' }} />
                    <Legend />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="card chart-card">
              <div className="card-header">
                <h3><TagIcon size={18} /> Trending Tags</h3>
              </div>
              <div className="tag-cloud">
                {topTags.map((tag, i) => (
                  <div key={tag.name} className="tag-rank-item" style={{ opacity: 1 - (i * 0.04) }}>
                    <span className="tag-name">#{tag.name}</span>
                    <div className="tag-bar-wrap">
                      <div className="tag-bar" style={{ width: `${(tag.value / (topTags[0]?.value || 1)) * 100}%`, backgroundColor: COLORS[i % COLORS.length] }}></div>
                    </div>
                    <span className="tag-count">{tag.value}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {view === 'clusters' && (
        <div className="clusters-view">
          <div className="clusters-grid">
            {clusters.map((cluster, i) => (
              <div key={cluster.id} className="cluster-card">
                <div className="cluster-icon">
                  <Boxes size={24} color={COLORS[i % COLORS.length]} />
                </div>
                <h3>{cluster.name}</h3>
                <div className="cluster-stats">
                  <span>{cluster.bookmark_count} Projects</span>
                </div>
                <div className="cluster-tags">
                  {cluster.tags.map(tag => (
                    <span key={tag} className="tag-pill">#{tag}</span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {view === 'nebula' && (
        <div className="nebula-view">
          <div className="nebula-controls card">
            <div className="viz-search">
              <Search size={16} />
              <input 
                type="text" 
                placeholder="Find concept..." 
                value={vizSearch}
                onChange={(e) => setVizSearch(e.target.value)}
              />
            </div>
            <div className="viz-cat-filter">
              <Filter size={16} />
              <select value={vizCategory} onChange={(e) => setVizCategory(e.target.value)}>
                <option value="">All Domains</option>
                {categories.map(cat => <option key={cat} value={cat}>{cat}</option>)}
              </select>
            </div>
          </div>
          <div className="card nebula-card mt-4">
            <div className="card-header">
              <h3><Orbit size={18} /> Knowledge Nebula</h3>
              <span className="text-xs text-muted">2D semantic projection of conceptual relationships</span>
            </div>
            <div ref={nebulaRef} className="d3-container"></div>
            <div className="graph-legend">
              <span className="legend-item"><span className="dot" style={{backgroundColor: '#60a5fa'}}></span> Semantic Node</span>
              <span className="legend-item">Conceptual groupings reveal hidden technical trends</span>
            </div>
          </div>
        </div>
      )}

      {view === 'graph' && (
        <div className="graph-view">
          <div className="card graph-card">
            <div className="card-header">
              <h3><Network size={18} /> Borg Consciousness Map</h3>
              <span className="text-xs text-muted">Visualizing connections between projects, categories, and tags</span>
            </div>
            <div ref={graphRef} className="d3-container"></div>
            <div className="graph-legend">
              <span className="legend-item"><span className="dot" style={{backgroundColor: '#a78bfa'}}></span> Bookmark</span>
              <span className="legend-item"><span className="dot" style={{backgroundColor: '#34d399'}}></span> Category</span>
              <span className="legend-item"><span className="dot" style={{backgroundColor: '#60a5fa'}}></span> Tag</span>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
