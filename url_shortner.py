'''url shortener desktop application'''
import tkinter as tk
from tkinter import messagebox
import pyshorteners

def url():
    long_url = str(entry.get())
    label.configure(text=str(long_url))
    tiny = pyshorteners.Shortener()
    short_url = tiny.tinyurl.short(long_url)
    messagebox.showinfo(title="shorten successfully", message=short_url)
    
    
windows = tk.Tk()
windows.title("Url Shortener")
windows.geometry("400x300")
windows.configure(bg="indigo")

label = tk.Label(windows, text="Enter the url you want to shortened", bg="indigo", fg="white", font=("helvical", 14))
label.pack(pady=10)
entry= tk.Entry(windows, width=30, bg="indigo", fg="white", font=("helvical", 12))
entry.pack(pady=20)
btn = tk.Button(windows, text="Click To Shorten", command=url, font=("arial", 14))
btn.pack(pady=10)


windows.mainloop()     
    
    

