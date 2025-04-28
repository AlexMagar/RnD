import sys
import os
from convertImage import downscale_image

def generate_output_path(input_path):
    """
    Generate output path by appending '_downscaled' before the file extension.
    """
    base, ext = os.path.splitext(input_path)
    return f"{base}_downscaled{ext}"

def main():
    # argv give the user defined path
    if len(sys.argv) < 2: 
        print(sys.argv)
        print("Usage: python main.py <image_path1> <image_path2> ...")
        sys.exit(1)

    image_paths = sys.argv[1:]
    print()
    for input_path in image_paths:
        if not os.path.isfile(input_path):
            print(f"File not found: {input_path}")
            continue

        output_path = generate_output_path(input_path)
        try:
            downscale_image(input_path, output_path)
            print(f"Downscaled image saved to: {output_path}")
        except Exception as e:
            print(f"Failed to downscale {input_path}: {e}")

if __name__ == "__main__":
    main()

# python ImageConverter/main.py ImageConverter/Image/img1.png ImageConverter/Image/img2.png;  