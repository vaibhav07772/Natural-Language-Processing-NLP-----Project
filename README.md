# Natural-Language-Processing-NLP-----Project
Resume NER Extractor using spacy BERT

## Overview
This project extracts key information like Name, Email, Phone, Skills, Education, Experience, and more from resumes using Named Entity Recognition (NER). It combines the power of spaCy’s NER pipeline with BERT-based embeddings to improve entity extraction accuracy, especially in unstructured resume formats.

## Key Features
- Extracts named entities from raw resume text.
- Custom NER training/fine-tuning using spaCy and contextual features from BERT.
- Handles noisy and diverse resume formats (PDF, DOCX, or plain text).
- Outputs structured JSON/CSV for downstream processing or analytics.

## Technologies Used
- Python
- spaCy (Custom NER Pipeline)
- Transformers (BERT for embeddings)
- PyMuPDF / docx2txt (for resume parsing)

## Use Case
Useful for automating resume parsing in HR systems, ATS software, or recruitment platforms to extract structured data for filtering, analytics, or machine learning applications.
