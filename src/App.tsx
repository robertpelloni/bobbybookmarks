import React, { useState } from 'react';
import { 
  Database, LayoutGrid, Gauge, Zap, 
  Cpu, Sparkles, Scale, Search, 
  ArrowRight, Tag as TagIcon, MoreVertical 
} from 'lucide-react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';
import { Bookmark, Stats, WorkerStatus } from './types';

function App() {
  const [view, setView] = useState<'grid' | 'import' | 'control'>('import');
  const [searchTerm, setSearchTerm] = useState('');
  const queryClient = useQueryClient();

  const { data: stats } = useQuery<Stats>({
    queryKey: ['stats'],
    queryFn: () => axios.get('/api/stats').then(res => res.data),
    refetchInterval: 10000,
  });

  const { data: bookmarksData } = useQuery<{ bookmarks: Bookmark[], total: number }>({
    queryKey: ['bookmarks', searchTerm],
    queryFn: () => axios.get('/api/bookmarks', { params: { q: searchTerm } }).then(res => res.data),
    enabled: view === 'grid',
  });

  const { data: workerStatus } = useQuery<WorkerStatus>({
    queryKey: ['workerStatus'],
    queryFn: () => axios.get('/api/research/status').then(res => res.data),
    refetchInterval: 5000,
  });

  return (
    <div className="min-h-screen bg-[#0a0f1d] text-[#e2e8f0] font-sans selection:bg-[#3b82f6]/30">
      {/* Header */}
      <header className="border-b border-[#1e293b] bg-[#0f172a]/80 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-[1600px] mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 bg-gradient-to-tr from-[#3b82f6] to-[#8b5cf6] rounded-xl flex items-center justify-center shadow-lg shadow-blue-500/20">
              <Zap size={22} className="text-white fill-white" />
            </div>
            <div>
              <h1 className="text-xl font-black tracking-tight text-white uppercase">BobbyBookmarks <span className="text-[#3b82f6]">TS</span></h1>
              <div className="flex items-center gap-3 mt-0.5">
                <div className="flex items-center gap-1.5 px-2 py-0.5 bg-[#1e293b] rounded-md border border-[#334155]">
                  <div className={`w-1.5 h-1.5 rounded-full ${workerStatus?.running ? 'bg-green-400 animate-pulse' : 'bg-slate-500'}`}></div>
                  <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">{workerStatus?.worker_mode || 'STOPPED'}</span>
                </div>
                <span className="text-[11px] font-medium text-slate-500">{stats?.total || 0} RESOURCES</span>
              </div>
            </div>
          </div>

          <nav className="flex items-center bg-[#1e293b]/50 p-1 rounded-xl border border-[#334155]">
            <button 
              onClick={() => setView('import')}
              className={`flex items-center gap-2 px-5 py-2 rounded-lg text-sm font-bold transition-all ${view === 'import' ? 'bg-[#3b82f6] text-white shadow-lg shadow-blue-500/30' : 'text-slate-400 hover:text-white'}`}
            >
              <Database size={16} /> INGESTION
            </button>
            <button 
              onClick={() => setView('control')}
              className={`flex items-center gap-2 px-5 py-2 rounded-lg text-sm font-bold transition-all ${view === 'control' ? 'bg-[#3b82f6] text-white shadow-lg shadow-blue-500/30' : 'text-slate-400 hover:text-white'}`}
            >
              <Gauge size={16} /> CONTROL
            </button>
            <button 
              onClick={() => setView('grid')}
              className={`flex items-center gap-2 px-5 py-2 rounded-lg text-sm font-bold transition-all ${view === 'grid' ? 'bg-[#3b82f6] text-white shadow-lg shadow-blue-500/30' : 'text-slate-400 hover:text-white'}`}
            >
              <LayoutGrid size={16} /> CATALOG
            </button>
          </nav>

          <div className="relative w-72">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" size={16} />
            <input 
              type="text" 
              placeholder="GLOBAL SEARCH..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-[#1e293b] border border-[#334155] rounded-xl pl-10 pr-4 py-2 text-sm focus:outline-none focus:border-[#3b82f6] transition-colors placeholder:text-slate-600 font-bold tracking-tight"
            />
          </div>
        </div>
      </header>

      <main className="max-w-[1600px] mx-auto p-8">
        {view === 'import' && (
          <div className="max-w-4xl mx-auto space-y-6">
             <div className="bg-[#0f172a] border border-[#1e293b] rounded-2xl overflow-hidden shadow-2xl">
                <div className="p-6 border-b border-[#1e293b] flex items-center justify-between bg-gradient-to-r from-[#0f172a] to-[#1e293b]/50">
                  <div>
                    <h2 className="text-lg font-black text-white tracking-tight flex items-center gap-2">
                      <Database className="text-[#3b82f6]" size={20} /> RESOURCE ASSIMILATION
                    </h2>
                    <p className="text-slate-500 text-xs font-medium mt-1 uppercase tracking-wider">Feed the machine with raw URLs or text content</p>
                  </div>
                </div>
                <div className="p-6">
                  <textarea 
                    className="w-full h-80 bg-[#020617] border border-[#1e293b] rounded-xl p-6 font-mono text-sm text-[#34d399] focus:outline-none focus:border-[#3b82f6]/50 transition-colors resize-none leading-relaxed"
                    placeholder="PASTE URLS (ONE PER LINE) OR MARKDOWN/HTML CONTENT..."
                  ></textarea>
                  <div className="mt-6 flex items-center justify-between">
                    <div className="flex items-center gap-2 text-[11px] font-bold text-slate-500 uppercase tracking-widest">
                       <div className="w-1.5 h-1.5 bg-[#3b82f6] rounded-full"></div>
                       PENDING DETECTION
                    </div>
                    <button className="bg-[#3b82f6] hover:bg-[#2563eb] text-white px-8 py-3 rounded-xl font-black text-sm tracking-tighter uppercase flex items-center gap-3 transition-all shadow-xl shadow-blue-500/20 active:scale-95">
                      <Zap size={18} className="fill-white" />
                      ASSIMILATE RESOURCES
                    </button>
                  </div>
                </div>
             </div>
          </div>
        )}

        {view === 'grid' && (
          <div className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
              {bookmarksData?.bookmarks.map((bm: Bookmark) => (
                <div key={bm.id} className="group bg-[#0f172a] border border-[#1e293b] rounded-2xl p-5 hover:border-[#3b82f6]/50 transition-all hover:shadow-2xl hover:shadow-blue-500/5 flex flex-col relative overflow-hidden">
                  <div className="flex items-start justify-between mb-4">
                    <div className="w-10 h-10 bg-[#1e293b] rounded-xl flex items-center justify-center group-hover:bg-[#3b82f6]/10 transition-colors">
                      <LayoutGrid size={20} className="text-slate-400 group-hover:text-[#3b82f6]" />
                    </div>
                    <button className="text-slate-600 hover:text-white transition-colors">
                      <MoreVertical size={18} />
                    </button>
                  </div>
                  <h3 className="font-bold text-white leading-tight mb-2 line-clamp-2 group-hover:text-[#3b82f6] transition-colors">{bm.page_title || bm.url}</h3>
                  <p className="text-slate-400 text-xs line-clamp-3 mb-4 leading-relaxed font-medium">{bm.page_description || 'NO DESCRIPTION EXTRACTED YET.'}</p>
                  
                  <div className="mt-auto pt-4 flex flex-wrap gap-2">
                    {bm.is_duplicate && <span className="bg-orange-500/10 text-orange-400 text-[9px] font-black px-2 py-0.5 rounded border border-orange-500/20 uppercase tracking-tighter">DUPLICATE</span>}
                    <span className={`text-[9px] font-black px-2 py-0.5 rounded border uppercase tracking-tighter ${
                      bm.research_status === 'done' ? 'bg-green-500/10 text-green-400 border-green-500/20' : 
                      bm.research_status === 'running' ? 'bg-blue-500/10 text-blue-400 border-blue-500/20' :
                      'bg-slate-500/10 text-slate-400 border-slate-500/20'
                    }`}>{bm.research_status}</span>
                  </div>

                  <a href={bm.url} target="_blank" className="absolute top-0 right-0 left-0 bottom-0 opacity-0" rel="noreferrer">Open</a>
                </div>
              ))}
            </div>
          </div>
        )}

        {view === 'control' && (
          <div className="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Worker Control */}
            <div className="bg-[#0f172a] border border-[#1e293b] rounded-2xl overflow-hidden shadow-2xl flex flex-col">
              <div className="p-6 border-b border-[#1e293b] bg-gradient-to-r from-[#0f172a] to-[#1e293b]/50">
                <h2 className="text-lg font-black text-white tracking-tight flex items-center gap-2">
                  <Cpu className="text-[#3b82f6]" size={20} /> RESEARCH CORE
                </h2>
              </div>
              <div className="p-8 flex flex-col h-full">
                <div className="flex items-center gap-4 mb-8">
                  <div className={`w-3 h-3 rounded-full ${workerStatus?.running ? 'bg-green-400 animate-pulse' : 'bg-slate-600'}`}></div>
                  <span className="text-sm font-black text-white uppercase tracking-tighter">
                    STATUS: <span className={workerStatus?.running ? 'text-green-400' : 'text-slate-400'}>{workerStatus?.running ? 'ACTIVE' : 'OFFLINE'}</span>
                  </span>
                </div>

                <div className="grid grid-cols-3 gap-4 mb-8">
                  <div className="bg-[#020617] p-4 rounded-xl border border-[#1e293b] text-center">
                    <span className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-1">PENDING</span>
                    <span className="text-2xl font-black text-white tracking-tighter">{workerStatus?.pending || 0}</span>
                  </div>
                  <div className="bg-[#020617] p-4 rounded-xl border border-[#1e293b] text-center">
                    <span className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-1">ACTIVE</span>
                    <span className="text-2xl font-black text-[#3b82f6] tracking-tighter">{workerStatus?.running_count || 0}</span>
                  </div>
                  <div className="bg-[#020617] p-4 rounded-xl border border-[#1e293b] text-center">
                    <span className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-1">DONE</span>
                    <span className="text-2xl font-black text-green-400 tracking-tighter">{workerStatus?.done || 0}</span>
                  </div>
                </div>

                <button className={`w-full py-4 rounded-xl font-black text-sm tracking-widest uppercase transition-all shadow-xl active:scale-95 flex items-center justify-center gap-3 ${
                  workerStatus?.running ? 'bg-red-500/10 text-red-500 border border-red-500/30 hover:bg-red-500/20' : 'bg-green-500/10 text-green-500 border border-green-500/30 hover:bg-green-500/20'
                }`}>
                  {workerStatus?.running ? <ArrowRight size={18} className="rotate-90" /> : <Zap size={18} className="fill-current" />}
                  {workerStatus?.running ? 'SHUT DOWN WORKER' : 'INITIATE RESEARCH'}
                </button>
              </div>
            </div>

            {/* Maintenance */}
            <div className="bg-[#0f172a] border border-[#1e293b] rounded-2xl overflow-hidden shadow-2xl flex flex-col">
              <div className="p-6 border-b border-[#1e293b] bg-gradient-to-r from-[#0f172a] to-[#1e293b]/50">
                <h2 className="text-lg font-black text-white tracking-tight flex items-center gap-2">
                  <Sparkles className="text-[#3b82f6]" size={20} /> DATA MAINTENANCE
                </h2>
              </div>
              <div className="p-8 space-y-4">
                <button className="w-full p-4 bg-[#1e293b]/50 border border-[#334155] rounded-xl flex items-center gap-4 hover:border-[#3b82f6]/50 transition-all group">
                   <div className="w-10 h-10 bg-[#1e293b] rounded-lg flex items-center justify-center group-hover:bg-[#3b82f6] group-hover:text-white transition-all">
                     <Sparkles size={20} />
                   </div>
                   <div className="text-left">
                     <span className="block text-xs font-black text-white uppercase tracking-tighter">RE-RUN CLUSTERING</span>
                     <span className="text-[10px] font-medium text-slate-500 uppercase tracking-widest">ORGANIZE CONCEPTUAL MAP</span>
                   </div>
                </button>
                <button className="w-full p-4 bg-[#1e293b]/50 border border-[#334155] rounded-xl flex items-center gap-4 hover:border-[#3b82f6]/50 transition-all group">
                   <div className="w-10 h-10 bg-[#1e293b] rounded-lg flex items-center justify-center group-hover:bg-orange-500 group-hover:text-white transition-all">
                     <Scale size={20} />
                   </div>
                   <div className="text-left">
                     <span className="block text-xs font-black text-white uppercase tracking-tighter">MERGE DUPLICATES</span>
                     <span className="text-[10px] font-medium text-slate-500 uppercase tracking-widest">DEDUPLICATE KNOWLEDGE BASE</span>
                   </div>
                </button>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
