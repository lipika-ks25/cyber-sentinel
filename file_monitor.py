import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alert import send_email_alert

with open('config.json') as f:
    config = json.load(f)

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f" File Modified: {event.src_path}")
            send_email_alert(" File Change Detected", f" File Modified: {event.src_path}")
    def on_created(self, event):
        if not event.is_directory:
            print(f"[CREATED] {event.src_path}")
            send_email_alert(
                subject="File created",
                body=f"New File Was Created: {event.src_path}"
            )
    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[DELETED] {event.src_path}")
            send_email_alert(
                subject="File Deleted",
                body=f"A file was deleted: {event.src_path}"
            )
def watch_files():
    path=config["file_watch_path"]
    event_handler= FileChangeHandler()
    observer= Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print(f"Watching folder: {path}")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



if __name__=="__main__":
    watch_files()
