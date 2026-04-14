const { build } = require('vite');

async function runBuild() {
  try {
    console.log('Starting Vite build via CommonJS API...');
    await build();
    console.log('Vite build completed successfully.');
  } catch (error) {
    console.error('Vite build failed:', error);
    process.exit(1);
  }
}

runBuild();
