# 📄 PDF Rearranger

## Introduction

PDF Rearranger is a lightweight web application built with Flask that allows users to upload a PDF, visually preview its pages, and rearrange them using a simple drag-and-drop interface.

---

## 🚀 Features

* Upload PDF files directly from the browser
* Automatic page-to-image preview generation
* Drag-and-drop interface for page reordering (powered by SortableJS)
* Custom page ordering handled dynamically
* Instant download of rearranged PDF
* Simple and responsive UI
* Error handling for invalid inputs

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **PDF Processing:** PyMuPDF (`fitz`)
* **Frontend:** HTML, CSS, JavaScript
* **Library:** SortableJS (for drag-and-drop functionality)

---

## 📂 Project Structure

```
project/
│
├── app.py
├── uploads/
├── static/
│   └── previews/
├── templates/
│   ├── index.html
│   └── rearrange.html
```

---

## ⚙️ How It Works

1. User uploads a PDF file
2. Backend processes the file using PyMuPDF
3. Each page is converted into a preview image
4. Images are displayed in a draggable grid layout
5. User rearranges pages via drag-and-drop
6. New order is captured and sent to the backend
7. A new PDF is generated and returned for download

---

## 📸 Screenshots

<img width="1356" height="885" alt="1" src="https://github.com/user-attachments/assets/1413c1e1-c1be-4cca-b878-4280d8829de4" />

<img width="1356" height="885" alt="2" src="https://github.com/user-attachments/assets/0097adf9-60a2-47f5-88ff-2f834ac0a1e6" />

<img width="1356" height="885" alt="3" src="https://github.com/user-attachments/assets/19c3519f-3578-4bde-add3-efde352093ce" />

<img width="1245" height="773" alt="4" src="https://github.com/user-attachments/assets/a8067f34-ca8c-4a11-9407-7349bc8de9d0" />

<img width="1358" height="885" alt="5" src="https://github.com/user-attachments/assets/bdb4c140-4d73-4611-a815-f2112905fc60" />

---

## ▶️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/owacez/PDF-Rearranger.git
cd PDF-Rearranger
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install flask pymupdf
```

### 4. Run the App

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000/
```

---

## ⚠️ Notes

* Only PDF files are supported
* Page numbering starts from **1**
* Output file (`output.pdf`) is overwritten on each request
* Preview images are low-resolution for performance

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Flask for backend simplicity
* PyMuPDF for efficient PDF processing
* SortableJS for drag-and-drop functionality

---
