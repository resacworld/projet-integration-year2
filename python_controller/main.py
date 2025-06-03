import tkinter as tk
import requests

# Function to display the entered text
def start_cmd():
    url = "http://10.7.5.185:8000/api/addmission"
    payload = {
        "status": True
    }

    response = requests.post(url, json=payload)

    print(response.status_code)
    print(response.json())

# Create the main window
root = tk.Tk()
root.title("Basic Tkinter GUI")
root.geometry("300x200")  # Set window size

# Add a start button
button = tk.Button(root, text="Start", command=start_cmd)
button.pack(pady=10, padx=30)

# Run the application
root.mainloop()