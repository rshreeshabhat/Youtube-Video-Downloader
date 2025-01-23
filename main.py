import os
import subprocess
from tkinter import Tk, StringVar, Entry, Label, filedialog, messagebox
from customtkinter import CTk, CTkButton

def select_location():
    location = filedialog.askdirectory()
    if location:
        download_location.set(location)

def download_video(video_url):
    if not video_url.strip():
        messagebox.showerror("Error", "Please enter a valid YouTube URL!")
        return

    location = download_location.get()
    if not location.strip():
        messagebox.showerror("Error", "Please select a save location!")
        return

    try:
        subprocess.run(
            [
                "yt-dlp",
                "-o", os.path.join(location, "%(title)s.%(ext)s"),
                video_url,
            ],
            check=True,
        )
        messagebox.showinfo("Success", f"Video downloaded successfully to {location}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")
    except FileNotFoundError:
        messagebox.showerror("Error", "yt-dlp is not installed or not in your PATH. Please install it.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = CTk()
    root.title("YouTube Video Downloader")
    root.geometry("550x350")

    global download_location
    download_location = StringVar()

    Label(root,text="YouTube Video Downloader",font=("Helvetica", 20, "bold"),bg="black" ,fg="white").grid(row=0, column=0, columnspan=2, pady=15, sticky="n")

    Label(root, text="Video URL:", font=("Helvetica", 16),bg="black",fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    url_entry = Entry(root, width=60)
    url_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(root, text="Save to:", font=("Helvetica", 16),bg="black",fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    location_entry = Entry(root, textvariable=download_location, width=60, state="readonly")
    location_entry.grid(row=2, column=1, padx=10, pady=5)

    location_button = CTkButton(root, text="Select Location", command=select_location)
    location_button.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    download_button = CTkButton(
        root,
        text="Download",
        command=lambda: download_video(url_entry.get()),
    )
    download_button.grid(row=4, column=0, columnspan=2, pady=25)
    
    root.mainloop()

if __name__ == "__main__":
    main()
