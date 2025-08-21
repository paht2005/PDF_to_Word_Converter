# PDF → Word Converter – Streamlit-based Document Toolkit
PDF → Word Converter is a simple yet powerful web application built with **Streamlit**.  
It allows users to upload PDF files and convert them into editable Word documents (.docx) directly in the browser.


  
<img src="demo.png"><br/>
<i>Sample </i>

---

## Table of Contents

1. [Project Overview](#-project-overview)  
2. [Features](#-features)  
3. [Project Structure](#-project-structure)  
4. [Use Cases](#-use-cases)  
5. [Tech Stack](#-tech-stack)  
6. [Installation](#-installation)  
7. [Feature Details](#-feature-details)  
8. [How It Works](#-how-it-works)  
9. [Known Issues](#-known-issues)  
10. [Future Enhancements](#-future-enhancements)  
11. [License](#-license)  
12. [Contributing](#-contributing)  
13. [Contact](#-contact)  

---

## Project Overview

### 1. This app is designed to:
- Upload PDF files up to **200MB**.  
- Convert PDF pages into **.docx Word files**.  
- Provide real-time feedback in a user-friendly Streamlit interface.  
- Support both **single file conversion** and **multiple files** (zipped).  

### 2. Why this project?
- Many existing PDF-to-Word tools are paid or limit free usage.  
- This is a lightweight, open-source alternative for **students, office workers, and researchers**.  

---

## Features

| Feature Name              | Description                                      | Library Used |
|----------------------------|--------------------------------------------------|--------------|
| **Single File Conversion** | Upload and convert a PDF into `.docx`.           | `pdf2docx`, `python-docx` |
| **Batch Conversion**       | Convert multiple PDFs and download as `.zip`.    | `zipfile`, `io.BytesIO` |
| **Clean UI**               | Simple drag-and-drop interface powered by Streamlit. | `streamlit` |
| **Safe Filenames**         | Auto-generate filenames with hash + timestamp.   | `hashlib`, `time` |

---

## Project Structure
