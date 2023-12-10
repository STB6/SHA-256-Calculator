import tkinter
import tkinter.ttk
import hashlib
import ctypes
import os


def toggle_password(entry, button):
    if entry.cget("show") == "*":
        entry.config(show="")
        button.config(text="Hide")
    else:
        entry.config(show="*")
        button.config(text="Show")


def calculate_sha256():
    if entry1.get() == entry2.get():
        sha_signature = hashlib.sha256(entry1.get().encode()).hexdigest()
        entry3.config(state="normal")
        entry3.delete(0, "end")
        entry3.insert(0, sha_signature)
        style.configure("TEntry", foreground="black")
        entry3.config(state="readonly")
    else:
        entry3.config(state="normal")
        entry3.delete(0, "end")
        entry3.insert(0, "Contents do not match!")
        style.configure("TEntry", foreground="red")
        entry3.config(state="readonly")


root = tkinter.Tk()
style = tkinter.ttk.Style()
root.title("SHA-256 Calculator")

if os.name == 'nt':
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.call('tk', 'scaling', ScaleFactor/70)


entry1 = tkinter.ttk.Entry(root, show="*", width=64, justify="center")
entry1.grid(row=0, column=0)
button1 = tkinter.ttk.Button(root, text="Show", command=lambda: toggle_password(entry1, button1), width=5)
button1.grid(row=0, column=1)

entry2 = tkinter.ttk.Entry(root, show="*", width=64, justify="center")
entry2.grid(row=1, column=0)
button2 = tkinter.ttk.Button(root, text="Show", command=lambda: toggle_password(entry2, button2), width=5)
button2.grid(row=1, column=1)

button3 = tkinter.ttk.Button(root, text="Calculate SHA-256", command=calculate_sha256, width=20)
button3.grid(row=2, column=0, columnspan=2)

entry3 = tkinter.ttk.Entry(root, show="*", width=64, justify="center", state="readonly")
entry3.grid(row=3, column=0)
button4 = tkinter.ttk.Button(root, text="Show", command=lambda: toggle_password(entry3, button4), width=5)
button4.grid(row=3, column=1)

button5 = tkinter.ttk.Button(
    root,
    text="Copy",
    command=lambda: root.clipboard_clear() or root.clipboard_append(entry3.get()) if entry3.get() != "" else None,
    width=10,
)
button5.grid(row=4, column=0, columnspan=2)


root.resizable(False, False)
root.mainloop()
