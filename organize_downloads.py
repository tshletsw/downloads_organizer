import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the folder to track (Downloads folder)
downloads_folder = os.path.expanduser("~/Downloads")

# Define the subfolders for different file types
subfolders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programs": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
  
}

# Event handler class that inherits from FileSystemEventHandler
class DownloadHandler(FileSystemEventHandler):
    # Method to handle file creation events
    def on_created(self, event):
        # Check if the event is not a directory creation
        if not event.is_directory:
            # Organize the newly created file
            self.organize_file(event.src_path)

    # Method to organize a file into the appropriate subfolder
    def organize_file(self, file_path):
        # Get the file name and extension
        file_name, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()
        
        # Iterate through subfolders to find the matching extension
        for folder, extensions in subfolders.items():
            if file_extension in extensions:
                # Determine the destination folder path
                destination_folder = os.path.join(downloads_folder, folder)
                # Create the destination folder if it doesn't exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                # Move the file to the destination folder
                shutil.move(file_path, destination_folder)
                print(f"Moved: {file_path} to {destination_folder}")
                break

# Function to organize existing files in the Downloads folder
def organize_existing_files():
    # List all items in the Downloads folder
    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)
        # Check if the item is a file (not a folder)
        if os.path.isfile(item_path):
            # Get the file name and extension
            file_name, file_extension = os.path.splitext(item_path)
            file_extension = file_extension.lower()
            # Iterate through subfolders to find the matching extension
            for folder, extensions in subfolders.items():
                if file_extension in extensions:
                    # Determine the destination folder path
                    destination_folder = os.path.join(downloads_folder, folder)
                    # Create the destination folder if it doesn't exist
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    # Move the file to the destination folder
                    shutil.move(item_path, destination_folder)
                    print(f"Moved: {item_path} to {destination_folder}")
                    break

if __name__ == "__main__":
    # Organize existing files in the Downloads folder
    organize_existing_files()
    
    # Set up the event handler and observer for real-time monitoring
    event_handler = DownloadHandler()
    observer = Observer()
    # Schedule the observer to monitor the Downloads folder
    observer.schedule(event_handler, downloads_folder, recursive=True)
    observer.start()
    print(f"Monitoring {downloads_folder}...")

    try:
        # Keep the script running to monitor folder changes
        while True:
            pass
    except KeyboardInterrupt:
        # Stop the observer when interrupted (e.g., with Ctrl+C)
        observer.stop()
    observer.join()
