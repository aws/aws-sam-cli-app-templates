import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig ({
  plugins: [
    vue(),
    ],    
  // ...
  test: {
    // enable jest-like global test APIs
    globals: true,
    // simulate DOM with happy-dom    
    environment: 'happy-dom'
  }
})
