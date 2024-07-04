# PMCreative_PinkTranscriptEditor
#  User-friendly  application designed to assist users in cleaning up text transcripts.

# How to Use
# Run the Application:
# Input Text:
# Remove All Numbers:
# Remove Specific Characters/Words:
# Save the Cleaned Text:

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, filedialog


# Function to remove all numbers from the input text

def remove_numbers():
    text = input_text.get("1.0", tk.END)
    cleaned_text = ''.join([i for i in text if not i.isdigit()])
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, cleaned_text)

# Function to remove specific characters, letters, or words from the input text

def remove_specific():
    text = input_text.get("1.0", tk.END)
    specific_to_remove = specific_entry.get()
    cleaned_text = text
    
    # Remove specific numbers, letters, or words
   
    if specific_to_remove:
        if specific_to_remove.isdigit():  # If the input is numbers
            cleaned_text = ''.join([i for i in text if i not in specific_to_remove])
        elif all(c.isalpha() or c.isspace() for c in specific_to_remove):  # If the input is letters or words
            words_to_remove = specific_to_remove.split(',')
            for word in words_to_remove:
                cleaned_text = cleaned_text.replace(word.strip(), '')
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, cleaned_text)

# Function to save the cleaned text to a file

def save_output():
    cleaned_text = output_text.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(cleaned_text)

# Create the main window
window = tk.Tk()
window.title("Pink Transcript Cleaner")

# Set window size and background color
window.geometry("600x500")
window.configure(bg='#FFD2D3')

# Create a style for the widgets

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=('calibri', 12), padding=10, background='#E2A3AA', foreground='#372C2F')
style.configure("TLabel", font=('calibri', 12), background='#EDC5C8')
style.configure("TEntry", font=('calibri', 12))
style.configure("TFrame", background='#EDC5C9')

# Create the main frame to hold all widgets

main_frame = ttk.Frame(window, padding="10 10 10 10", style="TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)

# Create the input text area with a label

input_label = ttk.Label(main_frame, text="Input Text", style="TLabel")
input_label.pack(anchor='w')
input_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=60, height=10, bg='#FFF7F6')
input_text.pack(pady=5)

# Create the specific input field with a label for characters or words to remove

specific_label = ttk.Label(main_frame, text="Specific Characters/Words to Remove (comma separated for words)", style="TLabel")
specific_label.pack(anchor='w', pady=(10, 0))
specific_entry = ttk.Entry(main_frame, width=50, font=('calibri', 12))
specific_entry.pack(pady=5)

# Create the frame for the action buttons

button_frame = ttk.Frame(main_frame, style="TFrame")
button_frame.pack(pady=10)

# Create the "Remove All Numbers" button

remove_all_button = ttk.Button(button_frame, text="Remove All Numbers", command=remove_numbers, style="TButton")
remove_all_button.grid(row=0, column=0, padx=5)

# Create the "Remove Specific" button

remove_specific_button = ttk.Button(button_frame, text="Remove Specific", command=remove_specific, style="TButton")
remove_specific_button.grid(row=0, column=1, padx=5)

# Create the "Save Output" button

save_button = ttk.Button(button_frame, text="Save Output", command=save_output, style="TButton")
save_button.grid(row=0, column=2, padx=5)

# Create the output text area with a label

output_label = ttk.Label(main_frame, text="Output Text", style="TLabel")
output_label.pack(anchor='w', pady=(10, 0))
output_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=60, height=10, bg='#FFF7F6')
output_text.pack(pady=5)

# Start the Tkinter event loop to run the application

window.mainloop()
