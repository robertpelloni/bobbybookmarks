import React, { useState, useRef, useEffect, useMemo } from 'react';
import { 
  Database, LayoutGrid, Gauge, Zap, 
  Cpu, Sparkles, Scale, Search, 
  ArrowRight, Tag as TagIcon, MoreVertical,
  Upload, FileText, Globe, Link,
  Activity, Layers, Fingerprint, Shield,
  Terminal, Share2, Box, Radio, Crosshair
} from 'lucide-react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';
import { motion, AnimatePresence } from 'framer-motion';
import * as d3 from 'd3';
import { Bookmark, Stats, WorkerStatus } from './types';

// --- Clean Utility UI Kit ---

const StandardCard = ({ children, title, icon: Icon, className = "", onClick }: any) => {
  return (
    <div 
      className={`bg-white border border-slate-200 rounded-lg shadow-sm overflow-hidden flex flex-col ${className}`}
      onClick={onClick}
    >
      {title && (
        <div className="px-4 py-3 border-b border-slate-100 flex items-center justify-between bg-slate-50">
           <div className="flex items-center gap-2">
              {Icon && <Icon size={16} className="text-slate-500" />}
              <h3 className="text-xs font-bold text-slate-700 uppercase tracking-wider">{title}</h3>
           </div>
        </div>
      )}
      <div className="p-4 flex-1">
        {children}
      </div>
    </div>
  );
};

const StandardStat = ({ label, value, color = "blue", icon: Icon }: any) => {
  const colorMap: any = {
    blue: "text-blue-600 bg-blue-100",
    purple: "text-purple-600 bg-purple-100",
    green: "text-emerald-600 bg-emerald-100",
    yellow: "text-amber-600 bg-amber-100",
    red: "text-rose-600 bg-rose-100"
  };

  return (
    <div className="flex items-center justify-between p-3 bg-slate-50 rounded-lg border border-slate-100">
      <div className="flex items-center gap-3">
         {Icon && <Icon size={16} className="text-slate-400" />}
         <span className="text-xs font-medium text-slate-500 uppercase tracking-wide">{label}</span>
      </div>
      <span className={`text-sm font-bold ${colorMap[color].split(' ')[0]}`}>{value || 0}</span>
    </div>
  );
};

const TagCloud = ({ bookmarks = [] }: { bookmarks: Bookmark[] }) => {
  const tags = useMemo(() => {
    const counts: Record<string, number> = {};
    bookmarks.forEach(b => {
      const bTags = b.tags ? b.tags.split(',') : [];
      bTags.forEach(t => {
        const tag = t.trim().toUpperCase();
        if (tag) counts[tag] = (counts[tag] || 0) + 1;
      });
    });
    return Object.entries(counts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 40);
  }, [bookmarks]);

  return (
    <div className="flex flex-wrap gap-2">
      {tags.map(([tag, count]) => (
        <span 
          key={tag}
          className="px-2 py-1 bg-slate-100 border border-slate-200 rounded text-[10px] font-bold text-slate-600 hover:bg-blue-50 hover:text-blue-600 hover:border-blue-200 transition-colors cursor-default"
        >
          {tag} <span className="text-slate-400 ml-1">({count})</span>
        </span>
      ))}
    </div>
  );
};

// --- D3 FORCE GRAPH COMPONENT ---

