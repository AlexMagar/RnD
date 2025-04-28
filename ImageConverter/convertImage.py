from PIL import Image

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
        print(f'Original size: {original_size}')

        aspect_ratio = original_size[0] / original_size[1]
        new_height = int(new_width / aspect_ratio)
        new_size = (new_width, new_height)

        resized_image = img.resize(new_size, Image.LANCZOS)
        resized_image.save(output_path)
        print(f'Resized image saved to: {output_path}')
        print(f'New size: {new_size}')


if __name__ == "__main__":
    # Example usage
    input_image_path = "./Image/img2.png"
    output_image_path = "./Image/img21.png"
    downscale_image(input_image_path, output_image_path, new_width=800)
