export interface Bookmark {
  id: number;
  url: string;
  title: string;
  description: string;
  page_title: string;
  page_description: string;
  research_status: 'pending' | 'running' | 'done' | 'failed' | 'skipped' | string;
  imported_at: string;
  researched_at?: string;
  cluster_id?: number;
  source: string;
  is_duplicate: boolean;
  original_id?: number;
  category?: string;
  short_description?: string;
  long_description?: string;
  tags?: string;
  main_features?: string;
  research_level?: string;
  innovation_score?: number;
}

export interface Stats {
  total: number;
  unique: number;
  clusters: number;
  duplicates: number;
  atlas_entries?: number;
  atlas_layers?: number;
  mcp_catalog_entries?: number;
  research?: {
    pending: number;
    running: number;
    done: number;
    failed: number;
    skipped?: number;
  };
}

export interface WorkerStatus {
  running: boolean;
  worker_mode: 'stopped' | 'app' | 'external' | string;
  pending: number;
  running_count: number;
  done: number;
  failed: number;
}

export interface SkillExecution {
  id: number;
  skill_name: string;
  strategy: string;
  execution_count: number;
  success_count: number;
  win_rate: number;
  status: string;
}

export interface AtlasLayer {
  name: string;
  slug: string;
  count: number;
}

export interface AtlasSummary {
  total_entries: number;
  total_layers: number;
  layers: AtlasLayer[];
}
