import tkinter as tk
from tkinter import messagebox
from scraper import scrape_website

def on_submit():
    url = url_entry.get()
    businesses = scrape_website(url)
    messagebox.showinfo("Scraping Result", '\n\n'.join(str(business) for business in businesses))

# Create the main window
root = tk.Tk()

# Create a label and entry for the URL
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Start the event loop
root.mainloop()
