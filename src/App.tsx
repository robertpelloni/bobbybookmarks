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

// --- Cyber Intelligence UI Kit ---

const Scanline = () => (
  <div className="fixed inset-0 pointer-events-none z-[200] opacity-[0.03] overflow-hidden">
    <div className="absolute inset-0 bg-[linear-gradient(rgba(18,16,16,0)_50%,rgba(0,0,0,0.25)_50%),linear-gradient(90deg,rgba(255,0,0,0.06),rgba(0,255,0,0.02),rgba(0,0,255,0.06))] bg-[length:100%_2px,3px_100%]"></div>
    <motion.div 
      animate={{ y: ['-100%', '100%'] }}
      transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
      className="absolute inset-0 w-full h-[100px] bg-gradient-to-b from-transparent via-blue-500/10 to-transparent"
    />
  </div>
);

const NeonCard = ({ children, title, icon: Icon, className = "", onClick }: any) => (
  <motion.div 
    initial={{ opacity: 0, scale: 0.98 }}
    animate={{ opacity: 1, scale: 1 }}
    className={`relative group ${className}`}
    onClick={onClick}
  >
    <div className="absolute -inset-[1px] bg-gradient-to-br from-blue-500/20 via-purple-500/10 to-blue-500/20 rounded-2xl blur-[2px] group-hover:blur-[6px] transition-all duration-500 opacity-50 group-hover:opacity-100"></div>
    <div className="relative bg-[#020617]/90 backdrop-blur-3xl border border-white/5 rounded-2xl overflow-hidden h-full flex flex-col">
      {title && (
        <div className="px-5 py-3 border-b border-white/5 flex items-center justify-between bg-white/[0.02]">
           <div className="flex items-center gap-3">
              {Icon && <div className="p-1.5 rounded-lg bg-blue-500/10 text-blue-400 border border-blue-500/20"><Icon size={14} /></div>}
              <h3 className="text-[10px] font-black text-blue-100 tracking-[0.25em] uppercase italic">{title}</h3>
           </div>
           <div className="flex gap-1.5">
             <div className="w-1 h-1 bg-blue-500/40 rounded-full animate-pulse"></div>
             <div className="w-4 h-1 bg-white/10 rounded-full overflow-hidden">
                <motion.div animate={{ x: [-16, 16] }} transition={{ repeat: Infinity, duration: 1.5 }} className="h-full w-full bg-blue-500/60" />
             </div>
           </div>
        </div>
      )}
      <div className="p-5 flex-1 relative">
        {children}
      </div>
      <div className="absolute bottom-0 right-0 p-1 opacity-20 pointer-events-none">
         <div className="w-4 h-4 border-r-2 border-b-2 border-blue-500/40 rounded-br-sm"></div>
      </div>
    </div>
  </motion.div>
);

const IntelStat = ({ label, value, color = "blue" }: any) => (
  <div className="space-y-1">
    <div className="flex items-center justify-between px-1">
      <span className="text-[9px] font-black text-slate-500 tracking-widest uppercase">{label}</span>
      <span className={`text-[10px] font-black text-${color}-400 uppercase tracking-tighter`}>{value || 0}</span>
    </div>
    <div className="h-1 w-full bg-white/5 rounded-full overflow-hidden">
       <motion.div 
         initial={{ width: 0 }}
         animate={{ width: '70%' }}
         className={`h-full bg-${color}-500/60`}
       />
    </div>
  </div>
);

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
        <motion.span 
          key={tag}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          whileHover={{ scale: 1.1, color: '#3b82f6' }}
          className="px-2 py-1 rounded bg-white/5 border border-white/5 text-[8px] font-black tracking-widest text-slate-500 cursor-pointer transition-colors"
        >
          {tag} <span className="text-blue-500/40 ml-1">{count}</span>
        </motion.span>
      ))}
    </div>
  );
};

// --- D3 FORCE GRAPH COMPONENT ---

