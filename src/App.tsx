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

const NeonCard = ({ children, title, icon: Icon, className = "" }) => (
  <motion.div 
    initial={{ opacity: 0, scale: 0.98 }}
    animate={{ opacity: 1, scale: 1 }}
    className={`relative group ${className}`}
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

const IntelStat = ({ label, value, color = "blue" }) => (
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

// --- D3 FORCE GRAPH COMPONENT ---

const ForceGraph = ({ bookmarks = [] }) => {
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

    // Mock data generation for cool viz if no real data
    const nodes = bookmarks.length > 0 ? bookmarks.map(b => ({ id: b.id, name: b.page_title || b.url, group: 'node' })) : [
      { id: 'root', name: 'CORE_INTELLIGENCE', group: 'root' },
      ...Array.from({ length: 12 }).map((_, i) => ({ id: i, name: `CLUSTER_${i}`, group: 'cluster' }))
    ];

    const links = nodes.slice(1).map(n => ({ source: 'root', target: n.id }));

    const simulation = d3.forceSimulation(nodes as any)
      .force("link", d3.forceLink(links).id((d: any) => d.id).distance(120))
      .force("charge", d3.forceManyBody().strength(-200))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("collision", d3.forceCollide().radius(30));

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
      .attr("r", (d: any) => d.group === 'root' ? 12 : 6)
      .attr("fill", (d: any) => d.group === 'root' ? "#3b82f6" : "#8b5cf6")
      .attr("filter", "url(#glow)")
      .attr("stroke", "#020617")
      .attr("stroke-width", 2);

    node.append("text")
      .text((d: any) => d.name)
      .attr("x", 12)
      .attr("y", 4)
      .attr("fill", "#64748b")
      .attr("font-size", "8px")
      .attr("font-weight", "900")
      .attr("class", "uppercase tracking-tighter pointer-events-none select-none")

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
    <div ref={containerRef} className="w-full h-full relative overflow-hidden bg-[#010411]">
      <div className="absolute top-4 right-4 z-10 flex gap-2">
         <div className="px-2 py-1 bg-blue-500/10 border border-blue-500/30 rounded text-[8px] font-black text-blue-400 tracking-widest uppercase">FORCE_ACTIVE</div>
         <div className="px-2 py-1 bg-white/5 border border-white/10 rounded text-[8px] font-black text-slate-500 tracking-widest uppercase">NODES: {bookmarks.length || 13}</div>
      </div>
      <svg ref={svgRef} className="w-full h-full" />
    </div>
  );
};

function App() {
  const [view, setView] = useState<'intel' | 'ingest' | 'catalog' | 'terminal'>('intel');
  const [searchTerm, setSearchTerm] = useState('');

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

  return (
    <div className="min-h-screen bg-[#01040a] text-slate-400 font-sans selection:bg-blue-500/30 overflow-hidden flex flex-col">
      <Scanline />

      {/* Top HUD */}
      <header className="h-16 border-b border-white/5 bg-[#01040a]/90 backdrop-blur-3xl z-[150] px-8 flex items-center justify-between">
         <div className="flex items-center gap-10">
            <div className="flex items-center gap-4 group cursor-pointer">
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
                <div className="col-span-6">
                   <NeonCard title="TOPOLOGICAL_MAP" icon={Globe} className="h-full">
                      <div className="absolute inset-0 z-0 opacity-20 bg-[radial-gradient(#1e293b_1px,transparent_1px)] bg-[size:20px_20px]"></div>
                      <ForceGraph />
                   </NeonCard>
                </div>

                {/* Right Column - Logs */}
                <div className="col-span-3 flex flex-col h-full">
                   <NeonCard title="LOG_STREAM" icon={Activity} className="h-full">
                      <div className="space-y-4 font-mono">
                         {[
                           { t: '12:04:11', m: 'ASSIMILATING_URL_PACKET', s: 'blue' },
                           { t: '12:04:45', m: 'CLUSTERING_PROTOCOL_START', s: 'purple' },
                           { t: '12:05:02', m: 'DUPLICATE_SIG_DETECTED', s: 'yellow' },
                           { t: '12:05:12', m: 'DATABASE_WRITE_STABLE', s: 'green' },
                           { t: '12:06:21', m: 'RESEARCH_AGENT_SLEEP', s: 'slate' },
                           { t: '12:07:01', m: 'WEB_HOOK_STANDBY', s: 'blue' },
                         ].map((log, i) => (
                           <div key={i} className="flex gap-4 border-l border-white/5 pl-4 py-1 group cursor-default">
                              <span className="text-[9px] text-slate-700 font-bold">{log.t}</span>
                              <span className={`text-[9px] font-black text-${log.s}-500/80 tracking-tighter uppercase group-hover:text-${log.s}-400 transition-colors`}>{log.m}</span>
                           </div>
                         ))}
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
                   {[
                     { l: 'BROWSER_X', d: 'HTML_IMPORT', i: Globe, c: 'blue' },
                     { l: 'CORE_DB', d: 'SQLITE_SYNC', i: Database, c: 'purple' },
                     { l: 'RAW_STREAM', d: 'TEXT_INJECT', i: Radio, c: 'yellow' }
                   ].map((t, i) => (
                     <NeonCard key={i} className="cursor-pointer group">
                        <div className="flex flex-col items-center gap-6 py-4">
                           <div className={`w-16 h-16 rounded-2xl bg-${t.c}-500/10 flex items-center justify-center text-${t.c}-500 border border-${t.c}-500/20 group-hover:bg-${t.c}-500 group-hover:text-white transition-all shadow-xl`}>
                              <t.i size={28} />
                           </div>
                           <div className="text-center">
                              <span className="block text-[11px] font-black text-white tracking-[0.2em] mb-1">{t.l}</span>
                              <span className="text-[9px] font-bold text-slate-500 tracking-widest uppercase">{t.d}</span>
                           </div>
                        </div>
                     </NeonCard>
                   ))}
                </div>

                <NeonCard title="INJECTION_TERMINAL" icon={Terminal} className="flex-1">
                   <textarea 
                     className="w-full h-full bg-transparent border-none focus:outline-none font-mono text-[11px] text-blue-400 placeholder:text-slate-800 leading-relaxed uppercase tracking-tighter"
                     placeholder="AWAITING_INPUT_STREAM_PACKETS..."
                   />
                   <div className="absolute bottom-10 right-10 flex gap-4">
                      <button 
                        onClick={() => window.location.href = '/api/database/download'}
                        className="px-8 py-4 bg-purple-600/20 hover:bg-purple-600/40 border border-purple-500/30 text-purple-400 rounded-xl font-black text-[10px] tracking-[0.3em] uppercase transition-all flex items-center gap-4 active:scale-95"
                      >
                         <Database size={18} /> BACKUP_DB
                      </button>
                      <button className="px-12 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-black text-[10px] tracking-[0.3em] uppercase transition-all shadow-[0_0_30px_rgba(37,99,235,0.3)] flex items-center gap-4 active:scale-95">
                         <Crosshair size={18} /> INITIATE_TRANSFER
                      </button>
                   </div>
                </NeonCard>
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
            <span className="text-blue-500/50 hover:text-blue-500 cursor-pointer transition-colors">V_3.4.1</span>
            <span className="text-blue-500/50 hover:text-blue-500 cursor-pointer transition-colors">KERN_ESTABLISHED</span>
         </div>
      </footer>
    </div>
  );
}

export default App;
