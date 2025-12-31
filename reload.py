import time
import threading
from pathlib import Path

import webview
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

UI_DIR = Path(__file__).resolve().parent / "ui"
INDEX = (UI_DIR / "index.html").resolve()

WATCH_EXT = {".html", ".css", ".js"}

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, window):
        self.window = window
        self._last = 0

    def on_modified(self, event):
        if event.is_directory:
            return
        p = Path(event.src_path)
        if p.suffix.lower() not in WATCH_EXT:
            return

        # Debounce: manche Editoren feuern mehrfach
        now = time.time()
        if now - self._last < 0.3:
            return
        self._last = now

        print("UI changed -> reload:", p.name)
        # Alternative 1:
        self.window.evaluate_js("location.reload()")
        # Alternative 2 (wenn du wirklich index neu laden willst):
        # self.window.load_url(str(INDEX))

def start_watcher(window):
    handler = ReloadHandler(window)
    obs = Observer()
    obs.schedule(handler, str(UI_DIR), recursive=True)
    obs.start()
    print("Watching:", UI_DIR)

def main():
    window = webview.create_window("Dev Reload", url=str(INDEX), width=1200, height=800)

    def after_start():
        threading.Thread(target=start_watcher, args=(window,), daemon=True).start()
        # DevTools optional:
        # window.show_devtools()

    webview.start(after_start, debug=True)

if __name__ == "__main__":
    main()

