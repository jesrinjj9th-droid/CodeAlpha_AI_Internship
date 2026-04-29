import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator
import pyperclip

def perform_translation():
    text_to_translate = input_box.get("1.0", tk.END).strip()
    if not text_to_translate:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    try:
        source = src_lang_entry.get().lower()
        target = tgt_lang_entry.get().lower()
        translated = GoogleTranslator(source=source, target=target).translate(text_to_translate)

        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)
        output_box.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Could not translate: {e}")

def copy_text():
    content = output_box.get("1.0", tk.END).strip()
    if content:
        pyperclip.copy(content)
        messagebox.showinfo("Success", "Copied to clipboard!")

root = tk.Tk()
root.title("AI Translator")
root.geometry("500x500")

tk.Label(root, text="Source (e.g. auto, en):").pack()
src_lang_entry = tk.Entry(root, justify='center')
src_lang_entry.insert(0, "auto")
src_lang_entry.pack()

tk.Label(root, text="Target (e.g. es, fr, hi):").pack()
tgt_lang_entry = tk.Entry(root, justify='center')
tgt_lang_entry.insert(0, "es")
tgt_lang_entry.pack()

input_box = tk.Text(root, height=8, width=50)
input_box.pack(pady=10)

tk.Button(root, text="TRANSLATE", command=perform_translation, bg="green", fg="white").pack()

output_box = tk.Text(root, height=8, width=50, state=tk.DISABLED, bg="#f0f0f0")
output_box.pack(pady=10)

tk.Button(root, text="Copy", command=copy_text).pack()

root.mainloop()