import tkinter as tk
from tkinter import filedialog, messagebox

from organizer import organize_folder


selected_folder = ""


def browse_folder():
    global selected_folder

    selected_folder = filedialog.askdirectory()

    if selected_folder:
        folder_label.config(
            text=selected_folder
        )


def organize():
    if not selected_folder:

        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )

        return

    organize_folder(selected_folder)

    log_box.insert(
        tk.END,
        f"✔ Organized: {selected_folder}\n"
    )

    messagebox.showinfo(
        "Success",
        "Files organized successfully."
    )


def start_app():

    window = tk.Tk()
    window.iconbitmap("C:\\Users\\DeLL\\Desktop\\AI_Learning\\File_Organizer\\documentation.ico")

    window.title("Smart File Organizer")
    window.geometry("800x600")

    title_label = tk.Label(
        window,
        text="Smart File Organizer",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=20)

    browse_button = tk.Button(
        window,
        text="Browse Folder",
        width=20,
        command=browse_folder
    )

    browse_button.pack(pady=10)

    global folder_label

    folder_label = tk.Label(
        window,
        text="No folder selected"
    )

    folder_label.pack()

    organize_button = tk.Button(
        window,
        text="Organize Files",
        width=20,
        command=organize
    )

    organize_button.pack(pady=15)

    tk.Label(
        window,
        text="Activity Log"
    ).pack()

    global log_box

    log_box = tk.Text(
        window,
        height=15,
        width=80
    )

    log_box.pack(pady=10)

    window.mainloop()