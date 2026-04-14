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
  <div className="fixed inset-0 pointer-events-none z-[200] opacity-[0.05] overflow-hidden">
    <div className="absolute inset-0 bg-[linear-gradient(rgba(18,16,16,0)_50%,rgba(0,0,0,0.25)_50%),linear-gradient(90deg,rgba(255,0,0,0.06),rgba(0,255,0,0.02),rgba(0,0,255,0.06))] bg-[length:100%_2px,3px_100%]"></div>
    <motion.div 
      animate={{ y: ['-100%', '100%'] }}
      transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
      className="absolute inset-0 w-full h-[200px] bg-gradient-to-b from-transparent via-cyan-500/10 to-transparent"
    />
  </div>
);

const NeonCard = ({ children, title, icon: Icon, className = "", onClick, color = "blue" }: any) => {
  const colorMap: any = {
    blue: "from-cyan-500/20 via-blue-500/10 to-cyan-500/20 shadow-cyan-500/5",
    purple: "from-purple-500/20 via-fuchsia-500/10 to-purple-500/20 shadow-purple-500/5",
    green: "from-emerald-500/20 via-green-500/10 to-emerald-500/20 shadow-green-500/5",
    red: "from-rose-500/20 via-red-500/10 to-rose-500/20 shadow-red-500/5"
  };

  const accentMap: any = {
    blue: "text-cyan-400 border-cyan-500/30 bg-cyan-500/10",
    purple: "text-fuchsia-400 border-fuchsia-500/30 bg-fuchsia-500/10",
    green: "text-emerald-400 border-emerald-500/30 bg-emerald-500/10",
    red: "text-rose-400 border-rose-500/30 bg-rose-500/10"
  };

  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ y: -2 }}
      className={`relative group ${className}`}
      onClick={onClick}
    >
      <div className={`absolute -inset-[1px] bg-gradient-to-br ${colorMap[color] || colorMap.blue} rounded-xl blur-[1px] group-hover:blur-[3px] transition-all duration-500 opacity-40 group-hover:opacity-80`}></div>
      <div className="relative bg-[#050b18]/80 backdrop-blur-2xl border border-white/5 rounded-xl overflow-hidden h-full flex flex-col shadow-2xl">
        {title && (
          <div className="px-5 py-3 border-b border-white/5 flex items-center justify-between bg-gradient-to-r from-white/[0.03] to-transparent">
             <div className="flex items-center gap-3">
                {Icon && <div className={`p-1.5 rounded border ${accentMap[color] || accentMap.blue}`}><Icon size={12} /></div>}
                <h3 className="text-[9px] font-black text-white tracking-[0.3em] uppercase italic group-hover:text-cyan-400 transition-colors">{title}</h3>
             </div>
             <div className="flex gap-1">
               <div className={`w-1 h-1 rounded-full animate-pulse ${color === 'red' ? 'bg-red-500' : 'bg-cyan-500'}`}></div>
               <div className="w-12 h-[2px] bg-white/5 self-center rounded-full overflow-hidden">
                  <motion.div animate={{ x: [-48, 48] }} transition={{ repeat: Infinity, duration: 2 }} className={`h-full w-full ${color === 'red' ? 'bg-red-500/40' : 'bg-cyan-500/40'}`} />
               </div>
             </div>
          </div>
        )}
        <div className="p-5 flex-1 relative">
          {children}
        </div>
        
        {/* Decorative corner accents */}
        <div className="absolute top-0 left-0 w-2 h-2 border-t border-l border-white/20"></div>
        <div className="absolute top-0 right-0 w-2 h-2 border-t border-r border-white/20"></div>
        <div className="absolute bottom-0 left-0 w-2 h-2 border-b border-l border-white/20"></div>
        <div className="absolute bottom-0 right-0 w-2 h-2 border-b border-r border-white/20"></div>
      </div>
    </motion.div>
  );
};

