import pandas as pd
from sentence_transformers import SentenceTransformer
import json


def load_xls_file(file_path):
    """
    Load an Excel file, read every row and column,
    convert each row into a string, and generate its embedding.
    Returns a list of tuples: (row_text, metadata, embedding).
    """
    # Read the Excel file
    df = pd.read_excel(file_path)
    # Initialize the embedding model (ensure this model is also used elsewhere for consistency)
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    results = []
    
    # Iterate through each row in the DataFrame
    for idx, row in df.iterrows():
        # Join all cell values (converted to string) using a separator (here using " | ")
        row_text = " | ".join([str(cell) for cell in row.values])
        
        # Check if there is non-empty text
        if row_text.strip():
            # Generate an embedding for the row text
            embedding = model.encode(row_text).tolist()
            # Create metadata to help trace the source of the data
            metadata = {
                "source": file_path,
                "row_index": idx,
                "columns": list(df.columns)
            }
            results.append((row_text, json.dumps(metadata), embedding))
    
    return results

def process_xls_files(xls_files):
    # Process all Excel files
    all_xls_results = []
    for file_path in xls_files:
        xls_results = load_xls_file(file_path)
        all_xls_results.extend(xls_results)
    return all_xls_results

