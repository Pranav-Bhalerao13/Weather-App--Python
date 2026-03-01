import tkinter
import requests
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling images

def get_weather():
    """ Fetch weather details from OpenWeatherMap API and update the UI."""
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    api_key = ""  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found!")
            return

        # Extract weather details
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"].lower()  # Convert to lowercase
        humidity = data["main"]["humidity"]

        # Update the result label
        result_label.config(
            text=f"City: {city}\nTemperature: {temperature}°C\nWeather: {weather_desc}\nHumidity: {humidity}%",
            bg="white", fg="black"
        )

        # Change background image based on weather condition
        change_background(weather_desc)

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Failed to retrieve weather data")

def change_background(weather_desc):
    """Change background image based on weather condition."""
    global bg_photo  # Ensure we use the global variable

    # Define image paths for different weather conditions
    if "cloud" in weather_desc:
        image_path = r"C:\Users\dell\Downloads\cloudy.jpg"
    elif "rain" in weather_desc:
        image_path = r"C:\Users\dell\Downloads\rainy.jpg"
    elif "clear" in weather_desc:
        image_path = r"C:\Users\dell\Downloads\sunny.jpg"
    elif "smoky" in weather_desc:
        image_path = r"C:\Users\dell\Downloads\smoky.jpg"
    elif "haze" in weather_desc:
        image_path = r"C:\Users\dell\Downloads\haze.jpg"
    else:
        image_path = r"C:\Users\dell\Downloads\default.jpg"  # Default image

    # Load new image
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((2000,1500))  # Resize image
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Update canvas background
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.image = bg_photo  # Keep reference to avoid garbage collection

# Create GUI window
root = tkinter.Tk()
root.title("Weather App")
root.geometry("700x600")

# Load and set default background image
default_image_path = r"C:\Users\dell\Downloads\default.jpg"
bg_image = Image.open(default_image_path)
bg_image = bg_image.resize((700, 600))  # Resize image to match window size
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tkinter.Canvas(root, width=700, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create a frame for UI elements
frame = tkinter.Frame(root, bg="white", bd=5)
frame.place(relx=0.5, rely=0.1, anchor="n")  # Center the frame at the top




# UI Elements (aligned using grid)
city_label = tkinter.Label(frame, text="Enter City:", font=("Arial", 14, "bold"), bg="white", fg="black")
city_label.grid(row=0, column=0, padx=10, pady=5)

city_entry = tkinter.Entry(frame, font=("Arial", 14))
city_entry.grid(row=0, column=1, padx=10, pady=5)

search_button = tkinter.Button(frame, text="Get Weather", font=("Arial", 14, "bold"), command=get_weather, bg="#3498db", fg="white")
search_button.grid(row=0, column=2, padx=10, pady=5)

# Result Label (placed below the input area)
result_label = tkinter.Label(root, text="", font=("Arial", 14), justify="left", bg="white", fg="black")
result_label.place(relx=0.5, rely=0.3, anchor="n", width=400, height=150)

# Start the main event loop
root.mainloop()