const ForceGraph = ({ nodes = [], links = [] }: { nodes: any[], links: any[] }) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const svgRef = useRef<SVGSVGElement>(null);

  useEffect(() => {
    if (!containerRef.current || !svgRef.current) return;

    const width = containerRef.current.clientWidth;
    const height = containerRef.current.clientHeight;

    const svg = d3.select(svgRef.current)
      .attr("viewBox", [0, 0, width, height])
      .attr("style", "max-width: 100%; height: auto;");

    svg.selectAll("*").remove();

    if (nodes.length === 0) return;

    const simulation = d3.forceSimulation(nodes as any)
      .force("link", d3.forceLink(links).id((d: any) => d.id).distance((d: any) => d.target.group === 'cluster' ? 80 : 40))
      .force("charge", d3.forceManyBody().strength(-100))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("collision", d3.forceCollide().radius(15));

    const g = svg.append("g");

    // Glow Filter
    const filter = svg.append("defs").append("filter").attr("id", "glow");
    filter.append("feGaussianBlur").attr("stdDeviation", "2.5").attr("result", "coloredBlur");
    const feMerge = filter.append("feMerge");
    feMerge.append("feMergeNode").attr("in", "coloredBlur");
    feMerge.append("feMergeNode").attr("in", "SourceGraphic");

    const link = g.append("g")
      .attr("stroke", "#1e293b")
      .attr("stroke-opacity", 0.4)
      .selectAll("line")
      .data(links)
      .join("line")
      .attr("stroke-width", 1);

    const node = g.append("g")
      .selectAll("g")
      .data(nodes)
      .join("g")
      .call(d3.drag<any, any>()
        .on("start", (event, d) => {
          if (!event.active) simulation.alphaTarget(0.3).restart();
          d.fx = d.x; d.fy = d.y;
        })
        .on("drag", (event, d) => {
          d.fx = event.x; d.fy = event.y;
        })
        .on("end", (event, d) => {
          if (!event.active) simulation.alphaTarget(0);
          d.fx = null; d.fy = null;
        })
      );

    node.append("circle")
      .attr("r", (d: any) => d.group === 'root' ? 10 : d.group === 'cluster' ? 7 : 4)
      .attr("fill", (d: any) => d.group === 'root' ? "#3b82f6" : d.group === 'cluster' ? "#8b5cf6" : d.group === 'duplicate' ? "#f59e0b" : "#10b981")
      .attr("stroke", "#ffffff")
      .attr("stroke-width", 2);

    node.append("text")
      .text((d: any) => d.name)
      .attr("x", 12)
      .attr("y", 4)
      .attr("fill", "#64748b")
      .attr("font-size", "10px")
      .attr("font-weight", "600")
      .attr("class", "pointer-events-none select-none");

    simulation.on("tick", () => {
      link
        .attr("x1", (d: any) => d.source.x)
        .attr("y1", (d: any) => d.source.y)
        .attr("x2", (d: any) => d.target.x)
        .attr("y2", (d: any) => d.target.y);

      node.attr("transform", (d: any) => `translate(${d.x},${d.y})`);
    });

    // Zoom
    svg.call(d3.zoom<SVGSVGElement, unknown>()
      .extent([[0, 0], [width, height]])
      .scaleExtent([0.5, 4])
      .on("zoom", (event) => g.attr("transform", event.transform))
    );

  }, [nodes, links]);

  return (
    <div ref={containerRef} className="w-full h-full relative">
      <svg ref={svgRef} className="w-full h-full" />
    </div>
  );
};

