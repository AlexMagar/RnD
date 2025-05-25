import os
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
    with Image.open(input_path) as img: #open the input image file
        original_size = img.size  #get orginal size of image
        aspect_ratio = original_size[0] / original_size[1] #calculate the aspect ratio
        new_height = int(new_width / aspect_ratio) #calculate new height to maintain aspect ratio
        new_size = (new_width, new_height) #create a tuple for the new size
        resized_image = img.resize(new_size, Image.LANCZOS) #resize the image using LANCZOS filter
        resized_image.save(output_path) #save the resised image to the output path 
