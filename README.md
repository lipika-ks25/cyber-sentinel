# 🔐 Cyber Sentinel

A lightweight Python tool that **monitors sensitive files** and sends instant **email alerts** to the owner when unauthorized changes are detected.

---

## 📌 Features

- 🛡️ Real-time file change detection
- 📬 Email alerts with timestamp and file details
- 🖥️ GUI interface for easy setup
- 💻 Lightweight, no cloud required

---

## 🧠 Tech Stack

- Python 3
- `smtplib` (for sending email)
- `os`, `time`, `hashlib` (for monitoring)
- `tkinter` (for basic GUI interface)

## 🚀 How to Run

1. Clone the repository
2. Install dependencies  
(**No external libraries required, all standard Python modules**)
3. Configure Email Settings  
Edit `config.json` to include your email, password, and file path to monitor.
{
  "email": "yourmail@example.com",
  "password": "your-app-password",
  "file_path": "C:/path/to/your/file.txt"
}
4. Run the tool
python alert.py
💡 Make sure to use an app-specific password for Gmail.