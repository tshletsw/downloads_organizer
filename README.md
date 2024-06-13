Downloads Organizer:
Downloads Organizer is a Python script that helps you manage your Downloads folder by automatically organizing files into subfolders based on their file types. This script also cleans up existing files in the Downloads folder and organizes them accordingly.

Features:
1. Automatically organize new files in the Downloads folder based on their file type.
2. Organize existing files in the Downloads folder upon script startup.
4. Real-time monitoring of the Downloads folder using the watchdog library.

Why Is It Useful?
1. Keeps Downloads Folder Organized: Automatically sorts files, reducing the clutter and making it easier to find files.
2. Saves Time: Eliminates the need for manual file organization.
3. Customizable: Easily modify the script to handle different file types and categories based on your needs.

How It Works
File Organization:
* The script defines a dictionary (subfolders) that maps subfolder names to lists of file extensions.
* When a new file is created in the Downloads folder, the script moves the file to the appropriate subfolder based on its extension.
* When the script starts, it first organizes all existing files in the Downloads folder.

Real-Time Monitoring:
* The script uses the watchdog library to monitor the Downloads folder for new files.
* The DownloadHandler class inherits from FileSystemEventHandler and handles file creation events.

Explanation of the Code:

1. Imports:
* os: Provides functions for interacting with the operating system.
* shutil: Provides functions for high-level file operations.
* watchdog.observers.Observer: Observes the file system for changes.
* watchdog.events.FileSystemEventHandler: Handles events for the observer.

2. Folder and Subfolder Definitions:
* downloads_folder: Specifies the path to the Downloads folder.
* subfolders: A dictionary mapping folder names to lists of file extensions.

3. DownloadHandler Class:
* Inherits from FileSystemEventHandler.
* on_created: Method called when a new file is created. It checks if the event is not a directory and calls organize_file.
* organize_file: Moves the file to the appropriate subfolder based on its extension.
  
4. organize_existing_files Function:
* Organizes existing files in the Downloads folder into the appropriate subfolders.

5. Main Execution Block:
* Calls organize_existing_files to organize current files in the Downloads folder.
* Sets up an Observer to monitor the Downloads folder for new files and handle them using the DownloadHandler.
* Keeps the script running to continue monitoring until interrupted.
