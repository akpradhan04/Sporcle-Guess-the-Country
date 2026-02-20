import time
import json
import tkinter as tk
import config


class CountriesGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(config.WINDOW_TITLE)

        self.start_time = time.time()

        self.countries_data = self.load_countries()
        self.countries_lookup = self.build_lookup()

        self.setup_ui()

        self.root.mainloop()

    def load_countries(self):
        with open('countries.json', 'r', encoding = 'utf-8') as file:
            return json.load(file)
        
    def build_lookup(self):
        countries_lookup = {}

        for country in self.countries_data:
            accepted_country_name = country["name"]

            # Official Country Name
            countries_lookup[accepted_country_name.lower()] = accepted_country_name

            # Country Alias
            for alias in country["aliases"]:
                countries_lookup[alias.lower()] = accepted_country_name

        return countries_lookup
    
    def setup_ui(self):
        self.counter_label = tk.Label(
            self.root,
            text=f"0 / {len(self.countries_data)}",
            font=("Arial", 16)
        )
        self.counter_label.pack()

        self.timer_label = tk.Label(self.root, font=("Arial", 16))
        self.timer_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 14), width=40)
        self.entry.pack()
        self.entry.focus()

        self.listbox = tk.Listbox(self.root, width=50, height=20)
        self.listbox.pack()


if __name__ == "__main__":
    game = CountriesGame()