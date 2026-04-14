const { build } = require('vite');
const react = require('@vitejs/plugin-react');
const path = require('path');

async function runBuild() {
  try {
    console.log('Starting Vite build via CommonJS API with explicit config...');
    await build({
      root: __dirname,
      base: '/',
      plugins: [react()],
      build: {
        outDir: 'dist',
        emptyOutDir: true
      }
    });
    console.log('Vite build completed successfully.');
  } catch (error) {
    console.error('Vite build failed:', error);
    process.exit(1);
  }
}

runBuild();
