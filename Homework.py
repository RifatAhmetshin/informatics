import tkinter as tk
from tkinter import filedialog
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get("1.0", tk.END))
def exit_program():
    root.destroy()
root = tk.Tk()
root.title("Текстовый редактор")
text_editor = tk.Text(root)
text_editor.pack()
save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack()
exit_button = tk.Button(root, text="Выход", command=exit_program)
exit_button.pack()
root.mainloop()
