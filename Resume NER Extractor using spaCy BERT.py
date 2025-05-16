import fitz  # PyMuPDF
import spacy
import re

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

# Step 1: Extract text from PDF resume
# ------------------------------------
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text



# Step 2: Extract Email, Phone, Skills
# ------------------------------------
def extract_email(text):
    return re.findall(r'\S+@\S+', text)

def extract_phone(text):
    return re.findall(r'\+?\d[\d\s\-\(\)]{8,}\d', text)

SKILLS_DB = ['python', 'java', 'sql', 'machine learning', 'nlp', 'deep learning', 'data analysis']

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS_DB if skill in text]


# Step 3: Extract Named Entities using spaCy
# ------------------------------------
def extract_entities(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        entities[ent.label_] = entities.get(ent.label_, set())
        entities[ent.label_].add(ent.text)
    return entities



# MAIN Function
# ------------------------------------
if __name__ == "__main__":
    file_path = "C:\\Users\\Vaibhav Singh\\OneDrive\\try_docement.pdf"



print("Reading Resume...")
resume_text = extract_text_from_pdf(file_path)




print("\n✅ Email(s):", extract_email(resume_text))
print("✅ Phone(s):", extract_phone(resume_text))
print("✅ Skills:", extract_skills(resume_text))


print("\n🔍 Named Entities (NER):")
entities = extract_entities(resume_text)
for label, values in entities.items():
    print(f"{label}: {list(values)}")
    