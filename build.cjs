const path = require('path');

// Vite 6 is ESM only, so we must use a dynamic import even in a CJS script
async function runBuild() {
  try {
    console.log('Starting programmatic Vite build (dynamic import)...');
    
    // Dynamically import Vite's build function and the React plugin
    const { build } = await import('vite');
    const react = (await import('@vitejs/plugin-react')).default;

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
