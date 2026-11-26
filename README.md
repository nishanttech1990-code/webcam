# webcam

Logitech 1080p → 9:16 Vertical HD Video Recorder (pure HTML5 + Canvas + MediaRecorder).

## Features
- Records **9:16 vertical MP4 / WebM** directly in Chrome or Edge.
- Supports both **Horizontal Mount (Center 9:16 Crop)** (`608×1080` native / `720×1280` HD) and **Rotated 90°** (`1080×1920` Full HD).
- Camera & microphone selector with live dBFS audio level meter.
- Uses `MediaStreamTrackProcessor` (with Web Worker fallback) to avoid background-tab frame drops.

## Usage
- **GitHub Pages (HTTPS):** Open the published `index.html` URL in Chrome or Edge.
- **Offline on Windows:** Double-click `Start_Recorder.bat` to serve on `http://127.0.0.1:8090/`.
