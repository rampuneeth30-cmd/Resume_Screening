# 📄 Resume Parser (Flask + NLP)

This project is a **Resume Parser Web Application** built with **Flask**.
It allows users to upload a resume in **PDF format** and automatically extracts key details such as:

* 👤 **Name**
* 📧 **Email Address**
* 📞 **Phone Number**
* 💡 **Skills**

The application leverages **Regex, NLTK (Natural Language Toolkit), and keyword matching** for accurate information extraction.

---

## ✨ Features

* 📂 Upload resumes in **PDF format**
* 🔎 Extracts **Name, Email, Phone, and Skills**
* 📊 Uses **NLP (NLTK)** for name detection
* 🧠 Detects skills from predefined skill keywords (expandable)
* 🌐 Simple and clean **Flask-based web interface**

---

## 📂 Project Structure

```
.
├── app.py               # Flask application (main entry point)
├── templates/
│   └── index.html       # Frontend template
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-parser.git
cd resume-parser
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The app will start in development mode and can be accessed at:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📦 Dependencies

* **Flask** – Web framework
* **pdfplumber** – PDF text extraction
* **NLTK** – Natural Language Processing for name detection
* **re (Regex)** – Pattern matching for emails and phone numbers

Install via:

```bash
pip install flask pdfplumber nltk
```

---

## ⚙️ How It Works

1. Upload a **resume PDF** through the web interface.
2. The app extracts raw text using **pdfplumber**.
3. **Regex + NLP** methods extract candidate details.
4. Extracted info is displayed on the webpage.

---

## 🚀 Example Output

**Input:** Resume.pdf (containing candidate details)

**Output on Webpage:**

```
Name: John Doe
Email: john.doe@example.com
Phone: +919876543210
Skills: Python, Data Science, Machine Learning
```

---

## 🔮 Future Improvements

* Support for **DOCX resumes**
* Expand **skills database** with AI-driven skill detection
* Add **work experience** and **education extraction**
* Integration with **databases (MongoDB/MySQL)** for storage

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to improve parsing accuracy or add new features, feel free to contribute.

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use and modify it.

