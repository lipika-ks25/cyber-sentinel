# 

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alert import send_email_alert  # Make sure alert.py is in the same folder

import time
import os

class MonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"[MODIFIED] {event.src_path}")
            send_email_alert("File Modified", f"A file was modified: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"[CREATED] {event.src_path}")
            send_email_alert("New File Created", f"A new file was created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[DELETED] {event.src_path}")
            send_email_alert("File Deleted", f"A file was deleted: {event.src_path}")

def start_monitoring(path):
    event_handler = MonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print(f"[INFO] Monitoring started on: {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        messagebox.showinfo("Monitoring Started", f"Monitoring started on:\n{folder_path}")
        # Run monitoring in a background thread
        threading.Thread(target=start_monitoring, args=(folder_path,), daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("Cybersecurity File Monitor")
root.geometry("400x200")

label = tk.Label(root, text="Select a folder to monitor for changes:")
label.pack(pady=20)

select_btn = tk.Button(root, text="Choose Folder", command=choose_folder)
select_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()