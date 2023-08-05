import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

stamps_list = []
stamps_directory = ""

# simple script to add some stamps to ur html :33

def browse_stamps_directory():
    global stamps_directory, stamps_list
    stamps_directory = filedialog.askdirectory()

    project_root = os.path.abspath(os.path.dirname(__file__))
    relative_stamps_directory = os.path.relpath(stamps_directory, project_root)

    stamps_dir.set(relative_stamps_directory)

    stamps_list = [filename for filename in os.listdir(stamps_directory) if os.path.isfile(os.path.join(stamps_directory, filename))]

    status_label.config(text=f"Stamps directory selected: {relative_stamps_directory}")

    stamps_directory = relative_stamps_directory

def browse_html_file():
	html_file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
	selected_html_file.set(html_file_path)
	status_label.config(text=f"HTML file selected: {html_file_path}")

def generate_stamps_div(stamps_list):
	stamps_div = '\n<div class="stamps">\n'
	
	for stamp_filename in stamps_list:
		stamps_div += f'\t<img src="{stamps_directory}/{stamp_filename}">\n'
	
	stamps_div += '</div>\n'
	return stamps_div

def add_stamps_to_html():
	stamps_div = generate_stamps_div(stamps_list)
	html_file_path = selected_html_file.get()
	
	try:
		with open(html_file_path, 'a') as html_file:
			html_file.write(stamps_div)
		messagebox.showinfo("Success", "Stamps added to HTML file!")
	except Exception as e:
		messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI Mainloop

root = tk.Tk()
root.title("Stamps HTML Generator")

stamps_dir = tk.StringVar()

instructions_label = tk.Label(root, text="Select the stamps directory")
instructions_label.pack()

stamps_button = tk.Button(root, text="Browse Stamps Directory", command=browse_stamps_directory)
stamps_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

instructions_label = tk.Label(root, text="Select the HTML file to update")
instructions_label.pack()

selected_html_file = tk.StringVar()
html_button = tk.Button(root, text="Browse HTML File", command=browse_html_file)
html_button.pack()

start_button = tk.Button(root, text="Start", command=add_stamps_to_html)
start_button.pack()

root.mainloop()