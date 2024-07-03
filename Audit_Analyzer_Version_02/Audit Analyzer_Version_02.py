# PMCreative 
# Audit Analyzer Version 02

# Read and Extract Text: Load PDF files and extract text using the PyPDF2 library.
# Keyword Search: Enable users to search for specific keywords within the extracted text and retrieve contextual snippets.
# User Interaction: Provide a graphical user interface (GUI) for easier interaction, allowing users to select PDF files, enter keywords, view results, and save findings.

# Importing Libraries:
# The code uses PyPDF2 for reading PDF files, re for regular expression-based searches,
#  os for file path validation, csv for saving results, and tkinter for the GUI.


import PyPDF2
import re
import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


# Reading the PDF:
# read_pdf(file_path): Reads and extracts text from the specified PDF file using PyPDF2.

def read_pdf(file_path):
    """Read text from a PDF file."""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file {file_path}: {e}")
        return None

# Searching for Keywords:
# search_keyword(text, keyword): Searches for occurrences of a keyword within the extracted text,
#  providing up to 50 characters of context before and after the keyword.

def search_keyword(text, keyword):
    """Search for a keyword in the text and return snippets with context."""
    pattern = re.compile(f'.{{0,50}}{re.escape(keyword)}.{{0,50}}', re.IGNORECASE)
    matches = pattern.findall(text)
    return matches

# Saving Results:
# save_results_to_csv(results, filename): Saves the search results to a CSV file, 
# allowing for easy sharing and further analysis.


def save_results_to_csv(results, filename):
    """Save search results to a CSV file."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Keyword', 'Snippet'])
            for keyword, snippets in results.items():
                for snippet in snippets:
                    writer.writerow([keyword, snippet])
        messagebox.showinfo("Success", f"Results saved to {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving results: {e}")


# GUI Implementation:
# AuditAnalyzerApp Class: Manages the GUI components and integrates the core functionality 
# (file selection, keyword search, displaying results, saving results).

class AuditAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audit Analyzer Version 1")

        self.file_paths = []
        self.results = {}

        self.create_widgets()

    def create_widgets(self):
        self.add_file_button = tk.Button(self.root, text="Add PDF File", command=self.add_file)
        self.add_file_button.pack(pady=5)

        self.file_listbox = tk.Listbox(self.root, width=50, height=10)
        self.file_listbox.pack(pady=5)

        self.keyword_entry = tk.Entry(self.root, width=50)
        self.keyword_entry.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Keyword", command=self.search_keyword)
        self.search_button.pack(pady=5)

        self.result_text = tk.Text(self.root, width=80, height=20, wrap='word')
        self.result_text.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Save Results to CSV", command=self.save_results)
        self.save_button.pack(pady=5)

    def add_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.file_paths.append(file_path)
            self.file_listbox.insert(tk.END, file_path)

    def search_keyword(self):
        keyword = self.keyword_entry.get().strip()
        if not keyword:
            messagebox.showwarning("Input Error", "Please enter a keyword to search.")
            return

        self.result_text.delete(1.0, tk.END)
        self.results[keyword] = []

        for file_path in self.file_paths:
            content = read_pdf(file_path)
            if not content:
                continue

            snippets = search_keyword(content, keyword)
            self.results[keyword].extend(snippets)

            if snippets:
                self.result_text.insert(tk.END, f"\nFound {len(snippets)} snippets containing '{keyword}' in {file_path}:\n")
                for snippet in snippets:
                    self.result_text.insert(tk.END, f"...{snippet}...\n")
            else:
                self.result_text.insert(tk.END, f"\nNo snippets found containing '{keyword}' in {file_path}.\n")

    def save_results(self):
        if not self.results:
            messagebox.showwarning("No Results", "No search results to save.")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            save_results_to_csv(self.results, filename)

# Main Function: Initializes the Tkinter GUI and runs the application.

def main():
    root = tk.Tk()
    app = AuditAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
