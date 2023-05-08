import tkinter as tk
root = tk.Tk()

def change_text():
    name = entry.get()
    label.config(text="Witaj " + name)

root.geometry("800x600")
root.title("Book Store")
root.iconbitmap("./bookshelf.ico")


left_frame = tk.Frame(root, borderwidth=4, relief="ridge", width=200, height=150)
left_frame.pack(side="left",padx=10, pady=10)
left_frame.pack_propagate(0)

right_frame = tk.Frame(root,width=200, height=left_frame["height"],borderwidth=4, relief="ridge")
right_frame.pack(side="right",padx=10, pady=10)
right_frame.pack_propagate(0)

label = tk.Label(right_frame, text="Podaj imie i nazwisko")
label.pack()

entry = tk.Entry(left_frame)
entry.pack(anchor="w", padx=10, pady=10)

button = tk.Button(left_frame, text="Click Me!", command=change_text)
button.pack()

root.resizable(width=False, height=False)

radio_var = tk.StringVar(value="RadioButton1")

radio_button1 = tk.Radiobutton(left_frame, text="Tester", variable=radio_var, value="tester")
radio_button1.pack(anchor="w", padx=10, pady=10)

radio_button2 = tk.Radiobutton(left_frame, text="Programista", variable=radio_var, value="programista")
radio_button2.pack(anchor="w", padx=10, pady=10)

root.mainloop()