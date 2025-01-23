import os
import subprocess
from tkinter import Tk, StringVar, Entry, Label, filedialog, messagebox
from customtkinter import CTk, CTkButton

# Function to select the download location
def select_location():
    location = filedialog.askdirectory()
    if location:
        download_location.set(location)

# Function to download the video using yt-dlp
def download_video(video_url):
    if not video_url.strip():
        messagebox.showerror("Error", "Please enter a valid YouTube URL!")
        return
    
    location = download_location.get() or os.getcwd()
    
    try:
        # Run yt-dlp subprocess to download the video
        subprocess.run(
            [
                "yt-dlp",
                "-o", f"{location}/%(title)s.%(ext)s",
                video_url,
            ],
            check=True,
        )
        messagebox.showinfo("Success", f"Video downloaded successfully to {location}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
def main():
    # Initialize the Tkinter root window
    root = CTk()
    root.title("YouTube Video Downloader")
    root.geometry("500x200")

    # Create the StringVar after initializing the root window
    global download_location
    download_location = StringVar()

    # Title Label
    Label(root, text="YouTube Video Downloader", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    # URL Entry Field
    Label(root, text="Video URL:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    url_entry = Entry(root, width=40)
    url_entry.grid(row=1, column=1, padx=10, pady=5)

    # Download Location Selector
    Label(root, text="Save to:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    location_button = CTkButton(root, text="Select Location", command=select_location)
    location_button.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # Download Button
    download_button = CTkButton(
        root,
        text="Download",
        command=lambda: download_video(url_entry.get()),
    )
    download_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Run the Tkinter loop
    root.mainloop()

if __name__ == "__main__":
    main()
