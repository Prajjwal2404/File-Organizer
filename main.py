import tkinter as tk
from file_organize import organize_files

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x180")
root.resizable(0, 0)


label = tk.Label(root, 
                 text="Enter Directory Path",
                 font=("Helvetica", 16),
                 fg="black",
                 padx=10,
                 pady=10)

label.pack()

entry = tk.Entry(root,
                 font=("Arial", 14),
                 fg="black",
                 bg="lightgrey")

entry.pack(pady=10)

def on_button_click():
    feedback_text = organize_files(entry.get())
    label.config(text=feedback_text)

button = tk.Button(root, 
                   text="Submit",
                   font=("Arial", 14),
                   fg="white",
                   bg="green", 
                   activebackground="lightgreen",
                   command=on_button_click)


button.pack(pady=20)

root.mainloop()