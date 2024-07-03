# PMCreative 
# Audit Analyzer Version 01

# PyPDF2: For reading and extracting text from PDF files.
# re: For performing regular expression-based searches.
# os: For file path validation.

import PyPDF2
import re
import os

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def search_keyword(text, keyword):
    pattern = re.compile(f'.{{0,50}}{re.escape(keyword)}.{{0,50}}', re.IGNORECASE)
    matches = pattern.findall(text)
    return matches

# Main Function
# The main function ties everything together. It prompts the user to enter the path to the PDF file
# validates the file path, reads the PDF content, and enters a loop to search for keywords.

def main():
    # Get the PDF file path
    while True:
        file_path = input("Enter the path to your PDF file: ")
        if os.path.exists(file_path) and file_path.lower().endswith('.pdf'):
            break
        print("Invalid file path. Please enter a valid PDF file path.")

    # Read the PDF
    # The read_pdf function takes the file path of a PDF, reads its content, and returns the extracted text.  
    # This function uses PyPDF2 to iterate through each page of the PDF and concatenate the text into a single string. 


    print("Reading PDF...")
    content = read_pdf(file_path)
    print("PDF read successfully.")

    # Search for keywords
    # The search_keyword function searches for occurrences of a keyword within the extracted text. 
    # It uses regular expressions to find matches, allowing for up to 50 characters of context before and after the keyword. 

    while True:
        keyword = input("Enter a keyword to search (or 'quit' to exit): ")
        if keyword.lower() == 'quit':
            break

        snippets = search_keyword(content, keyword)

        if snippets:
            print(f"\nFound {len(snippets)} snippets containing '{keyword}':")
            for i, snippet in enumerate(snippets, 1):
                print(f"{i}. ...{snippet}...")
        else:
            print(f"No snippets found containing '{keyword}'.")
        print()

if __name__ == "__main__":
    main()