function App() {
  const [view, setView] = useState<'intel' | 'ingest' | 'catalog' | 'terminal' | 'activity' | 'control' | 'analytics'>('intel');
  const [searchTerm, setSearchTerm] = useState('');
  const [ingestText, setIngestText] = useState('');
  const queryClient = useQueryClient();

  const { data: stats } = useQuery<Stats>({
    queryKey: ['stats'],
    queryFn: () => axios.get('/api/analytics/summary').then(res => res.data),
    refetchInterval: 10000,
  });

  const { data: timeline } = useQuery<any[]>({
    queryKey: ['analytics/timeline'],
    queryFn: () => axios.get('/api/analytics/timeline').then(res => res.data),
    refetchInterval: 30000,
  });

  const { data: categories } = useQuery<any[]>({
    queryKey: ['analytics/categories'],
    queryFn: () => axios.get('/api/analytics/categories').then(res => res.data),
    refetchInterval: 30000,
  });

  const { data: tagsData } = useQuery<any[]>({
    queryKey: ['analytics/tags'],
    queryFn: () => axios.get('/api/analytics/tags').then(res => res.data),
    refetchInterval: 30000,
  });

  const { data: systemLogs } = useQuery<string[]>({
    queryKey: ['system/logs'],
    queryFn: () => axios.get('/api/system/logs').then(res => res.data),
    refetchInterval: 5000,
  });

  const { data: battleCards } = useQuery<any[]>({
    queryKey: ['battle-cards'],
    queryFn: () => axios.get('/api/battle-cards').then(res => res.data),
    refetchInterval: 60000,
  });

  const { data: workerStatus } = useQuery<WorkerStatus>({
    queryKey: ['workerStatus'],
    queryFn: () => axios.get('/api/research/status').then(res => res.data),
    refetchInterval: 5000,
  });

  const { data: bookmarksData } = useQuery<{ bookmarks: Bookmark[], total: number }>({
    queryKey: ['bookmarks', searchTerm, view],
    queryFn: () => axios.get('/api/bookmarks', { params: { q: searchTerm, limit: view === 'intel' ? 100 : 200 } }).then(res => res.data),
  });

  const { data: graphData } = useQuery<{ nodes: any[], links: any[] }>({
    queryKey: ['analytics/graph'],
    queryFn: () => axios.get('/api/analytics/graph').then(res => res.data),
    refetchInterval: 60000,
  });

  const { data: liveFeed } = useQuery<Bookmark[]>({
    queryKey: ['live-feed'],
    queryFn: () => axios.get('/api/live-feed').then(res => res.data),
    refetchInterval: 5000,
  });

  const assimilateMutation = useMutation({
    mutationFn: (text: string) => axios.post('/api/bookmarks', { content: text }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['stats'] });
      queryClient.invalidateQueries({ queryKey: ['bookmarks'] });
      setView('catalog');
    }
  });

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 font-sans selection:bg-blue-100 flex flex-col">
      {/* Header */}
      <header className="h-16 border-b border-slate-200 bg-white z-[150] px-8 flex items-center justify-between shadow-sm">
         <div className="flex items-center gap-8">
            <div className="flex items-center gap-3 cursor-pointer" onClick={() => setView('intel')}>
               <div className="w-9 h-9 bg-blue-600 rounded-lg flex items-center justify-center text-white shadow-md shadow-blue-500/20">
                  <Zap size={20} className="fill-white" />
               </div>
               <div>
                  <h1 className="text-lg font-bold tracking-tight text-slate-900">BobbyIntel</h1>
                  <span className="text-[10px] font-bold text-slate-400 uppercase tracking-widest">v2.0.4 Unified</span>
               </div>
            </div>

            <nav className="flex items-center gap-1 p-1 bg-slate-100 rounded-lg">
              {[
                { id: 'intel', label: 'Intelligence', icon: Activity },
                { id: 'activity', label: 'Activity', icon: Radio },
                { id: 'analytics', label: 'Analytics', icon: Sparkles },
                { id: 'control', label: 'Control', icon: Gauge },
                { id: 'ingest', label: 'Ingest', icon: Share2 },
                { id: 'catalog', label: 'Catalog', icon: Box },
                { id: 'terminal', label: 'Terminal', icon: Terminal }
              ].map((m) => (
                <button 
                  key={m.id}
                  onClick={() => setView(m.id as any)}
                  className={`flex items-center gap-2 px-4 py-1.5 rounded-md text-xs font-semibold transition-all ${
                    view === m.id 
                      ? 'bg-white text-blue-600 shadow-sm' 
                      : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50'
                  }`}
                >
                  <m.icon size={14} />
                  {m.label}
                </button>
              ))}
            </nav>
         </div>

         <div className="flex items-center gap-6">
            <div className="relative group">
               <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" size={14} />
               <input 
                 type="text" 
                 placeholder="Search Knowledge Base..."
                 value={searchTerm}
                 onChange={(e) => setSearchTerm(e.target.value)}
                 className="w-64 bg-slate-100 border border-slate-200 rounded-lg pl-9 pr-4 py-2 text-xs font-medium focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:bg-white transition-all placeholder:text-slate-400"
               />
            </div>
         </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 overflow-hidden p-8 flex gap-8">
         <AnimatePresence mode="wait">
           {view === 'intel' && (
             <motion.div 
               key="intel"
               initial={{ opacity: 0, y: 10 }}
               animate={{ opacity: 1, y: 0 }}
               exit={{ opacity: 0, y: -10 }}
               className="flex-1 grid grid-cols-12 gap-8"
             >
                {/* Left Column - Stats */}
                <div className="col-span-3 space-y-6">
                   <StandardCard title="System Overview" icon={Gauge}>
                      <div className="space-y-3">
                         <StandardStat label="Total Items" value={stats?.total} color="blue" icon={Database} />
                         <StandardStat label="Clusters" value={stats?.clusters} color="purple" icon={Layers} />
                         <StandardStat label="Processed" value={stats?.research?.done} color="green" icon={Sparkles} />
                         <StandardStat label="Duplicates" value={stats?.duplicates} color="yellow" icon={Shield} />
                      </div>
                      
                      <div className="mt-6 pt-6 border-t border-slate-100 space-y-2">
                         <button 
                           onClick={() => axios.post('/api/research/start')}
                           className="w-full py-2 bg-blue-600 text-white rounded-md text-xs font-bold hover:bg-blue-700 active:scale-[0.98] transition-all"
                         >
                           {workerStatus?.running ? 'Engine Running' : 'Start Research'}
                         </button>
                         <button 
                           onClick={() => axios.post('/api/research/stop')}
                           className="w-full py-2 bg-white border border-slate-200 text-slate-700 rounded-md text-xs font-bold hover:bg-slate-50 active:scale-[0.98] transition-all"
                         >
                           Stop Engine
                         </button>
                         <button 
                           onClick={() => axios.post('/api/bookmarks/deduplicate')}
                           className="w-full py-2 bg-white border border-slate-200 text-amber-600 rounded-md text-xs font-bold hover:bg-amber-50 active:scale-[0.98] transition-all"
                         >
                           Remove Duplicates
                         </button>
                      </div>
                   </StandardCard>

                   <StandardCard title="Activity Level" icon={Cpu}>
                      <div className="h-20 flex items-end gap-1 px-1">
                         {Array.from({ length: 24 }).map((_, i) => (
                           <motion.div 
                             key={i}
                             animate={{ height: [10, Math.random() * 50 + 10, 10] }}
                             transition={{ repeat: Infinity, duration: 1.5 + Math.random(), ease: "easeInOut" }}
                             className="flex-1 bg-blue-100 rounded-t-sm"
                           />
                         ))}
                      </div>
                   </StandardCard>
                </div>

                {/* Center Column - Visual Map */}
                <div className="col-span-6 flex flex-col gap-6">
                   <StandardCard title="Knowledge Graph" icon={Globe} className="flex-1 min-h-[500px]">
                      <ForceGraph nodes={graphData?.nodes || []} links={graphData?.links || []} />
                   </StandardCard>
                   
                   <StandardCard title="Tag Cloud" icon={TagIcon}>
                      <TagCloud bookmarks={bookmarksData?.bookmarks || []} />
                   </StandardCard>
                </div>

                {/* Right Column - Logs */}
                <div className="col-span-3 flex flex-col h-full">
                   <StandardCard title="Recent Activity" icon={Activity} className="h-full">
                      <div className="space-y-3">
                         {(liveFeed || []).slice(0, 15).map((log, i) => (
                           <div key={log.id} className="flex flex-col border-l-2 border-slate-100 pl-3 py-1 group hover:border-blue-500 transition-all">
                              <span className="text-[10px] text-slate-400 font-medium">{new Date(log.imported_at || Date.now()).toLocaleTimeString()}</span>
                              <span className="text-xs font-bold text-slate-700 truncate">
                                {log.page_title || log.url}
                              </span>
                           </div>
                         ))}
                         {(!liveFeed || liveFeed.length === 0) && (
                           <div className="text-xs font-medium text-slate-400 text-center mt-20 italic">No activity detected</div>
                         )}
                      </div>
                   </StandardCard>
                </div>
             </motion.div>
           )}

           {view === 'ingest' && (
             <motion.div 
               key="ingest"
               initial={{ opacity: 0, scale: 0.98 }}
               animate={{ opacity: 1, scale: 1 }}
               exit={{ opacity: 0, scale: 1.02 }}
               className="flex-1 flex flex-col max-w-5xl mx-auto gap-8"
             >
                <div className="grid grid-cols-3 gap-6">
                   <StandardCard className="cursor-pointer group hover:bg-slate-50 transition-colors" onClick={() => window.location.href = '/api/database/download'}>
                      <div className="flex flex-col items-center gap-4 py-2">
                         <div className="w-12 h-12 rounded-lg bg-blue-50 flex items-center justify-center text-blue-600 border border-blue-100 group-hover:bg-blue-600 group-hover:text-white transition-all">
                            <Database size={24} />
                         </div>
                         <div className="text-center">
                            <span className="block text-xs font-bold text-slate-900">Export Database</span>
                            <span className="text-[10px] font-medium text-slate-400">Download .db file</span>
                         </div>
                      </div>
                   </StandardCard>
                   
                   <StandardCard className="cursor-pointer group hover:bg-slate-50 transition-colors">
                      <div className="flex flex-col items-center gap-4 py-2">
                         <div className="w-12 h-12 rounded-lg bg-slate-50 flex items-center justify-center text-slate-600 border border-slate-100 group-hover:bg-slate-600 group-hover:text-white transition-all">
                            <Upload size={24} />
                         </div>
                         <div className="text-center">
                            <span className="block text-xs font-bold text-slate-900">Import Data</span>
                            <span className="text-[10px] font-medium text-slate-400">Upload CSV/JSON</span>
                         </div>
                      </div>
                   </StandardCard>

                   <StandardCard className="cursor-pointer group hover:bg-slate-50 transition-colors">
                      <div className="flex flex-col items-center gap-4 py-2">
                         <div className="w-12 h-12 rounded-lg bg-amber-50 flex items-center justify-center text-amber-600 border border-amber-100 group-hover:bg-amber-600 group-hover:text-white transition-all">
                            <Radio size={24} />
                         </div>
                         <div className="text-center">
                            <span className="block text-xs font-bold text-slate-900">Live Stream</span>
                            <span className="text-[10px] font-medium text-slate-400">Direct injection</span>
                         </div>
                      </div>
                   </StandardCard>
                </div>

                <StandardCard title="Resource Import" icon={Terminal} className="flex-1">
                   <textarea 
                     value={ingestText}
                     onChange={(e) => setIngestText(e.target.value)}
                     className="w-full h-full bg-slate-50 border border-slate-200 rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-blue-500/20 font-mono text-xs text-slate-700 placeholder:text-slate-400 resize-none"
                     placeholder="Paste URLs or text content here to import..."
                   />
                   <div className="mt-4 flex justify-end">
                      <button 
                        onClick={() => {
                          if (ingestText.trim()) {
                            assimilateMutation.mutate(ingestText);
                            setIngestText('');
                          }
                        }}
                        disabled={assimilateMutation.isPending}
                        className="px-8 py-2.5 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-lg font-bold text-xs flex items-center gap-2 transition-all shadow-md shadow-blue-500/10"
                      >
                         <Zap size={14} className={assimilateMutation.isPending ? 'animate-spin' : ''} /> 
                         {assimilateMutation.isPending ? 'Processing...' : 'Import Resource'}
                      </button>
                   </div>
                </StandardCard>
             </motion.div>
           )}

           {view === 'catalog' && (
             <motion.div 
               key="catalog"
               initial={{ opacity: 0 }}
               animate={{ opacity: 1 }}
               exit={{ opacity: 0 }}
               className="flex-1 flex flex-col gap-8 overflow-y-auto max-h-[80vh] pr-4 custom-scrollbar"
             >
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 pb-20">
                  {(bookmarksData?.bookmarks || []).map((bm: Bookmark) => (
                    <StandardCard key={bm.id} title={bm.is_duplicate ? "Duplicate" : "Item"} icon={bm.is_duplicate ? Shield : Box} className="h-fit hover:border-blue-300 transition-colors group">
                      <div className="space-y-3">
                        <h4 className="text-xs font-bold text-slate-900 leading-snug group-hover:text-blue-600 transition-colors line-clamp-2">{bm.page_title || bm.url}</h4>
                        <p className="text-[10px] text-slate-500 font-medium leading-relaxed line-clamp-3 italic">
                          {bm.page_description || 'No description available'}
                        </p>
                        <div className="flex items-center justify-between pt-3 border-t border-slate-100">
                          <span className={`text-[9px] font-bold px-2 py-0.5 rounded ${bm.research_status === 'done' ? 'bg-emerald-50 text-emerald-600' : 'bg-blue-50 text-blue-600'} border border-slate-100 uppercase tracking-tighter`}>
                            {bm.research_status}
                          </span>
                          <div className="flex gap-3">
                             <a href={bm.url} target="_blank" rel="noreferrer" className="text-slate-400 hover:text-blue-600 transition-all">
                                <Globe size={14} />
                             </a>
                             <button className="text-slate-400 hover:text-slate-900 transition-all">
                                <ArrowRight size={14} />
                             </button>
                          </div>
                        </div>
                      </div>
                    </StandardCard>
                  ))}
                </div>
             </motion.div>
           )}

           {view === 'activity' && (
             <motion.div 
               key="activity"
               initial={{ opacity: 0, x: -20 }}
               animate={{ opacity: 1, x: 0 }}
               exit={{ opacity: 0, x: 20 }}
               className="flex-1 flex flex-col gap-8 overflow-y-auto max-h-[80vh] pr-4 custom-scrollbar"
             >
                <div className="space-y-4 max-w-5xl mx-auto w-full pb-20">
                  {(liveFeed || []).map((log) => (
                    <div key={log.id} className="flex items-center gap-6 p-4 bg-white/[0.02] border border-white/5 rounded-xl hover:bg-white/[0.05] transition-all group">
                       <div className={`p-2 rounded-lg ${log.research_status === 'done' ? 'bg-green-500/10 text-green-400' : 'bg-blue-500/10 text-blue-400'} border border-white/5`}>
                          <Fingerprint size={16} />
                       </div>
                       <div className="flex-1">
                          <div className="flex items-center justify-between mb-1">
                             <span className="text-[10px] font-black text-white tracking-widest uppercase truncate max-w-xl">{log.page_title || log.url}</span>
                             <span className="text-[8px] font-black text-slate-600 uppercase tracking-widest">{new Date(log.imported_at || Date.now()).toLocaleString()}</span>
                          </div>
                          <div className="text-[9px] text-slate-500 font-bold uppercase truncate max-w-2xl italic tracking-tighter">{log.url}</div>
                       </div>
                       <div className="flex gap-4 opacity-0 group-hover:opacity-100 transition-opacity">
                          <button onClick={() => window.open(log.url, '_blank')} className="px-4 py-1.5 bg-blue-500/10 border border-blue-500/20 text-blue-400 rounded-lg text-[8px] font-black tracking-widest uppercase hover:bg-blue-500/20 transition-all">
                             OPEN_NODE
                          </button>
                       </div>
                    </div>
                  ))}
                </div>
             </motion.div>
           )}

           {view === 'analytics' && (
             <motion.div 
               key="analytics"
               initial={{ opacity: 0, y: 10 }}
               animate={{ opacity: 1, y: 0 }}
               exit={{ opacity: 0, y: -10 }}
               className="flex-1 grid grid-cols-12 gap-8 overflow-y-auto max-h-[80vh] pr-4 custom-scrollbar"
             >
                <div className="col-span-8 space-y-8">
                   <StandardCard title="Harvest Velocity" icon={Activity}>
                      <div className="h-64 flex items-end gap-2 px-2">
                        {(timeline || []).slice().reverse().map((day: any, i: number) => (
                          <div key={i} className="flex-1 flex flex-col justify-end gap-1 group">
                             <div className="opacity-0 group-hover:opacity-100 transition-opacity text-[10px] text-blue-600 text-center mb-1 font-bold">{day.count}</div>
                             <motion.div 
                               initial={{ height: 0 }}
                               animate={{ height: `${Math.min(100, (day.count / (stats?.total || 1)) * 1000)}%` }}
                               className="bg-blue-100 group-hover:bg-blue-200 border-t border-blue-300 rounded-t-sm transition-all"
                             />
                          </div>
                        ))}
                        {(!timeline || timeline.length === 0) && Array.from({ length: 30 }).map((_, i) => (
                          <div key={i} className="flex-1 bg-slate-100 rounded-t-sm h-4" />
                        ))}
                      </div>
                      <div className="flex justify-between mt-4 text-[10px] font-bold text-slate-400 tracking-wider uppercase">
                         <span>30 Days Ago</span>
                         <span>Today</span>
                      </div>
                   </StandardCard>

                   <div className="grid grid-cols-2 gap-8">
                      <StandardCard title="Cluster Distribution" icon={Layers}>
                         <div className="h-48 flex items-center justify-center relative">
                            <div className="text-center z-10">
                               <span className="block text-3xl font-bold text-slate-900">{stats?.clusters || 0}</span>
                               <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">CLUSTERS</span>
                            </div>
                         </div>
                         <div className="mt-4 space-y-2">
                            {(categories || []).slice(0, 4).map((cl: any, idx: number) => (
                              <div key={cl.name} className="flex items-center justify-between">
                                 <div className="flex items-center gap-2">
                                    <div className={`w-2 h-2 rounded-full ${['bg-blue-500', 'bg-purple-500', 'bg-emerald-500', 'bg-amber-500'][idx % 4]}`}></div>
                                    <span className="text-[10px] font-bold text-slate-600 uppercase tracking-wide truncate max-w-[120px]">{cl.name}</span>
                                 </div>
                                 <span className="text-xs font-bold text-slate-900">{cl.value}</span>
                              </div>
                            ))}
                         </div>
                      </StandardCard>

                      <StandardCard title="Knowledge Network" icon={Sparkles}>
                         <div className="h-48 bg-slate-50 rounded-lg border border-slate-100 flex items-center justify-center">
                            <div className="text-center p-6">
                               <Sparkles size={32} className="text-slate-200 mx-auto mb-3" />
                               <p className="text-[10px] text-slate-400 font-bold uppercase tracking-wider leading-relaxed">
                                  Vector Space Projection Available in Full View
                               </p>
                            </div>
                         </div>
                      </StandardCard>
                   </div>
                </div>

                <div className="col-span-4 space-y-8">
                   <StandardCard title="Trending Tags" icon={TagIcon}>
                      <TagCloud bookmarks={bookmarksData?.bookmarks || []} />
                   </StandardCard>

                   <StandardCard title="System Metrics" icon={Shield}>
                      <div className="space-y-4">
                         {(battleCards || []).map(card => (
                           <div key={card.t} className="p-3 bg-slate-50 border border-slate-100 rounded-lg">
                              <div className="flex items-center justify-between mb-2">
                                 <span className="text-[10px] font-bold text-slate-600 tracking-wide uppercase">{card.t}</span>
                                 <span className="text-xs font-bold text-blue-600">{card.v}</span>
                              </div>
                              <div className="h-1.5 w-full bg-slate-200 rounded-full overflow-hidden">
                                 <div className="h-full bg-blue-500" style={{ width: card.v }}></div>
                              </div>
                           </div>
                         ))}
                      </div>
                   </StandardCard>
                </div>
             </motion.div>
           )}

           {view === 'control' && (
             <motion.div 
               key="control"
               initial={{ opacity: 0, y: 10 }}
               animate={{ opacity: 1, y: 0 }}
               exit={{ opacity: 0, y: -10 }}
               className="flex-1 max-w-5xl mx-auto w-full"
             >
                <div className="grid grid-cols-2 gap-8">
                   <StandardCard title="Maintenance" icon={Cpu}>
                      <div className="space-y-4">
                         <div className="p-4 bg-slate-50 border border-slate-200 rounded-lg flex items-center justify-between">
                            <div>
                               <span className="block text-xs font-bold text-slate-900 uppercase">Stabilize Database</span>
                               <span className="text-[10px] font-medium text-slate-400 uppercase">Vacuum & Reindex</span>
                            </div>
                            <button className="px-4 py-1.5 bg-white border border-slate-200 text-slate-700 rounded-md text-xs font-bold hover:bg-slate-100 transition-all">
                               Run
                            </button>
                         </div>

                         <div className="p-4 bg-slate-50 border border-slate-200 rounded-lg flex items-center justify-between">
                            <div>
                               <span className="block text-xs font-bold text-slate-900 uppercase">Sync Core</span>
                               <span className="text-[10px] font-medium text-slate-400 uppercase">Pull Latest</span>
                            </div>
                            <button className="px-4 py-1.5 bg-white border border-slate-200 text-slate-700 rounded-md text-xs font-bold hover:bg-slate-100 transition-all">
                               Sync
                            </button>
                         </div>

                         <div className="p-4 bg-slate-50 border border-slate-200 rounded-lg flex items-center justify-between">
                            <div>
                               <span className="block text-xs font-bold text-slate-900 uppercase">Flush Cache</span>
                               <span className="text-[10px] font-medium text-slate-400 uppercase">Clear Buffer</span>
                            </div>
                            <button className="px-4 py-1.5 bg-white border border-slate-200 text-rose-600 rounded-md text-xs font-bold hover:bg-rose-50 hover:border-rose-200 transition-all">
                               Flush
                            </button>
                         </div>
                      </div>
                   </StandardCard>

                   <StandardCard title="Research Parameters" icon={Sparkles}>
                      <div className="grid grid-cols-1 gap-3">
                         {[
                           { n: 'Deep Scan', d: 'Metadata & LLM Analysis', i: Search, a: true },
                           { n: 'Rapid Index', d: 'URL-only processing', i: Zap, a: false },
                           { n: 'Auto-Link', d: 'Knowledge graph mapping', i: Link, a: false }
                         ].map(mode => (
                           <div key={mode.n} className={`p-4 border rounded-lg transition-all cursor-pointer ${mode.a ? 'bg-blue-50 border-blue-200' : 'bg-slate-50 border-slate-200 hover:border-slate-300'}`}>
                              <div className="flex items-center justify-between mb-1">
                                 <div className="flex items-center gap-3">
                                    <div className={`p-2 rounded-md ${mode.a ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-500'}`}>
                                       <mode.i size={16} />
                                    </div>
                                    <span className={`text-xs font-bold uppercase ${mode.a ? 'text-blue-700' : 'text-slate-700'}`}>{mode.n}</span>
                                 </div>
                                 <div className={`w-8 h-4 rounded-full p-0.5 transition-colors ${mode.a ? 'bg-blue-600' : 'bg-slate-300'}`}>
                                    <div className={`w-3 h-3 bg-white rounded-full transition-transform ${mode.a ? 'translate-x-4' : 'translate-x-0'}`}></div>
                                 </div>
                              </div>
                              <p className="text-[10px] font-medium text-slate-500 uppercase ml-11">
                                 {mode.d}
                              </p>
                           </div>
                         ))}
                      </div>
                   </StandardCard>
                </div>

                <div className="mt-8">
                   <StandardCard title="System Logs" icon={Terminal}>
                      <div className="bg-slate-900 rounded-lg p-4 font-mono text-[11px] text-slate-300 space-y-1.5 max-h-64 overflow-y-auto">
                         {(systemLogs || []).map((log, idx) => (
                           <div key={idx} className="border-l border-slate-700 pl-3">{log}</div>
                         ))}
                         <div className="text-blue-400 animate-pulse">Ready for incoming packets...</div>
                      </div>
                   </StandardCard>
                </div>
             </motion.div>
           )}

         </AnimatePresence>
      </main>

      {/* Footer */}
      <footer className="h-10 border-t border-slate-200 bg-white px-8 flex items-center justify-between text-[10px] font-bold text-slate-400 uppercase tracking-wider shadow-sm">
         <div className="flex gap-8">
            <span className="flex items-center gap-2">Storage: <span className="text-slate-600">1.4GB / 5.0GB</span></span>
            <span className="flex items-center gap-2">Status: <span className="text-emerald-600">Stable</span></span>
         </div>
         <div className="flex gap-6 italic">
            <span>v2.0.4</span>
            <span>BobbyIntel Core</span>
         </div>
      </footer>
    </div>
  );
}

export default App;
