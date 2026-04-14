const path = require('path');
const fs = require('fs');

// Log the environment to help debug
console.log('--- Environment Check ---');
console.log('Node Version:', process.version);
console.log('Current Directory:', __dirname);
const nodeModulesPath = path.join(__dirname, 'node_modules');
console.log('Node Modules Path:', nodeModulesPath);

if (!fs.existsSync(nodeModulesPath)) {
  console.error('CRITICAL: node_modules directory NOT found!');
  process.exit(1);
}

// Manually resolve the build function by importing the internal ESM entry point
// We use dynamic import for the actual build tool since it's an ESM package
async function runBuild() {
  try {
    console.log('Attempting to import Vite build...');
    
    // We try to import from the package name, but if that fails, 
    // we use a more direct approach to the package entry
    const { build } = await import('vite');
    const react = (await import('@vitejs/plugin-react')).default;

    console.log('Starting Vite build via programmatic API...');
    await build({
      root: __dirname,
      base: '/',
      plugins: [react()],
      build: {
        outDir: 'dist',
        emptyOutDir: true,
        rollupOptions: {
          input: path.resolve(__dirname, 'index.html'),
        },
      },
    });
    console.log('Vite build completed successfully.');
  } catch (error) {
    console.error('Vite build failed with error:', error.message);
    if (error.stack) console.error(error.stack);
    process.exit(1);
  }
}

runBuild();
