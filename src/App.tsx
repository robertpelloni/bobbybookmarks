import React, { useState, useEffect } from 'react';
import CyberKineticHud from './CyberKineticHud';
import CleanUtilityHud from './CleanUtilityHud';

export type HudMode = 'cyber' | 'utility';

export function App() {
  const [hudMode, setHudMode] = useState<HudMode>(() => {
    const saved = typeof window !== 'undefined' ? window.localStorage.getItem('bobbyintel_hud_mode') : null;
    return saved === 'utility' ? 'utility' : 'cyber';
  });

  useEffect(() => {
    try {
      window.localStorage.setItem('bobbyintel_hud_mode', hudMode);
    } catch {
      // ignore storage errors
    }
  }, [hudMode]);

  if (hudMode === 'utility') {
    return <CleanUtilityHud onSwitchMode={() => setHudMode('cyber')} />;
  }

  return <CyberKineticHud onSwitchMode={() => setHudMode('utility')} />;
}

export default App;
