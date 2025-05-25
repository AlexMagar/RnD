import os
import tkinter as tk
from tkinter import filedialog, messagebox
from Image_process.image_processor import downscale_image

class ImageCompressorApp:
    def __init__(self, root):
        """
        Initialize the Image Compressor desktop application GUI.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root #store the root window
        self.root.title("Image Compressor Desktop App") #window title
        self.root.geometry("600x500") #window dimension 

        self.selected_files = [] #list to hold selected image file
        self.destination_folder = None #store user selected destination folder

        # Button to select image files
        self.select_button = tk.Button(root, text="Select Images", command=self.select_files)
        self.select_button.pack(pady=20) #pady: padding y axis: 20

        # Listbox to display selected files
        self.listbox = tk.Listbox(root, width=80, height=15)
        self.listbox.pack(pady=20)

        # Button to select destination folder to save compressed images
        self.select_dest_button = tk.Button(root, text="Select Destination Folder", command=self.select_destination_folder)
        self.select_dest_button.pack(pady=10)

        # Label to show selected destination folder path
        self.destination_label = tk.Label(root, text="No destination folder selected")
        self.destination_label.pack(pady=5)

        # Button to compress selected images
        self.compress_button = tk.Button(root, text="Compress Images", command=self.compress_images, state=tk.DISABLED)
        self.compress_button.pack(pady=10)

        # Label to show status messages
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)

        # Folder to save compressed images
        # self.compressed_folder = os.path.join("./ImageCompressorDesktop/Compressed_Image")
        # os.makedirs(self.compressed_folder, exist_ok=True) #create folder if doesnot exist

    def select_files(self):
        """
        Open a file dialog to select image files and display them in the listbox.
        Enable the compress button if files are selected.
        """

        # Open a file dialog to select multiple image files
        files = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if files: #check if any files were selected 
            self.selected_files = list(files) #store the selected files
            self.listbox.delete(0, tk.END) #clear the listbox
            for f in self.selected_files: #iterate through the selected files
                self.listbox.insert(tk.END, f) #add each file to the listbox
            self.compress_button.config(state=tk.NORMAL) #enable the compress button
            self.status_label.config(text=f"{len(self.selected_files)} files selected.") #update the status label
        else:            
            self.selected_files = []
            self.listbox.delete(0, tk.END)
            self.update_compress_button_state()
            self.status_label.config(text="No files selected.")

    def select_destination_folder(self):
        """
        Open a folder dialog for the user to select the destination folder.
        Update the label and compress button state accordingly.
        """
        folder = filedialog.askdirectory(title="Select Destination Folder")
        if folder:
            self.destination_folder = folder
            self.destination_label.config(text=f"Destination folder: {folder}")
        else:
            self.destination_folder = None
            self.destination_label.config(text="No destination folder selected")
        self.update_compress_button_state()
    def update_compress_button_state(self):
        """
        Enable compress button only if both files are selected and destination folder is set
        Disable it otherwise.
        """
        if self.selected_files and self.destination_folder:
            self.compress_button.config(state=tk.NORMAL)
        else:
            self.compress_button.config(state=tk.DISABLED)

    def compress_images(self):
        """
        Compress the selected images using the downscale_image function.
        Show progress and completion messages.
        """
        if not self.selected_files: #check if any files are selected
            messagebox.showwarning("No files", "Please select images to compress.") #show warning message
            return #exist if not files are selected

        if not self.destination_folder:
            messagebox.showwarning("No destination folder", "Please select a destination folder.")
            return

        self.status_label.config(text="Compressing images...") #update status label
        self.root.update_idletasks() #update the GUI to reflect the status change

        success_count = 0 #Initialise a counter for successfully compressed images
        for file_path in self.selected_files: 
            try:
                filename = os.path.basename(file_path) #get the base filename
                output_path = os.path.join(self.destination_folder, f"compressed_{filename}") #define the output path
                downscale_image(file_path, output_path) #function call
                success_count += 1 
            except Exception as e: 
                print(f"Error compressing {file_path}: {e}")

        # update the status label with the compression result
        self.status_label.config(text=f"Compression complete: {success_count}/{len(self.selected_files)} images compressed.")

        #show a message box with the completion information
        messagebox.showinfo("Done", f"Compression complete: {success_count}/{len(self.selected_files)} images compressed.\nSaved in {self.destination_folder}")

if __name__ == "__main__":
    root = tk.Tk() #create the root Tkinter window
    app = ImageCompressorApp(root)
    root.mainloop() #start the Tkinter event loop
