"""Local HTTP launcher for the 9:16 webcam recorder (ensures secure http://127.0.0.1 context)."""

import functools
import http.server
import os
import socket
import subprocess
import sys
import threading
import urllib.request
import webbrowser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "127.0.0.1"
BASE_PORT = 8090


def find_browser_exe():
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    return None


def open_url(url):
    browser = find_browser_exe()
    if browser:
        subprocess.Popen([browser, url], close_fds=True)
    else:
        webbrowser.open(url)


def is_our_server_running(port):
    try:
        with urllib.request.urlopen(f"http://{HOST}:{port}/index.html", timeout=1.0) as resp:
            body = resp.read(512).decode("utf-8", errors="ignore")
            return "Logitech 1080p" in body
    except Exception:
        return False


def pick_port():
    for port in range(BASE_PORT, BASE_PORT + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex((HOST, port)) != 0:
                return port, False
        if is_our_server_running(port):
            return port, True
    raise RuntimeError("No free localhost port found between 8090 and 8109.")


def main():
    os.chdir(ROOT_DIR)
    port, already_running = pick_port()
    url = f"http://{HOST}:{port}/"

    if already_running:
        print(f"Recorder server already running at {url}")
        open_url(url)
        return 0

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT_DIR)
    server = http.server.ThreadingHTTPServer((HOST, port), handler)

    print(f"Serving 9:16 Webcam Studio at {url}")
    print("Keep this window open while recording. Press Ctrl+C to stop.")

    threading.Timer(0.4, open_url, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
