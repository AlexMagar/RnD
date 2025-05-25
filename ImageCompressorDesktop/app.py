import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# downscale_image function copied from Convert_Image/convertImage.py for simplicity
def downscale_image(input_path, output_path, new_width=800):
    """
    Downscale the image to the specified width while maintaining aspect ratio.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the downscaled image.
        new_width (int, optional): The desired width of the downscaled image. Defaults to 800.
    """
    with Image.open(input_path) as img:
        original_size = img.size
        aspect_ratio = original_size[0] / original_size[1]
        new_height = int(new_width / aspect_ratio)
        new_size = (new_width, new_height)
        resized_image = img.resize(new_size, Image.LANCZOS)
        resized_image.save(output_path)

class ImageCompressorApp:
    def __init__(self, root):
        """
        Initialize the Image Compressor desktop application GUI.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("Image Compressor Desktop App")
        self.root.geometry("600x500")

        self.selected_files = []

        # Button to select image files
        self.select_button = tk.Button(root, text="Select Images", command=self.select_files)
        self.select_button.pack(pady=10)

        # Listbox to display selected files
        self.listbox = tk.Listbox(root, width=80, height=15)
        self.listbox.pack(pady=10)

        # Button to compress selected images
        self.compress_button = tk.Button(root, text="Compress Images", command=self.compress_images, state=tk.DISABLED)
        self.compress_button.pack(pady=10)

        # Label to show status messages
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)

        # Folder to save compressed images
        self.compressed_folder = os.path.join("./ImageCompressorDesktop/Compressed_Image")
        os.makedirs(self.compressed_folder, exist_ok=True)

    def select_files(self):
        """
        Open a file dialog to select image files and display them in the listbox.
        Enable the compress button if files are selected.
        """
        files = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if files:
            self.selected_files = list(files)
            self.listbox.delete(0, tk.END)
            for f in self.selected_files:
                self.listbox.insert(tk.END, f)
            self.compress_button.config(state=tk.NORMAL)
            self.status_label.config(text=f"{len(self.selected_files)} files selected.")
        else:
            self.status_label.config(text="No files selected.")
            self.compress_button.config(state=tk.DISABLED)

    def compress_images(self):
        """
        Compress the selected images using the downscale_image function.
        Show progress and completion messages.
        """
        if not self.selected_files:
            messagebox.showwarning("No files", "Please select images to compress.")
            return

        self.status_label.config(text="Compressing images...")
        self.root.update_idletasks()

        success_count = 0
        for file_path in self.selected_files:
            try:
                filename = os.path.basename(file_path)
                output_path = os.path.join(self.compressed_folder, f"compressed_{filename}")
                downscale_image(file_path, output_path)
                success_count += 1
            except Exception as e:
                print(f"Error compressing {file_path}: {e}")

        self.status_label.config(text=f"Compression complete: {success_count}/{len(self.selected_files)} images compressed.")
        messagebox.showinfo("Done", f"Compression complete: {success_count}/{len(self.selected_files)} images compressed.\nSaved in {self.compressed_folder}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressorApp(root)
    root.mainloop()
