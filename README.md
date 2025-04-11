# 🦇 Darkwing Dox v3.3 – Webigail Rising

Darkwing Dox is a document extraction and forensics tool that rips images, diagrams, metadata, and hidden gems from `.doc` and `.docx` files. With **Webigail**, it also downloads files via URL and processes them automatically.

---

## 🚀 Features

- 🖱️ Drag-and-drop `.doc` or `.docx`
- 📂 Extract embedded media (`.wmf`, `.png`, `.svg`, `.ole`, etc.)
- 🧠 Metadata extraction (author, app info, timestamps)
- 🔗 URL harvesting from text content
- 🖼️ Full-page render to PNG + optional OCR
- 🕷️ **Webigail**: Download and extract from URL or URL queue
- 🔧 GUI checkboxes for:
  - Export `.svg`
  - Export `.png`
  - Run OCR
- 🛡️ Spoofs referrer headers (Webigail mode)
- 💾 Outputs into `ripped_output_<filename>` next to the original doc

---

## 🔧 Setup

1. Install dependencies:
```bash
pip install python-docx Pillow pytesseract requests
