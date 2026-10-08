import os
import json

base_dir = r"C:\Users\Neha\OneDrive\Desktop\SIH\SIH WINNERS\backend"
dirs = [
    "src/controllers",
    "src/routes",
    "src/services",
    "src/models",
    "src/middleware",
    "src/config",
]

for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

files = {
    "package.json": json.dumps({
      "name": "sahaya-backend",
      "version": "1.0.0",
      "main": "dist/server.js",
      "scripts": {
        "build": "tsc",
        "start": "node dist/server.js",
        "dev": "ts-node-dev --respawn src/server.ts"
      },
      "dependencies": {
        "express": "^4.18.2",
        "cors": "^2.8.5",
        "dotenv": "^16.3.1",
        "pg": "^8.11.3",
        "jsonwebtoken": "^9.0.1"
      },
      "devDependencies": {
        "@types/express": "^4.17.17",
        "@types/cors": "^2.8.13",
        "@types/node": "^20.5.0",
        "@types/pg": "^8.10.2",
        "@types/jsonwebtoken": "^9.0.2",
        "typescript": "^5.1.6",
        "ts-node-dev": "^2.0.0"
      }
    }, indent=2),
    "tsconfig.json": json.dumps({
      "compilerOptions": {
        "target": "es2016",
        "module": "commonjs",
        "rootDir": "./src",
        "outDir": "./dist",
        "esModuleInterop": True,
        "forceConsistentCasingInFileNames": True,
        "strict": True,
        "skipLibCheck": True
      }
    }, indent=2),
    "Dockerfile": """FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
""",
    "src/server.ts": """import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import authRoutes from './routes/authRoutes';
import workerRoutes from './routes/workerRoutes';
import bookingRoutes from './routes/bookingRoutes';
import aiRoutes from './routes/aiRoutes';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/workers', workerRoutes);
app.use('/api/bookings', bookingRoutes);
app.use('/api/ai', aiRoutes);

app.get('/health', (req, res) => {
  res.json({ status: 'ok', message: 'SAHAYA Backend is running' });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
""",
    "src/routes/authRoutes.ts": """import { Router } from 'express';
const router = Router();

router.post('/login', (req, res) => {
  const { phone } = req.body;
  // Mock OTP send
  res.json({ success: true, message: 'OTP sent successfully (Mock: 123456 or 654321)' });
});

router.post('/verify-otp', (req, res) => {
  const { phone, otp } = req.body;
  if (otp === '123456' || otp === '654321') {
    res.json({ success: true, token: 'mock-jwt-token-xyz', role: otp === '123456' ? 'CONSUMER' : 'WORKER' });
  } else {
    res.status(401).json({ success: false, message: 'Invalid OTP' });
  }
});

export default router;
""",
    "src/routes/workerRoutes.ts": """import { Router } from 'express';
const router = Router();

router.get('/', (req, res) => {
  res.json({
    success: true,
    data: [
      { id: 1, name: 'Ramesh Kumar', category: 'Plumbing', distance: '1.4km', rating: 4.9, verified: true },
      { id: 2, name: 'Suresh Das', category: 'Electrical', distance: '0.8km', rating: 4.6, verified: true }
    ]
  });
});

export default router;
""",
    "src/routes/bookingRoutes.ts": """import { Router } from 'express';
const router = Router();

router.post('/', (req, res) => {
  res.json({ success: true, message: 'Booking created successfully', bookingId: 'BKG-001' });
});

router.post('/emergency', (req, res) => {
  res.json({ success: true, message: 'Emergency broadcast sent', nearestWorker: 'Suresh Das', eta: '5 mins' });
});

export default router;
""",
    "src/routes/aiRoutes.ts": """import { Router } from 'express';
const router = Router();

router.get('/forecast', (req, res) => {
  res.json({
    success: true,
    forecast: {
      zone: 'Peelamedu',
      service: 'Plumbing',
      demand: 'High',
      recommendation: 'Allocate 2 additional plumbers'
    }
  });
});

export default router;
"""
}

for path, content in files.items():
    with open(os.path.join(base_dir, path), "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print("Backend scaffolded.")
