from flask import Flask, render_template, request
import pdfplumber
import nltk
import re

# Download NLTK's named entity recognition model (Only needed once)
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")

app = Flask(__name__)

# Common false-positive words (locations, addresses)
location_keywords = {"nagar", "street", "road", "block", "village", "town", "city", "district", "state", "india"}
common_names = {"rajesh", "pavan", "anand", "arjun", "suresh", "priya", "deepa"}  # Expandable
skill_keywords = {"Python", "Java", "C++", "Machine Learning", "AI", "Data Science", "Communication", "Time Management", "Leadership"}

def extract_text_from_pdf(file):
    """Extracts text from PDF using pdfplumber."""
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_name(text):
    """Extracts the name from the resume using regex, layout structure, and NLTK."""
    lines = text.split("\n")
    first_5_lines = " ".join(lines[:5])  # Look at only the top section

    # Try regex-based name extraction (First word is Capitalized)
    name_match = re.search(r"^([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)", first_5_lines)
    if name_match:
        name = name_match.group(1)
        if name.lower() not in location_keywords and name.lower() not in common_names:
            return name

    # Use NLTK POS tagging to find Proper Nouns (NNP)
    words = nltk.word_tokenize(first_5_lines)
    pos_tags = nltk.pos_tag(words)
    
    possible_names = [word for word, tag in pos_tags if tag == "NNP" and word.lower() not in location_keywords]

    if possible_names:
        return " ".join(possible_names[:2])  # Take the first two words (First Name + Last Name)

    return "N/A"

def extract_email(text):
    """Extracts email from resume text using regex."""
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return email_match.group(0) if email_match else "N/A"

def extract_phone(text):
    """Extracts phone number using regex."""
    phone_match = re.search(r"\+?\d{10,15}", text)
    return phone_match.group(0) if phone_match else "N/A"

def extract_skills(text):
    """Extracts skills from predefined keywords."""
    found_skills = {skill for skill in skill_keywords if skill.lower() in text.lower()}
    return ", ".join(found_skills) if found_skills else "N/A"

def extract_details_from_pdf(file):
    """Extracts all resume details."""
    text = extract_text_from_pdf(file)

    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    return name, email, phone, skills

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return 'No file part'
        file = request.files['resume']
        if file.filename == '':
            return 'No selected file'

        # Parse the PDF for details
        name, email, phone, skills = extract_details_from_pdf(file)

        return render_template('index.html', name=name, email=email, phone=phone, skills=skills)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