const IntelStat = ({ label, value, color = "blue", icon: Icon }: any) => {
  const colorMap: any = {
    blue: "text-cyan-400 bg-cyan-500/40 shadow-[0_0_10px_rgba(34,211,238,0.3)]",
    purple: "text-fuchsia-400 bg-fuchsia-500/40 shadow-[0_0_10px_rgba(232,121,249,0.3)]",
    green: "text-emerald-400 bg-emerald-500/40 shadow-[0_0_10px_rgba(52,211,153,0.3)]",
    yellow: "text-amber-400 bg-amber-500/40 shadow-[0_0_10px_rgba(251,191,36,0.3)]",
    red: "text-rose-400 bg-rose-500/40 shadow-[0_0_10px_rgba(244,63,94,0.3)]"
  };

  return (
    <div className="group cursor-default">
      <div className="flex items-center justify-between px-1 mb-1.5">
        <div className="flex items-center gap-2">
           {Icon && <Icon size={10} className="text-slate-500 group-hover:text-white transition-colors" />}
           <span className="text-[8px] font-black text-slate-500 tracking-widest uppercase group-hover:text-slate-300 transition-colors">{label}</span>
        </div>
        <span className={`text-[11px] font-black tracking-tighter ${colorMap[color].split(' ')[0]}`}>{value || 0}</span>
      </div>
      <div className="h-[3px] w-full bg-white/5 rounded-full overflow-hidden">
         <motion.div 
           initial={{ width: 0 }}
           animate={{ width: '85%' }}
           className={`h-full ${colorMap[color].split(' ')[1]} ${colorMap[color].split(' ')[2]}`}
         />
      </div>
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
    <div className="flex flex-wrap gap-2.5">
      {tags.map(([tag, count]) => (
        <motion.span 
          key={tag}
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          whileHover={{ 
            scale: 1.05, 
            backgroundColor: 'rgba(34, 211, 238, 0.15)',
            borderColor: 'rgba(34, 211, 238, 0.4)',
            color: '#22d3ee'
          }}
          className="px-3 py-1.5 rounded-lg bg-[#0a1224] border border-white/5 text-[9px] font-black tracking-[0.15em] text-slate-400 cursor-pointer transition-all duration-300 shadow-sm"
        >
          {tag} <span className="text-cyan-500/50 ml-1.5 font-mono">[{count}]</span>
        </motion.span>
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
      .attr("r", (d: any) => d.group === 'root' ? 14 : d.group === 'cluster' ? 10 : 5)
      .attr("fill", (d: any) => d.group === 'root' ? "#06b6d4" : d.group === 'cluster' ? "#d946ef" : d.group === 'duplicate' ? "#f59e0b" : "#10b981")
      .attr("filter", "url(#glow)")
      .attr("stroke", "#020617")
      .attr("stroke-width", 2.5);

    node.append("text")
      .text((d: any) => d.name)
      .attr("x", 15)
      .attr("y", 5)
      .attr("fill", (d: any) => d.group === 'cluster' ? "#d946ef" : "#94a3b8")
      .attr("font-size", (d: any) => d.group === 'cluster' ? "11px" : "8px")
      .attr("font-weight", "900")
      .attr("class", "uppercase tracking-[0.1em] pointer-events-none select-none italic");

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
    <div className="min-h-screen bg-[#020408] text-slate-400 font-sans selection:bg-cyan-500/30 overflow-hidden flex flex-col">
      <Scanline />

      {/* Top HUD */}
      <header className="h-20 border-b border-white/5 bg-[#020408]/90 backdrop-blur-3xl z-[150] px-8 flex items-center justify-between shadow-[0_10px_40px_rgba(0,0,0,0.5)]">
         <div className="flex items-center gap-12">
            <div className="flex items-center gap-5 group cursor-pointer" onClick={() => setView('intel')}>
               <div className="relative">
                  <div className="absolute -inset-2 bg-cyan-500/20 blur-xl group-hover:bg-cyan-500/40 transition-all rounded-full"></div>
                  <div className="relative w-11 h-11 bg-cyan-600 rounded-lg flex items-center justify-center border border-cyan-400/30 group-hover:scale-105 transition-transform overflow-hidden">
                     <Zap size={24} className="text-white fill-white animate-pulse" />
                     <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/20 to-transparent translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700"></div>
                  </div>
               </div>
               <div>
                  <h1 className="text-xl font-black tracking-[0.3em] text-white italic group-hover:text-cyan-400 transition-colors">BOBBY<span className="text-cyan-500 group-hover:text-white">INTEL</span></h1>
                  <div className="flex items-center gap-2">
                    <span className="text-[8px] font-black text-cyan-500/60 tracking-[0.4em] uppercase">OS_V2.04_KINETIC</span>
                    <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse shadow-[0_0_10px_#22c55e]"></div>
                  </div>
               </div>
            </div>

            <nav className="flex items-center gap-1.5 px-2 py-1.5 bg-white/[0.02] rounded-xl border border-white/5 shadow-inner">
              {[
                { id: 'intel', label: 'INTELLIGENCE', icon: Activity },
                { id: 'activity', label: 'LIVE_FEED', icon: Radio },
                { id: 'analytics', label: 'ANALYTICS', icon: Sparkles },
                { id: 'control', label: 'CONTROL', icon: Gauge },
                { id: 'ingest', label: 'INGESTION', icon: Share2 },
                { id: 'catalog', label: 'CATALOG', icon: Box },
                { id: 'terminal', label: 'TERMINAL', icon: Terminal }
              ].map((m) => (
                <button 
                  key={m.id}
                  onClick={() => setView(m.id as any)}
                  className={`flex items-center gap-2.5 px-5 py-2.5 rounded-lg text-[9px] font-black tracking-[0.2em] transition-all duration-500 relative group overflow-hidden ${
                    view === m.id 
                      ? 'text-white' 
                      : 'text-slate-500 hover:text-cyan-400'
                  }`}
                >
                  {view === m.id && (
                    <motion.div 
                      layoutId="activeNav"
                      className="absolute inset-0 bg-cyan-600 border border-cyan-400/50 shadow-[0_0_20px_rgba(8,145,178,0.4)]"
                      transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                    />
                  )}
                  <span className="relative z-10 flex items-center gap-2">
                    <m.icon size={13} className={view === m.id ? "text-white" : "group-hover:animate-bounce"} />
                    {m.label}
                  </span>
                </button>
              ))}
            </nav>
         </div>

         <div className="flex items-center gap-10">
            <div className="flex items-center gap-6 text-right font-mono">
               <div className="group cursor-default">
                  <span className="block text-[7px] font-black text-slate-600 tracking-widest uppercase group-hover:text-cyan-500 transition-colors">LATENCY</span>
                  <span className="text-[10px] font-black text-green-500 tracking-tighter uppercase group-hover:drop-shadow-[0_0_5px_rgba(34,197,94,0.5)] transition-all">12MS / NOMINAL</span>
               </div>
               <div className="h-10 w-[1px] bg-white/5 rotate-12"></div>
               <div className="group cursor-default">
                  <span className="block text-[7px] font-black text-slate-600 tracking-widest uppercase group-hover:text-purple-500 transition-colors">SECURITY</span>
                  <span className="text-[10px] font-black text-cyan-400 tracking-tighter uppercase group-hover:drop-shadow-[0_0_5px_rgba(34,211,238,0.5)] transition-all">ENCRYPTED</span>
               </div>
            </div>
            <div className="relative group">
               <div className="absolute -inset-1 bg-cyan-500/10 blur opacity-0 group-hover:opacity-100 transition-opacity rounded-xl"></div>
               <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-600 group-focus-within:text-cyan-500 transition-colors" size={14} />
               <input 
                 type="text" 
                 placeholder="GLOBAL_SCAN..."
                 value={searchTerm}
                 onChange={(e) => setSearchTerm(e.target.value)}
                 className="w-72 bg-white/[0.03] border border-white/5 rounded-xl pl-11 pr-4 py-3 text-[10px] font-black tracking-widest text-white focus:outline-none focus:border-cyan-500/40 focus:bg-white/[0.05] transition-all uppercase placeholder:text-slate-800"
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
                   <NeonCard title="SYSTEM_OVERVIEW" icon={Gauge} color="blue">
                      <div className="space-y-6">
                         <IntelStat label="TOTAL_ENTROPY" value={stats?.total} color="blue" icon={Database} />
                         <IntelStat label="ACTIVE_CLUSTERS" value={stats?.clusters} color="purple" icon={Layers} />
                         <IntelStat label="PROCESSED_NODES" value={stats?.research?.done} color="green" icon={Sparkles} />
                         <IntelStat label="DUPLICATE_SIG" value={stats?.duplicates} color="yellow" icon={Shield} />
                      </div>
                      
                      <div className="mt-8 pt-6 border-t border-white/5 space-y-3">
                         <button 
                           onClick={() => axios.post('/api/research/start')}
                           className="w-full py-3 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 rounded-lg text-[9px] font-black tracking-[0.2em] uppercase hover:bg-emerald-500/20 active:scale-95 transition-all shadow-[0_0_15px_rgba(16,185,129,0.1)]"
                         >
                           {workerStatus?.running ? 'ENGINE_ONLINE' : 'INITIATE_RESEARCH'}
                         </button>
                         <button 
                           onClick={() => axios.post('/api/research/stop')}
                           className="w-full py-3 bg-rose-500/10 border border-rose-500/20 text-rose-400 rounded-lg text-[9px] font-black tracking-[0.2em] uppercase hover:bg-rose-500/20 active:scale-95 transition-all shadow-[0_0_15px_rgba(244,63,94,0.1)]"
                         >
                           SUSPEND_OPERATIONS
                         </button>
                         <button 
                           onClick={() => axios.post('/api/bookmarks/deduplicate')}
                           className="w-full py-3 bg-amber-500/10 border border-amber-500/20 text-amber-400 rounded-lg text-[9px] font-black tracking-[0.2em] uppercase hover:bg-amber-500/20 active:scale-95 transition-all shadow-[0_0_15px_rgba(245,158,11,0.1)]"
                         >
                           PURGE_DUPLICATES
                         </button>
                      </div>
                   </NeonCard>

                   <NeonCard title="CORE_LOAD" icon={Cpu} color="blue">
                      <div className="flex items-center justify-between mb-4">
                         <span className="text-[8px] font-black text-slate-500 tracking-[0.3em] uppercase">PROCESSING_ENTROPY</span>
                         <span className="text-[11px] font-black text-cyan-400 font-mono">14.2%</span>
                      </div>
                      <div className="h-24 flex items-end gap-1 px-1">
                         {Array.from({ length: 20 }).map((_, i) => (
                           <motion.div 
                             key={i}
                             animate={{ height: [10, Math.random() * 60 + 10, 10] }}
                             transition={{ repeat: Infinity, duration: 0.8 + Math.random(), ease: "easeInOut" }}
                             className="flex-1 bg-gradient-to-t from-cyan-600/40 to-cyan-400/20 rounded-t-sm"
                           />
                         ))}
                      </div>
                   </NeonCard>
                </div>

                {/* Center Column - Visual Map */}
                <div className="col-span-6 flex flex-col gap-8">
                   <NeonCard title="TOPOLOGICAL_MAP" icon={Globe} className="flex-1 min-h-[500px]" color="purple">
                      <div className="absolute inset-0 z-0 opacity-[0.03] bg-[radial-gradient(#22d3ee_1px,transparent_1px)] bg-[size:30px_30px]"></div>
                      <ForceGraph nodes={graphData?.nodes || []} links={graphData?.links || []} />
                   </NeonCard>
                   
                   <NeonCard title="COGNITIVE_CLOUD" icon={TagIcon} color="blue">
                      <div className="absolute top-0 right-0 p-4 opacity-10">
                         <Sparkles size={40} className="text-cyan-500" />
                      </div>
                      <TagCloud bookmarks={bookmarksData?.bookmarks || []} />
                   </NeonCard>
                </div>

                {/* Right Column - Logs */}
                <div className="col-span-3 flex flex-col h-full">
                   <NeonCard title="REALTIME_STREAM" icon={Activity} className="h-full" color="blue">
                      <div className="space-y-4 font-mono">
                         {(liveFeed || []).slice(0, 18).map((log, i) => (
                           <div key={log.id} className="flex gap-4 border-l border-cyan-500/20 pl-4 py-1.5 group cursor-default hover:bg-white/[0.02] transition-colors rounded-r-lg">
                              <span className="text-[8px] text-slate-600 font-bold group-hover:text-cyan-500/60 transition-colors">{new Date(log.imported_at || Date.now()).toLocaleTimeString()}</span>
                              <span className={`text-[9px] font-black ${log.research_status === 'done' ? 'text-emerald-500/70' : 'text-cyan-500/70'} tracking-tighter uppercase group-hover:text-white transition-all truncate`}>
                                {log.research_status === 'done' ? 'STABLE' : 'PENDING'}: {log.page_title || log.url}
                              </span>
                           </div>
                         ))}
                         {(!liveFeed || liveFeed.length === 0) && (
                           <div className="text-[9px] font-black text-slate-800 uppercase tracking-[0.5em] text-center mt-32 italic animate-pulse">AWAITING_DATA_STREAM...</div>
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
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8 pb-24">
                  {(bookmarksData?.bookmarks || []).map((bm: Bookmark) => (
                    <NeonCard key={bm.id} title={bm.is_duplicate ? "DUPLICATE_SIG" : "KNOWLEDGE_NODE"} icon={bm.is_duplicate ? Shield : Box} className="h-fit group" color={bm.is_duplicate ? "red" : "blue"}>
                      <div className="space-y-5">
                        <div className="relative">
                          <h4 className="text-[11px] font-black text-white leading-tight uppercase tracking-[0.15em] line-clamp-2 group-hover:text-cyan-400 transition-colors">{bm.page_title || bm.url}</h4>
                          <div className="absolute -left-5 top-0 w-1 h-full bg-cyan-500/0 group-hover:bg-cyan-500/40 transition-all rounded-full" />
                        </div>
                        <p className="text-[10px] text-slate-400 font-bold leading-relaxed line-clamp-3 italic uppercase tracking-tight opacity-70 group-hover:opacity-100 transition-opacity">
                          {bm.page_description || 'NO_METADATA_EXTRACTED_YET'}
                        </p>
                        <div className="flex items-center justify-between pt-4 border-t border-white/5">
                          <span className={`text-[8px] font-black px-2.5 py-1 rounded-md border ${bm.research_status === 'done' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' : 'bg-cyan-500/10 text-cyan-400 border-cyan-500/20'} uppercase tracking-[0.2em] shadow-sm`}>
                            {bm.research_status}
                          </span>
                          <div className="flex gap-4">
                             <a href={bm.url} target="_blank" rel="noreferrer" className="text-slate-500 hover:text-cyan-400 transition-all hover:scale-110">
                                <Globe size={16} />
                             </a>
                             <button className="text-slate-500 hover:text-white transition-all hover:scale-110">
                                <ArrowRight size={16} />
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
               initial={{ opacity: 0, y: 20 }}
               animate={{ opacity: 1, y: 0 }}
               exit={{ opacity: 0, y: -20 }}
               className="flex-1 grid grid-cols-12 gap-8 overflow-y-auto max-h-[80vh] pr-4 custom-scrollbar"
             >
                <div className="col-span-8 space-y-8">
                   <NeonCard title="HARVEST_VELOCITY" icon={Activity}>
                      <div className="h-64 flex items-end gap-2 px-2">
                        {(timeline || []).slice().reverse().map((day: any, i: number) => (
                          <div key={i} className="flex-1 flex flex-col justify-end gap-1 group">
                             <div className="opacity-0 group-hover:opacity-100 transition-opacity text-[7px] text-blue-400 text-center mb-1">{day.count}</div>
                             <motion.div 
                               initial={{ height: 0 }}
                               animate={{ height: `${Math.min(100, (day.count / (stats?.total || 1)) * 1000)}%` }}
                               className="bg-blue-500/20 group-hover:bg-blue-500/40 border-t border-blue-500/50 rounded-t-sm transition-all"
                             />
                          </div>
                        ))}
                        {(!timeline || timeline.length === 0) && Array.from({ length: 30 }).map((_, i) => (
                          <div key={i} className="flex-1 bg-white/5 rounded-t-sm h-4 animate-pulse" />
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
                               <span className="block text-xl font-black text-white">{stats?.clusters || 0}</span>
                               <span className="text-[8px] font-black text-slate-500 uppercase tracking-widest">CLUSTERS</span>
                            </div>
                         </div>
                         <div className="mt-4 space-y-2">
                            {(categories || []).slice(0, 4).map((cl: any, idx: number) => (
                              <div key={cl.name} className="flex items-center justify-between">
                                 <div className="flex items-center gap-2">
                                    <div className={`w-1.5 h-1.5 rounded-full ${['bg-blue-500', 'bg-purple-500', 'bg-green-500', 'bg-yellow-500'][idx % 4]}`}></div>
                                    <span className="text-[8px] font-black text-slate-400 uppercase tracking-widest truncate max-w-[100px]">{cl.name}</span>
                                 </div>
                                 <span className="text-[9px] font-black text-white">{cl.value}</span>
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
                         {(tagsData || []).map((t: any) => (
                           <span key={t.name} className="px-2 py-1 bg-white/5 border border-white/5 rounded text-[8px] font-black text-slate-500 hover:text-blue-400 hover:border-blue-500/30 transition-all cursor-pointer uppercase tracking-widest">
                              {t.name} <span className="text-blue-500/40 ml-1">{t.value}</span>
                           </span>
                         ))}
                      </div>
                   </NeonCard>

                   <NeonCard title="BATTLE_CARDS" icon={Shield}>
                      <div className="space-y-4">
                         {(battleCards || []).map(card => (
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
                         {(systemLogs || []).map((log, idx) => (
                           <div key={idx}>{log}</div>
                         ))}
                         <div className="animate-pulse">[LISTENING] AWAITING_INCOMING_RESOURCE_PACKETS...</div>
                      </div>
                   </NeonCard>
                </div>
             </motion.div>
           )}

         </AnimatePresence>
      </main>

      {/* Footer HUD */}
      <footer className="h-12 border-t border-white/5 bg-[#020408] px-8 flex items-center justify-between text-[8px] font-black tracking-[0.5em] text-slate-600 uppercase shadow-[0_-10px_40px_rgba(0,0,0,0.5)]">
         <div className="flex gap-12">
            <span className="flex items-center gap-3 group cursor-default">
               <div className="w-2 h-2 rounded-full bg-cyan-500 group-hover:animate-ping"></div> 
               STORAGE: <span className="text-slate-400 group-hover:text-cyan-400 transition-colors">1.4GB / 5.0GB</span>
            </span>
            <span className="flex items-center gap-3 group cursor-default">
               <div className="w-2 h-2 rounded-full bg-fuchsia-500 group-hover:animate-ping"></div> 
               COMPRESSION: <span className="text-slate-400 group-hover:text-fuchsia-400 transition-colors">4.2X</span>
            </span>
         </div>
         <div className="flex gap-10 italic font-mono">
            <span className="text-cyan-500/30 hover:text-cyan-400 cursor-pointer transition-all hover:tracking-[0.8em]">V_2.04</span>
            <span className="text-cyan-500/30 hover:text-cyan-400 cursor-pointer transition-all hover:tracking-[0.8em]">KERN_ESTABLISHED</span>
         </div>
      </footer>
    </div>
  );
}

export default App;
