# Advanced OCR Web Application

![OCR Demo]![image](https://github.com/user-attachments/assets/f15ac036-238d-43df-8286-8b1c2c466ba4)
 <!-- Replace with actual screenshot -->

A powerful Optical Character Recognition (OCR) web application that extracts text from images with multi-language support, built with Python Flask and Tesseract OCR.

## ✨ Features

- **Multi-Language OCR**: Supports English, Hindi, French, Spanish, and more
- **Interactive Preview**: Zoom, rotate, and view image thumbnails
- **User-Friendly Interface**: Drag & drop file uploads
- **Text Management**: Copy or download extracted text
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Clear user feedback for all operations

## 🛠 Tech Stack

**Backend:**
- Python
- Flask

**OCR Engine:**
- Tesseract OCR

**Frontend:**
- HTML5, CSS3
- Bootstrap 5
- Vanilla JavaScript

**Image Processing:**
- Pillow (Python Imaging Library)

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Tesseract OCR installed on your system

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/v0Xd7n/Advanced-OCR.git
   cd ocr-web-app
    ```
2. **Set up virtual environment**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
  ```
3.**Install dependencies**
  ```bash
  pip install -r requirements.txt
  ```
4.**Install Tesseract OCR**
Windows: Download from ![UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
Linux: ```sudo apt install tesseract-ocr```
Mac: ```brew install tesseract```

5.**Run the application**
```python app.py```

6.**Access the application**
Open your browser and visit:``` http://localhost:5000```

**📂 Project Structure**:-
```
ocr-web-app/
├── app.py                # Flask backend & OCR logic
├── static/
│   ├── uploads/          # Stores uploaded images
│   ├── css/style.css     # Custom styling
│   └── js/script.js      # Interactive features
└── templates/
    ├── base.html         # Main layout
    ├── index.html        # Upload interface
    └── result.html       # Results display
```

🔮 Future Improvements
      PDF text extraction support
      Batch processing for multiple images
      Cloud storage integration (Google Drive/Dropbox)
      AI-powered text correction
      Enhanced language support


📜 License
This project is free to use. If you find it useful, please consider giving credit by linking to my LinkedIn profile.
![](https://www.linkedin.com/in/raj-guru-432680303/)

##Created by Raj Guru
