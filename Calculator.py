import tkinter as tk
from tkinter import messagebox


def Button12():
    try:
        result = entry.get()
        if result != None:
            result = eval(result)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
    except:
        messagebox.showinfo("Eror", "The value entered is invalid")


root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.config(bg="#828282")

entry = tk.Entry(root, bg="#3E4248", fg="white", justify="right",
                 width=18, borderwidth=5, font=("arial", 20))
entry.grid(row=0, column=0, columnspan=4)

button19 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, "**"), text="x^y", font=("arial", 18), width=4, fg="white")
button19.grid(row=1, column=0,)

button18 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, "("), text="(", font=("arial", 18), width=4, fg="white")
button18.grid(row=1, column=1)

button17 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, ")"), text=")", font=("arial", 18), width=4, fg="white")
button17.grid(row=1, column=2)

button16 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.delete(
    0, tk.END), text="C", font=("arial", 18), width=4, fg="white")
button16.grid(row=1, column=3)

button15 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 7), text="7", font=("arial", 18), width=4)
button15.grid(row=2, column=0)

button14 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 8), text="8", font=("arial", 18), width=4)
button14.grid(row=2, column=1)

button13 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 9), text="9", font=("arial", 18), width=4)
button13.grid(row=2, column=2)

button12 = tk.Button(root, borderwidth=4, bg="#3E4248", command=Button12, text="=", font=(
    "arial", 18), width=4, fg="white")
button12.grid(row=2, column=3)

button11 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 4), text="4", font=("arial", 18), width=4)
button11.grid(row=3, column=0)

button10 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 5), text="5", font=("arial", 18), width=4)
button10.grid(row=3, column=1)

button9 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 6), text="6", font=("arial", 18), width=4)
button9.grid(row=3, column=2)

button8 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, "+"), text="+", font=("arial", 18), width=4, fg="white")
button8.grid(row=3, column=3)


button7 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 1), text="1", font=("arial", 18), width=4)
button7.grid(row=4, column=0)

button6 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 2), text="2", font=("arial", 18), width=4)
button6.grid(row=4, column=1)

button5 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 3), text="3", font=("arial", 18), width=4)
button5.grid(row=4, column=2)

button4 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, "-"), text="-", font=("arial", 18), width=4, fg="white")
button4.grid(row=4, column=3)

button3 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, 0), text="0", font=("arial", 18), width=4)
button3.grid(row=5, column=0)


button2 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, "."), text=".", font=("arial", 18), width=4, fg="white")
button2.grid(row=5, column=1)

button1 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, "/"), text="/", font=("arial", 18), width=4, fg="white")
button1.grid(row=5, column=2)

button0 = tk.Button(root, borderwidth=4, bg="#3E4248", command=lambda: entry.insert(
    tk.END, "*"), text="x", font=("arial", 18), width=4, fg="white")
button0.grid(row=5, column=3)
root.mainloop()
