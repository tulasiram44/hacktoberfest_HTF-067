import os
import json

base_dir = r"C:\Users\Neha\OneDrive\Desktop\SIH\SIH WINNERS\admin-dashboard"
os.makedirs(base_dir, exist_ok=True)
os.makedirs(os.path.join(base_dir, "src", "components"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "src", "pages"), exist_ok=True)

files = {
    "package.json": json.dumps({
      "name": "admin-dashboard",
      "private": True,
      "version": "0.0.0",
      "type": "module",
      "scripts": {
        "dev": "vite",
        "build": "tsc && vite build",
        "preview": "vite preview"
      },
      "dependencies": {
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "lucide-react": "^0.263.1"
      },
      "devDependencies": {
        "@types/react": "^18.2.15",
        "@types/react-dom": "^18.2.7",
        "@vitejs/plugin-react": "^4.0.3",
        "autoprefixer": "^10.4.14",
        "postcss": "^8.4.27",
        "tailwindcss": "^3.3.3",
        "typescript": "^5.0.2",
        "vite": "^4.4.5"
      }
    }, indent=2),
    "vite.config.ts": "import { defineConfig } from 'vite'\nimport react from '@vitejs/plugin-react'\n\nexport default defineConfig({\n  plugins: [react()],\n})",
    "tailwind.config.js": "/** @type {import('tailwindcss').Config} */\nexport default {\n  content: [\n    \"./index.html\",\n    \"./src/**/*.{js,ts,jsx,tsx}\",\n  ],\n  theme: {\n    extend: {},\n  },\n  plugins: [],\n}",
    "postcss.config.js": "export default {\n  plugins: {\n    tailwindcss: {},\n    autoprefixer: {},\n  },\n}",
    "tsconfig.json": json.dumps({
      "compilerOptions": {
        "target": "ES2020",
        "useDefineForClassFields": True,
        "lib": ["ES2020", "DOM", "DOM.Iterable"],
        "module": "ESNext",
        "skipLibCheck": True,
        "moduleResolution": "bundler",
        "allowImportingTsExtensions": True,
        "resolveJsonModule": True,
        "isolatedModules": True,
        "noEmit": True,
        "jsx": "react-jsx"
      },
      "include": ["src"],
      "references": [{ "path": "./tsconfig.node.json" }]
    }, indent=2),
    "tsconfig.node.json": json.dumps({
      "compilerOptions": {
        "composite": True,
        "skipLibCheck": True,
        "module": "ESNext",
        "moduleResolution": "bundler",
        "allowSyntheticDefaultImports": True
      },
      "include": ["vite.config.ts"]
    }, indent=2),
    "index.html": "<!DOCTYPE html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <title>Sahaya Admin Dashboard</title>\n  </head>\n  <body>\n    <div id=\"root\"></div>\n    <script type=\"module\" src=\"/src/main.tsx\"></script>\n  </body>\n</html>",
    "src/index.css": "@tailwind base;\n@tailwind components;\n@tailwind utilities;\n\nbody { background-color: #F7F9F8; }",
    "src/main.tsx": "import React from 'react'\nimport ReactDOM from 'react-dom/client'\nimport App from './App.tsx'\nimport './index.css'\n\nReactDOM.createRoot(document.getElementById('root')!).render(\n  <React.StrictMode>\n    <App />\n  </React.StrictMode>,\n)",
    "src/App.tsx": "import React from 'react';\n\nfunction App() {\n  return (\n    <div className=\"min-h-screen p-8 text-[#26332E]\">\n      <h1 className=\"text-3xl font-bold mb-6 text-[#356B59]\">SAHAYA Admin Dashboard</h1>\n      <div className=\"grid grid-cols-1 md:grid-cols-3 gap-6\">\n        <div className=\"bg-white p-6 rounded-lg shadow-sm border border-[#DDE5E1]\">\n          <h3 className=\"text-lg font-semibold\">Total Workers</h3>\n          <p className=\"text-4xl font-bold text-[#4F806B] mt-2\">2,450</p>\n        </div>\n        <div className=\"bg-white p-6 rounded-lg shadow-sm border border-[#DDE5E1]\">\n          <h3 className=\"text-lg font-semibold\">Pending Verification</h3>\n          <p className=\"text-4xl font-bold text-[#B38A4A] mt-2\">42</p>\n        </div>\n        <div className=\"bg-white p-6 rounded-lg shadow-sm border border-[#DDE5E1]\">\n          <h3 className=\"text-lg font-semibold\">Active Disputes</h3>\n          <p className=\"text-4xl font-bold text-[#B85C5C] mt-2\">7</p>\n        </div>\n      </div>\n    </div>\n  )\n}\n\nexport default App;\n"
}

for path, content in files.items():
    with open(os.path.join(base_dir, path), "w", encoding="utf-8") as f:
        f.write(content)

print("Admin dashboard scaffolded.")
