# SAHAYA - SIH 26089 Prototype

This is the frontend prototype for SAHAYA: Cooperative-Owned Digital Workforce & Community Service Platform.

## Monorepo Structure

```
SIH WINNERS/
├── mobile/
│   ├── consumer_app/       (Flutter) - Consumer-facing UI
│   └── worker_app/         (Flutter) - Worker-facing UI
├── admin-dashboard/        (React/TS) - Admin web dashboard
└── README.md
```

## Setup & Running

### 1. Consumer App
```bash
cd mobile/consumer_app
flutter run -d chrome
```
*Provides simulated OTP (123456), natural language search UI, category browsing, and emergency booking.*

### 2. Worker App
```bash
cd mobile/worker_app
flutter run -d chrome
```
*Provides simulated OTP (654321), cooperative verification badge, availability toggle, AI allocation recommendation, and job acceptance UI.*

### 3. Admin Dashboard
```bash
cd admin-dashboard
npm install
npm run dev
```
*Provides high-level cooperative statistics, pending verification queues, and dispute resolution UI.*

## What is Fully Functional (Frontend Mode)
- **UI Architecture**: Flutter Material 3 standard implemented.
- **Routing**: Flow from Splash -> Login -> Dashboard.
- **State**: Basic ephemeral state (OTP simulation, Availability toggles).
- **Design System**: Official SAHAYA color palette implemented.

## What is Mocked / Simulated
- OTP Authentication (Accepts hardcoded values)
- Backend APIs
- Database / PostGIS logic
- Real-time WebSockets
- No telephony/IVR components exist in this system.

## Next Steps for Integration
1. Configure `pubspec.yaml` with `http` or `dio` packages.
2. Replace mock JSON/hardcoded strings with `FutureBuilder` pulling from Node.js backend.
3. Replace mock maps with `google_maps_flutter` when API keys are available.
