#Student Name : ABID NAWAZ
#Roll Number : F21BSEEN1E02032
#Project Name : Assets Life Time 
#creating a assets life time project for assets management

import tkinter as tk
from tkinter import messagebox

class Asset:
    def __init__(self, name, purchase_date, lifespan):
        self.name = name
        self.purchase_date = purchase_date
        self.lifespan = lifespan

    def calculate_remaining_lifetime(self, current_date):
        purchase_year = int(self.purchase_date.split('-')[0])
        current_year = int(current_date.split('-')[0])
        remaining_years = self.lifespan - (current_year - purchase_year)
        return remaining_years if remaining_years > 0 else 0

class AssetManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Asset Management")

        self.assets = []
        self.current_date = "2023-12-02"

        self.name_label = tk.Label(root, text="Asset Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.purchase_label = tk.Label(root, text="Purchase Date (YYYY-MM-DD):")
        self.purchase_label.pack()
        self.purchase_entry = tk.Entry(root)
        self.purchase_entry.pack()

        self.lifespan_label = tk.Label(root, text="Lifespan (in years):")
        self.lifespan_label.pack()
        self.lifespan_entry = tk.Entry(root)
        self.lifespan_entry.pack()

        self.add_button = tk.Button(root, text="Add Asset", command=self.add_asset)
        self.add_button.pack()

        self.display_button = tk.Button(root, text="Display Assets", command=self.display_assets)
        self.display_button.pack()

    def add_asset(self):
        name = self.name_entry.get()
        purchase_date = self.purchase_entry.get()
        lifespan = int(self.lifespan_entry.get())

        new_asset = Asset(name, purchase_date, lifespan)
        self.assets.append(new_asset)
        messagebox.showinfo("Success", "Asset added successfully!")

    def display_assets(self):
        display_text = "Assets:\n"
        for asset in self.assets:
            remaining_lifetime = asset.calculate_remaining_lifetime(self.current_date)
            display_text += f"Name: {asset.name}, Purchase Date: {asset.purchase_date}, Remaining Lifetime: {remaining_lifetime} years\n"
        messagebox.showinfo("Asset Details", display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssetManagerApp(root)
    root.mainloop()
