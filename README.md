# README - Assignment 2: NLP Query Documents

## **1. OS Platform / Environment**
This program is designed to run on:
- **Operating System:** Windows, Linux, or macOS
- **Python Version:** 3.x
- **Required Libraries:** PyPDF2, pandas, collections, re

## **2. Project Structure**
The project follows this folder structure:
```
project-folder/
│-- data/               # Folder containing input PDF documents
│-- word_frequencies.csv # Generated CSV file with word frequencies
│-- query_processor.py  # Main Python script to process queries
│-- README.md           # Documentation file
```

## **3. Commands to Install & Execute Program**
### Install Required Dependencies:
```bash
pip install PyPDF2 pandas
```
### Run the Program:
```bash
python query_processor.py
```

## **4. Vocabulary Management Strategy**
- **Stop Word Removal:** The program removes common English stop words (e.g., "the", "and", "is").
- **Prioritized Words:** Only meaningful words (nouns, verbs) are considered for ranking.
- **Curation Strategy:**
  - Extracts text from PDFs and tokenizes it.
  - Filters out non-informative words.
  - Uses word frequencies to rank documents based on relevance.

## **5. Query Processing & Ranking**
- The user enters topic words.
- The program calculates document relevance based on word probability.
- The document(s) with the highest score are displayed.

## **6. User Interaction**
- The program prompts the user for input.
- Allows multiple queries until the user exits.
- Provides clear messages when no matches are found.

---
### **Submission:**
- Submit a zip file containing `query_processor.py` and `README.md`.
- Ensure all paths in code are relative to the project folder.

