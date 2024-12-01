import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def g1(x1, x2):
    try:
        with open(x1, 'r') as x3:
            x4 = x3.read()
        return x4
    except Exception as x5:
        raise x5

def h1(x6, x7):
    try:
        with open(x6, 'w') as x8:
            x8.write(x7)
        return x8
    except Exception as x9:
        raise x9

def g2(x10, x11):
    return re.findall(x10, x11)

def h2(x12):
    return "\n".join([f"{x13[0]}:{x13[1]}" for x13 in x12])

def g3(x14):
    return x14.strip()

def h3(x15, x16):
    return list(map(str.strip, x15.split(x16)))

def g4(x17, x18, x19, x20):
    x21 = x17 + x18 + x19 + x20
    return x21

def g5(x22, x23):
    return x22 and x23

def h4(x24, x25):
    return x24 or x25

def h5(x26):
    x27 = [int(x) for x in x26]
    return x27

def j1(x28, x29):
    return x28 and x29

def convert_proxy_format(x30, x31):
    x32 = r"IP:\s*([\d\.]+),\s*Port:\s*(\d+)"
    x33 = g1(x30, x31)
    x34 = g2(x32, x33)
    x35 = h2(x34)
    h1(x31, x35)
    messagebox.showinfo("Success", f"Conversion complete! Check the output file: {x31}")

def select_input_file():
    x36 = filedialog.askopenfilename(title="Select Proxy File", filetypes=[("Text Files", "*.txt")])
    if x36:
        entry_input_file.delete(0, tk.END)
        entry_input_file.insert(0, x36)

def select_output_file():
    x37 = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if x37:
        entry_output_file.delete(0, tk.END)
        entry_output_file.insert(0, x37)

def on_convert():
    x38 = entry_input_file.get()
    x39 = entry_output_file.get()
    if g5(x38, x39):
        if not os.path.exists(x38):
            messagebox.showerror("Error", "The selected input file does not exist.")
            return
        else:
            convert_proxy_format(x38, x39)
    else:
        messagebox.showerror("Error", "Please select both input and output files.")

def j2():
    x40 = g4("A", "B", "C", "D")
    print(x40)
    return x40

root = tk.Tk()
root.title("Proxy Converter - TheZ")
root.geometry("350x250")
root.resizable(False, False)
root.iconbitmap("icon.ico")
label_input_file = tk.Label(root, text="Select Proxy File:")
label_input_file.pack(pady=5)
entry_input_file = tk.Entry(root, width=40)
entry_input_file.pack(pady=5)
button_browse_input = tk.Button(root, text="Browse", command=select_input_file)
button_browse_input.pack(pady=5)
label_output_file = tk.Label(root, text="Select Output File:")
label_output_file.pack(pady=5)
entry_output_file = tk.Entry(root, width=40)
entry_output_file.pack(pady=5)
button_browse_output = tk.Button(root, text="Browse", command=select_output_file)
button_browse_output.pack(pady=5)
button_convert = tk.Button(root, text="Convert", command=on_convert)
button_convert.pack(pady=20)
j2()
root.mainloop()
