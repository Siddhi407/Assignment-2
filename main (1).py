import pandas as pd
import os

data_folder = "data"
out_csv = "word_frequencies.csv"

def load_word_frequencies(csv_file):
    """Load word frequencies from CSV into a dictionary."""
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found. Run Assignment 1 first.")
        return None
    
    df = pd.read_csv(csv_file)
    word_frequencies = {}
    
    for _, row in df.iterrows():
        word = row["Word"]
        if word == "TOTAL":  # Skip total row
            continue
        for doc in df.columns[2:]:  # Skip 'Word' and 'Total' columns
            if doc not in word_frequencies:
                word_frequencies[doc] = {}
            word_frequencies[doc][word] = row[doc]
    
    return word_frequencies

def calculate_document_scores(query, word_frequencies):
    """Calculate scores for each document based on query words."""
    query_words = query.lower().split()
    scores = {}
    
    for doc, word_counts in word_frequencies.items():
        score = sum(word_counts.get(word, 0) for word in query_words)
        scores[doc] = score
    
    max_score = max(scores.values(), default=0)
    return [doc for doc, score in scores.items() if score == max_score]

def main():
    print("Loading word frequencies...")
    word_frequencies = load_word_frequencies(out_csv)
    if not word_frequencies:
        return
    
    while True:
        user_query = input("Enter topic words (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            break
        
        matching_docs = calculate_document_scores(user_query, word_frequencies)
        if matching_docs:
            print("Relevant document(s):", ", ".join(matching_docs))
        else:
            print("No matching documents found.")

if __name__ == "__main__":
    main()
