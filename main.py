import tkinter as tk
from tkinter import messagebox
import requests

class SimpleWeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Weather")
        self.root.geometry("350x300")
        
        # API setup (get free key from openweathermap.org)
        self.api_key = "afa96cc18a8aaae4d880c8734c004869"
        
        # Create widgets
        tk.Label(root, text="Enter City:").pack(pady=10)
        self.city_entry = tk.Entry(root, width=25)
        self.city_entry.pack()
        
        tk.Button(root, text="Get Weather", command=self.get_weather).pack(pady=10)
        
        # Weather display
        self.weather_info = tk.Label(root, text="", justify=tk.LEFT)
        self.weather_info.pack(pady=20)
    
    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city")
            return
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if data['cod'] != 200:
                messagebox.showerror("Error", data['message'])
                return
            
            weather_text = (
                f"City: {data['name']}, {data['sys']['country']}\n"
                f"Temperature: {data['main']['temp']}°C\n"
                f"Weather: {data['weather'][0]['description'].title()}\n"
                f"Humidity: {data['main']['humidity']}%\n"
                f"Wind: {data['wind']['speed']} m/s"
            )
            self.weather_info.config(text=weather_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get weather: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleWeatherApp(root)
    root.mainloop()