const ForceGraph = ({ bookmarks = [] }: { bookmarks: Bookmark[] }) => {
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

    const nodes: any[] = bookmarks.length > 0 ? bookmarks.slice(0, 100).map(b => ({ id: b.id, name: b.page_title || b.url, group: b.is_duplicate ? 'duplicate' : 'node' })) : [
      { id: 'root', name: 'CORE_INTELLIGENCE', group: 'root' },
      ...Array.from({ length: 12 }).map((_, i) => ({ id: i, name: `CLUSTER_${i}`, group: 'cluster' }))
    ];

    const links: any[] = bookmarks.length > 0 ? [] : nodes.slice(1).map(n => ({ source: 'root', target: n.id }));

    if (bookmarks.length > 0) {
      const domains: Record<string, string[]> = {};
      nodes.forEach((n: any) => {
        try {
          const urlStr = n.name.startsWith('http') ? n.name : `https://${n.name}`;
          const url = new URL(urlStr);
          const domain = url.hostname.replace('www.', '');
          if (!domains[domain]) domains[domain] = [];
          domains[domain].push(n.id);
        } catch(e) {}
      });

      Object.entries(domains).forEach(([domain, ids]) => {
        const rootId = `domain-${domain}`;
        nodes.push({ id: rootId, name: domain.toUpperCase(), group: 'domain' } as any);
        ids.forEach(id => links.push({ source: rootId, target: id } as any));
      });
    }

    const simulation = d3.forceSimulation(nodes as any)
      .force("link", d3.forceLink(links).id((d: any) => d.id).distance((d: any) => d.target.group === 'domain' ? 150 : 80))
      .force("charge", d3.forceManyBody().strength((d: any) => d.group === 'domain' ? -500 : -100))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("collision", d3.forceCollide().radius(20));

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
      .attr("r", (d: any) => d.group === 'root' ? 12 : d.group === 'domain' ? 8 : 4)
      .attr("fill", (d: any) => d.group === 'root' ? "#3b82f6" : d.group === 'domain' ? "#8b5cf6" : d.group === 'duplicate' ? "#f59e0b" : "#34d399")
      .attr("filter", "url(#glow)")
      .attr("stroke", "#020617")
      .attr("stroke-width", 2);

    node.append("text")
      .text((d: any) => d.name)
      .attr("x", 12)
      .attr("y", 4)
      .attr("fill", (d: any) => d.group === 'domain' ? "#8b5cf6" : "#64748b")
      .attr("font-size", (d: any) => d.group === 'domain' ? "10px" : "7px")
      .attr("font-weight", "900")
      .attr("class", "uppercase tracking-tighter pointer-events-none select-none");

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

  }, [bookmarks]);

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
    queryFn: () => axios.get('/api/stats').then(res => res.data),
    refetchInterval: 10000,
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

  const { data: recentActivity } = useQuery<Bookmark[]>({
    queryKey: ['recentActivity'],
    queryFn: () => axios.get('/api/bookmarks', { params: { limit: 50, sort: 'created_at', order: 'desc' } }).then(res => res.data.bookmarks),
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
    <div className="min-h-screen bg-[#01040a] text-slate-400 font-sans selection:bg-blue-500/30 overflow-hidden flex flex-col">
      <Scanline />

      {/* Top HUD */}
      <header className="h-16 border-b border-white/5 bg-[#01040a]/90 backdrop-blur-3xl z-[150] px-8 flex items-center justify-between">
         <div className="flex items-center gap-10">
            <div className="flex items-center gap-4 group cursor-pointer" onClick={() => setView('intel')}>
               <div className="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center shadow-[0_0_30px_rgba(37,99,235,0.4)] group-hover:scale-110 transition-transform">
                  <Zap size={22} className="text-white fill-white" />
               </div>
               <div>
                  <h1 className="text-lg font-black tracking-[0.2em] text-white italic">BOBBY<span className="text-blue-500">INTEL</span></h1>
                  <span className="text-[8px] font-black text-blue-500/60 tracking-widest uppercase">OS_V2.04_KINETIC</span>
               </div>
            </div>

            <nav className="flex items-center gap-1 px-1.5 py-1 bg-white/[0.03] rounded-xl border border-white/5">
              {[
                { id: 'intel', label: 'INTELLIGENCE', icon: Activity },
                { id: 'activity', label: 'ACTIVITY_LOG', icon: Radio },
                { id: 'analytics', label: 'ANALYTICS', icon: Sparkles },
                { id: 'control', label: 'CONTROL', icon: Gauge },
                { id: 'ingest', label: 'INGESTION', icon: Share2 },
                { id: 'catalog', label: 'CATALOG', icon: Box },
                { id: 'terminal', label: 'TERMINAL', icon: Terminal }
              ].map((m) => (
                <button 
                  key={m.id}
                  onClick={() => setView(m.id as any)}
                  className={`flex items-center gap-2.5 px-6 py-2 rounded-lg text-[9px] font-black tracking-widest transition-all duration-300 ${
                    view === m.id ? 'bg-blue-600 text-white shadow-lg' : 'text-slate-500 hover:text-white hover:bg-white/5'
                  }`}
                >
                  <m.icon size={13} /> {m.label}
                </button>
              ))}
            </nav>
         </div>

         <div className="flex items-center gap-8">
            <div className="flex items-center gap-4 text-right">
               <div>
                  <span className="block text-[8px] font-black text-slate-600 tracking-widest uppercase">LATENCY</span>
                  <span className="text-[10px] font-black text-green-500 tracking-tighter uppercase">12MS / NOMINAL</span>
               </div>
               <div className="h-8 w-px bg-white/5"></div>
               <div>
                  <span className="block text-[8px] font-black text-slate-600 tracking-widest uppercase">SECURITY</span>
                  <span className="text-[10px] font-black text-blue-400 tracking-tighter uppercase">ENCRYPTED</span>
               </div>
            </div>
            <div className="relative w-72">
               <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-600" size={14} />
               <input 
                 type="text" 
                 placeholder="GLOBAL_SCAN..."
                 value={searchTerm}
                 onChange={(e) => setSearchTerm(e.target.value)}
                 className="w-full bg-white/[0.03] border border-white/5 rounded-xl pl-11 pr-4 py-2.5 text-[10px] font-black tracking-widest text-white focus:outline-none focus:border-blue-500/40 transition-all uppercase placeholder:text-slate-700"
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
               initial={{ opacity: 0, x: 20 }}
               animate={{ opacity: 1, x: 0 }}
               exit={{ opacity: 0, x: -20 }}
               className="flex-1 grid grid-cols-12 gap-8"
             >
                {/* Left Column - Stats */}
                <div className="col-span-3 space-y-8">
                   <NeonCard title="SYSTEM_OVERVIEW" icon={Gauge}>
                      <div className="space-y-6">
                         <IntelStat label="TOTAL_ENTROPY" value={stats?.total} color="blue" />
                         <IntelStat label="ACTIVE_CLUSTERS" value={stats?.clusters} color="purple" />
                         <IntelStat label="PROCESSED_NODES" value={workerStatus?.done} color="green" />
                         <IntelStat label="DUPLICATE_SIG" value={stats?.duplicates} color="yellow" />
                      </div>
                      
                      <div className="mt-8 pt-8 border-t border-white/5 space-y-3">
                         <button 
                           onClick={() => axios.post('/api/research/start')}
                           className="w-full py-2 bg-green-500/10 border border-green-500/20 text-green-500 rounded-lg text-[8px] font-black tracking-widest uppercase hover:bg-green-500/20 transition-all"
                         >
                           {workerStatus?.running ? 'ENGINE_ONLINE' : 'INITIATE_RESEARCH'}
                         </button>
                         <button 
                           onClick={() => axios.post('/api/research/stop')}
                           className="w-full py-2 bg-red-500/10 border border-red-500/20 text-red-500 rounded-lg text-[8px] font-black tracking-widest uppercase hover:bg-red-500/20 transition-all"
                         >
                           SUSPEND_OPERATIONS
                         </button>
                         <button 
                           onClick={() => axios.post('/api/bookmarks/deduplicate')}
                           className="w-full py-2 bg-yellow-500/10 border border-yellow-500/20 text-yellow-500 rounded-lg text-[8px] font-black tracking-widest uppercase hover:bg-yellow-500/20 transition-all"
                         >
                           PURGE_DUPLICATES
                         </button>
                      </div>
                   </NeonCard>

                   <NeonCard title="CORE_STATUS" icon={Cpu}>
                      <div className="flex items-center justify-between mb-4">
                         <span className="text-[9px] font-black text-slate-500 tracking-widest uppercase">ENGINE_LOAD</span>
                         <span className="text-[10px] font-black text-blue-400">14.2%</span>
                      </div>
                      <div className="h-20 flex items-end gap-1 px-1">
                         {Array.from({ length: 15 }).map((_, i) => (
                           <motion.div 
                             key={i}
                             animate={{ height: [10, Math.random() * 40 + 10, 10] }}
                             transition={{ repeat: Infinity, duration: 1 + Math.random(), ease: "easeInOut" }}
                             className="flex-1 bg-blue-500/20 rounded-t-sm"
                           />
                         ))}
                      </div>
                   </NeonCard>
                </div>

                {/* Center Column - Visual Map */}
                <div className="col-span-6 flex flex-col gap-8">
                   <NeonCard title="TOPOLOGICAL_MAP" icon={Globe} className="flex-1 min-h-[500px]">
                      <div className="absolute inset-0 z-0 opacity-20 bg-[radial-gradient(#1e293b_1px,transparent_1px)] bg-[size:20px_20px]"></div>
                      <ForceGraph bookmarks={bookmarksData?.bookmarks || []} />
                   </NeonCard>
                   
                   <NeonCard title="COGNITIVE_CLOUD" icon={TagIcon}>
                      <TagCloud bookmarks={bookmarksData?.bookmarks || []} />
                   </NeonCard>
                </div>

                {/* Right Column - Logs */}
                <div className="col-span-3 flex flex-col h-full">
                   <NeonCard title="REALTIME_STREAM" icon={Activity} className="h-full">
                      <div className="space-y-4 font-mono">
                         {(recentActivity || []).slice(0, 10).map((log, i) => (
                           <div key={log.id} className="flex gap-4 border-l border-white/5 pl-4 py-1 group cursor-default">
                              <span className="text-[9px] text-slate-700 font-bold">{new Date(log.created_at || Date.now()).toLocaleTimeString()}</span>
                              <span className={`text-[9px] font-black ${log.research_status === 'done' ? 'text-green-500/80' : 'text-blue-500/80'} tracking-tighter uppercase group-hover:text-white transition-colors truncate`}>
                                {log.research_status === 'done' ? 'STABLE' : 'PENDING'}: {log.page_title || log.url}
                              </span>
                           </div>
                         ))}
                         {(!recentActivity || recentActivity.length === 0) && (
                           <div className="text-[9px] font-black text-slate-700 uppercase tracking-widest text-center mt-20 italic">AWAITING_DATA_STREAM...</div>
                         )}
                      </div>
                   </NeonCard>
                </div>
             </motion.div>
           )}

           {view === 'ingest' && (
             <motion.div 
               key="ingest"
               initial={{ opacity: 0, scale: 0.95 }}
               animate={{ opacity: 1, scale: 1 }}
               exit={{ opacity: 0, scale: 1.05 }}
               className="flex-1 flex flex-col max-w-5xl mx-auto gap-8"
             >
                <div className="grid grid-cols-3 gap-8">
                   <NeonCard className="cursor-pointer group" onClick={() => window.location.href = '/api/database/download'}>
                      <div className="flex flex-col items-center gap-6 py-4">
                         <div className="w-16 h-16 rounded-2xl bg-purple-500/10 flex items-center justify-center text-purple-500 border border-purple-500/20 group-hover:bg-purple-500 group-hover:text-white transition-all shadow-xl">
                            <Database size={28} />
                         </div>
                         <div className="text-center">
                            <span className="block text-[11px] font-black text-white tracking-[0.2em] mb-1">EXPORT_DB</span>
                            <span className="text-[9px] font-bold text-slate-500 tracking-widest uppercase">DOWNLOAD_BACKUP</span>
                         </div>
                      </div>
                   </NeonCard>
                   <NeonCard className="cursor-pointer group">
                      <div className="flex flex-col items-center gap-6 py-4">
                         <div className="w-16 h-16 rounded-2xl bg-blue-500/10 flex items-center justify-center text-blue-500 border border-blue-500/20 group-hover:bg-blue-500 group-hover:text-white transition-all shadow-xl">
                            <Upload size={28} />
                         </div>
                         <div className="text-center">
                            <span className="block text-[11px] font-black text-white tracking-[0.2em] mb-1">IMPORT_DATA</span>
                            <span className="text-[9px] font-bold text-slate-500 tracking-widest uppercase">UPLOAD_RESOURCES</span>
                         </div>
                      </div>
                   </NeonCard>
                   <NeonCard className="cursor-pointer group">
                      <div className="flex flex-col items-center gap-6 py-4">
                         <div className="w-16 h-16 rounded-2xl bg-yellow-500/10 flex items-center justify-center text-yellow-500 border border-yellow-500/20 group-hover:bg-yellow-500 group-hover:text-white transition-all shadow-xl">
                            <Radio size={28} />
                         </div>
                         <div className="text-center">
                            <span className="block text-[11px] font-black text-white tracking-[0.2em] mb-1">RAW_STREAM</span>
                            <span className="text-[9px] font-bold text-slate-500 tracking-widest uppercase">TEXT_INJECTION</span>
                         </div>
                      </div>
                   </NeonCard>
                </div>

                <NeonCard title="RESOURCE_ASSIMILATION_TERMINAL" icon={Terminal} className="flex-1">
                   <textarea 
                     value={ingestText}
                     onChange={(e) => setIngestText(e.target.value)}
                     className="w-full h-full bg-transparent border-none focus:outline-none font-mono text-[11px] text-green-400 placeholder:text-slate-800 leading-relaxed uppercase tracking-tighter resize-none"
                     placeholder="AWAITING_INPUT_STREAM_PACKETS..."
                   />
                   <div className="absolute bottom-10 right-10 flex gap-4">
                      <button 
                        onClick={() => {
                          if (ingestText.trim()) {
                            assimilateMutation.mutate(ingestText);
                            setIngestText('');
                          }
                        }}
                        disabled={assimilateMutation.isPending}
                        className="px-12 py-4 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-xl font-black text-[10px] tracking-[0.3em] uppercase transition-all shadow-[0_0_30px_rgba(37,99,235,0.3)] flex items-center gap-4 active:scale-95"
                      >
                         <Zap size={18} className={assimilateMutation.isPending ? 'animate-spin' : ''} /> 
                         {assimilateMutation.isPending ? 'ASSIMILATING...' : 'INITIATE_TRANSFER'}
                      </button>
                   </div>
                </NeonCard>
             </motion.div>
           )}

           {view === 'catalog' && (
             <motion.div 
               key="catalog"
               initial={{ opacity: 0, scale: 0.95 }}
               animate={{ opacity: 1, scale: 1 }}
               exit={{ opacity: 0, scale: 1.05 }}
               className="flex-1 flex flex-col gap-8 overflow-y-auto max-h-[80vh] pr-4 custom-scrollbar"
             >
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 pb-20">
                  {(bookmarksData?.bookmarks || []).map((bm: Bookmark) => (
                    <NeonCard key={bm.id} title={bm.is_duplicate ? "DUPLICATE_SIG" : "KNOWLEDGE_NODE"} icon={bm.is_duplicate ? Shield : Box} className="h-fit">
                      <div className="space-y-4">
                        <h4 className="text-[10px] font-black text-white leading-tight uppercase tracking-[0.1em] line-clamp-2">{bm.page_title || bm.url}</h4>
                        <p className="text-[9px] text-slate-500 font-bold leading-relaxed line-clamp-3 italic uppercase tracking-tighter">{bm.page_description || 'NO_METADATA_EXTRACTED_YET'}</p>
                        <div className="flex items-center justify-between pt-2 border-t border-white/5">
                          <span className={`text-[8px] font-black px-2 py-0.5 rounded border ${bm.research_status === 'done' ? 'bg-green-500/10 text-green-500 border-green-500/20' : 'bg-blue-500/10 text-blue-500 border-blue-500/20'} uppercase tracking-widest`}>
                            {bm.research_status}
                          </span>
                          <div className="flex gap-3">
                             <a href={bm.url} target="_blank" rel="noreferrer" className="text-slate-500 hover:text-blue-400 transition-colors">
                                <Globe size={14} />
                             </a>
                             <button className="text-slate-500 hover:text-white transition-colors">
                                <ArrowRight size={14} />
                             </button>
                          </div>
                        </div>
                      </div>
                    </NeonCard>
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
                  {(recentActivity || []).map((log) => (
                    <div key={log.id} className="flex items-center gap-6 p-4 bg-white/[0.02] border border-white/5 rounded-xl hover:bg-white/[0.05] transition-all group">
                       <div className={`p-2 rounded-lg ${log.research_status === 'done' ? 'bg-green-500/10 text-green-400' : 'bg-blue-500/10 text-blue-400'} border border-white/5`}>
                          <Fingerprint size={16} />
                       </div>
                       <div className="flex-1">
                          <div className="flex items-center justify-between mb-1">
                             <span className="text-[10px] font-black text-white tracking-widest uppercase truncate max-w-xl">{log.page_title || log.url}</span>
                             <span className="text-[8px] font-black text-slate-600 uppercase tracking-widest">{new Date(log.created_at || Date.now()).toLocaleString()}</span>
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
               initial={{ opacity: 0, y: 20 }}
               animate={{ opacity: 1, y: 0 }}
               exit={{ opacity: 0, y: -20 }}
               className="flex-1 grid grid-cols-12 gap-8 overflow-y-auto max-h-[80vh] pr-4 custom-scrollbar"
             >
                <div className="col-span-8 space-y-8">
                   <NeonCard title="HARVEST_VELOCITY" icon={Activity}>
                      <div className="h-64 flex items-end gap-2 px-2">
                        {Array.from({ length: 30 }).map((_, i) => (
                          <div key={i} className="flex-1 flex flex-col justify-end gap-1 group">
                             <div className="opacity-0 group-hover:opacity-100 transition-opacity text-[7px] text-blue-400 text-center mb-1">{Math.floor(Math.random() * 100)}</div>
                             <motion.div 
                               initial={{ height: 0 }}
                               animate={{ height: `${Math.random() * 80 + 10}%` }}
                               className="bg-blue-500/20 group-hover:bg-blue-500/40 border-t border-blue-500/50 rounded-t-sm transition-all"
                             />
                          </div>
                        ))}
                      </div>
                      <div className="flex justify-between mt-4 text-[7px] font-black text-slate-700 tracking-[0.2em] uppercase">
                         <span>T-30_DAYS</span>
                         <span>CURRENT_STAMP</span>
                      </div>
                   </NeonCard>

                   <div className="grid grid-cols-2 gap-8">
                      <NeonCard title="CLUSTER_DISTRIBUTION" icon={Layers}>
                         <div className="h-48 flex items-center justify-center relative">
                            <div className="absolute inset-0 flex items-center justify-center">
                               <div className="w-32 h-32 rounded-full border-8 border-blue-500/10 border-t-blue-500 animate-[spin_10s_linear_infinite]"></div>
                               <div className="absolute w-24 h-24 rounded-full border-8 border-purple-500/10 border-b-purple-500 animate-[spin_15s_linear_infinite_reverse]"></div>
                            </div>
                            <div className="text-center z-10">
                               <span className="block text-xl font-black text-white">14</span>
                               <span className="text-[8px] font-black text-slate-500 uppercase tracking-widest">CLUSTERS</span>
                            </div>
                         </div>
                         <div className="mt-4 space-y-2">
                            {[
                              { n: 'DEVELOPMENT', v: '34%', c: 'bg-blue-500' },
                              { n: 'RESEARCH', v: '28%', c: 'bg-purple-500' },
                              { n: 'SYSTEMS', v: '21%', c: 'bg-green-500' },
                              { n: 'OTHER', v: '17%', c: 'bg-slate-500' }
                            ].map(cl => (
                              <div key={cl.n} className="flex items-center justify-between">
                                 <div className="flex items-center gap-2">
                                    <div className={`w-1.5 h-1.5 rounded-full ${cl.c}`}></div>
                                    <span className="text-[8px] font-black text-slate-400 uppercase tracking-widest">{cl.n}</span>
                                 </div>
                                 <span className="text-[9px] font-black text-white">{cl.v}</span>
                              </div>
                            ))}
                         </div>
                      </NeonCard>

                      <NeonCard title="KNOWLEDGE_NEBULA" icon={Sparkles}>
                         <div className="h-48 bg-white/[0.02] rounded-xl border border-white/5 relative overflow-hidden group">
                            <div className="absolute inset-0 opacity-40 bg-[radial-gradient(#3b82f6_1px,transparent_1px)] bg-[size:15px_15px] animate-pulse"></div>
                            {Array.from({ length: 20 }).map((_, i) => (
                              <motion.div 
                                key={i}
                                animate={{ 
                                  x: [Math.random() * 200, Math.random() * 200],
                                  y: [Math.random() * 150, Math.random() * 150],
                                  opacity: [0.2, 0.8, 0.2]
                                }}
                                transition={{ duration: 5 + Math.random() * 5, repeat: Infinity }}
                                className="absolute w-1 h-1 bg-blue-400 rounded-full blur-[1px]"
                              />
                            ))}
                            <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-[#020617]/80 backdrop-blur-sm">
                               <button className="px-6 py-2 bg-blue-600 text-white rounded-lg text-[9px] font-black tracking-widest uppercase shadow-xl">
                                  OPEN_PROJECTION
                               </button>
                            </div>
                         </div>
                         <p className="mt-4 text-[8px] text-slate-500 font-bold uppercase tracking-widest leading-relaxed">
                            HIGH-DIMENSIONAL_VECTOR_SPACE_PROJECTION_OF_CORE_KNOWLEDGE_ASSETS.
                         </p>
                      </NeonCard>
                   </div>
                </div>

                <div className="col-span-4 space-y-8">
                   <NeonCard title="TRENDING_SIGS" icon={TagIcon}>
                      <div className="flex flex-wrap gap-2">
                         {['AI', 'REACT', 'GO', 'SQLITE', 'DOCKER', 'TAILWIND', 'VITE', 'RENDER', 'D3', 'FIBER', 'TYPESCRIPT', 'PYTHON', 'ML', 'LLM', 'AGENT'].map(t => (
                           <span key={t} className="px-2 py-1 bg-white/5 border border-white/5 rounded text-[8px] font-black text-slate-500 hover:text-blue-400 hover:border-blue-500/30 transition-all cursor-pointer uppercase tracking-widest">
                              {t}
                           </span>
                         ))}
                      </div>
                   </NeonCard>

                   <NeonCard title="BATTLE_CARDS" icon={Shield}>
                      <div className="space-y-4">
                         {[
                           { t: 'ARCHITECTURE_STABILITY', v: '98.2%', s: 'bg-green-500' },
                           { t: 'INGESTION_EFFICIENCY', v: '84.5%', s: 'bg-blue-500' },
                           { t: 'DEDUPLICATION_ACCURACY', v: '92.1%', s: 'bg-purple-500' }
                         ].map(card => (
                           <div key={card.t} className="p-3 bg-white/[0.03] border border-white/5 rounded-xl">
                              <div className="flex items-center justify-between mb-2">
                                 <span className="text-[8px] font-black text-white tracking-widest uppercase">{card.t}</span>
                                 <span className="text-[10px] font-black text-blue-400">{card.v}</span>
                              </div>
                              <div className="h-1 w-full bg-white/5 rounded-full overflow-hidden">
                                 <div className={`h-full ${card.s}/60`} style={{ width: card.v }}></div>
                              </div>
                           </div>
                         ))}
                      </div>
                   </NeonCard>
                </div>
             </motion.div>
           )}

           {view === 'control' && (
             <motion.div 
               key="control"
               initial={{ opacity: 0, scale: 0.95 }}
               animate={{ opacity: 1, scale: 1 }}
               exit={{ opacity: 0, scale: 1.05 }}
               className="flex-1 max-w-5xl mx-auto w-full"
             >
                <div className="grid grid-cols-2 gap-8">
                   <NeonCard title="ENGINE_MAINTENANCE" icon={Cpu}>
                      <div className="space-y-6">
                         <div className="p-4 bg-white/[0.03] border border-white/5 rounded-xl flex items-center justify-between group">
                            <div>
                               <span className="block text-[10px] font-black text-white tracking-widest uppercase">STABILIZE_DATABASE</span>
                               <span className="text-[8px] font-bold text-slate-500 uppercase tracking-tighter">VACUUM_&_REINDEX_CORE_TABLES</span>
                            </div>
                            <button className="px-6 py-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 rounded-lg text-[8px] font-black tracking-widest uppercase hover:bg-blue-500 hover:text-white transition-all">
                               INITIATE
                            </button>
                         </div>

                         <div className="p-4 bg-white/[0.03] border border-white/5 rounded-xl flex items-center justify-between group">
                            <div>
                               <span className="block text-[10px] font-black text-white tracking-widest uppercase">SYNC_CORE_DB</span>
                               <span className="text-[8px] font-bold text-slate-500 uppercase tracking-tighter">PULL_LATEST_FROM_REMOTE_MIRROR</span>
                            </div>
                            <button className="px-6 py-2 bg-purple-500/10 border border-purple-500/20 text-purple-400 rounded-lg text-[8px] font-black tracking-widest uppercase hover:bg-purple-500 hover:text-white transition-all">
                               SYNC_NOW
                            </button>
                         </div>

                         <div className="p-4 bg-white/[0.03] border border-white/5 rounded-xl flex items-center justify-between group">
                            <div>
                               <span className="block text-[10px] font-black text-white tracking-widest uppercase">FLUSH_CACHE</span>
                               <span className="text-[8px] font-bold text-slate-500 uppercase tracking-tighter">CLEAR_EPHEMERAL_BUFFER_NODES</span>
                            </div>
                            <button className="px-6 py-2 bg-red-500/10 border border-red-500/20 text-red-400 rounded-lg text-[8px] font-black tracking-widest uppercase hover:bg-red-500 hover:text-white transition-all">
                               PURGE
                            </button>
                         </div>
                      </div>
                   </NeonCard>

                   <NeonCard title="RESEARCH_MODES" icon={Sparkles}>
                      <div className="grid grid-cols-1 gap-4">
                         {[
                           { n: 'DEEP_SCAN', d: 'FULL_METADATA_EXTRACTION_&_LLM_ANALYSIS', i: Search, a: true },
                           { n: 'RAPID_INGEST', d: 'URL_ONLY_INDEXING_FOR_SPEED', i: Zap, a: false },
                           { n: 'INTELLIGENT_LINK', d: 'AUTO-CONNECTING_RELATED_KNOWLEDGE_NODES', i: Link, a: false }
                         ].map(mode => (
                           <div key={mode.n} className={`p-4 border rounded-xl transition-all cursor-pointer ${mode.a ? 'bg-blue-600/10 border-blue-500/40' : 'bg-white/[0.02] border-white/5 hover:border-white/20'}`}>
                              <div className="flex items-center justify-between mb-2">
                                 <div className="flex items-center gap-3">
                                    <div className={`p-2 rounded-lg ${mode.a ? 'bg-blue-500 text-white' : 'bg-white/5 text-slate-500'}`}>
                                       <mode.i size={16} />
                                    </div>
                                    <span className={`text-[10px] font-black tracking-widest uppercase ${mode.a ? 'text-white' : 'text-slate-400'}`}>{mode.n}</span>
                                 </div>
                                 <div className={`w-8 h-4 rounded-full p-0.5 transition-colors ${mode.a ? 'bg-blue-500' : 'bg-slate-800'}`}>
                                    <div className={`w-3 h-3 bg-white rounded-full transition-transform ${mode.a ? 'translate-x-4' : 'translate-x-0'}`}></div>
                                 </div>
                              </div>
                              <p className="text-[8px] font-bold text-slate-500 uppercase tracking-tighter leading-relaxed">
                                 {mode.d}
                              </p>
                           </div>
                         ))}
                      </div>
                   </NeonCard>
                </div>

                <div className="mt-8">
                   <NeonCard title="GLOBAL_SYSTEM_LOGS" icon={Terminal}>
                      <div className="bg-black/40 rounded-xl p-6 font-mono text-[10px] text-green-500/80 space-y-2 max-h-64 overflow-y-auto custom-scrollbar">
                         <div>[SYSTEM] KERNEL_INITIALIZED_AT_{new Date().toISOString()}</div>
                         <div>[DATABASE] CORE_ESTABLISHED_SUCCESSFULLY</div>
                         <div>[WORKER] RESEARCH_ENGINE_ONLINE_IN_DEEP_SCAN_MODE</div>
                         <div>[NETWORK] HANDSHAKE_NOMINAL_WITH_REMOTE_NODES</div>
                         <div className="animate-pulse">[LISTENING] AWAITING_INCOMING_RESOURCE_PACKETS...</div>
                      </div>
                   </NeonCard>
                </div>
             </motion.div>
           )}

         </AnimatePresence>
      </main>

      {/* Footer HUD */}
      <footer className="h-10 border-t border-white/5 bg-[#01040a] px-8 flex items-center justify-between text-[9px] font-black tracking-[0.3em] text-slate-700 uppercase">
         <div className="flex gap-8">
            <span className="flex items-center gap-2"><div className="w-1.5 h-1.5 rounded-full bg-blue-500"></div> STORAGE: 1.4GB / 5.0GB</span>
            <span className="flex items-center gap-2"><div className="w-1.5 h-1.5 rounded-full bg-purple-500"></div> COMPRESSION: 4.2X</span>
         </div>
         <div className="flex gap-6 italic">
            <span className="text-blue-500/50 hover:text-blue-500 cursor-pointer transition-colors">V_2.04</span>
            <span className="text-blue-500/50 hover:text-blue-500 cursor-pointer transition-colors">KERN_ESTABLISHED</span>
         </div>
      </footer>
    </div>
  );
}

export default App;
