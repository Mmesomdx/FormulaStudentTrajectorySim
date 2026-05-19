import os
from PIL import Image

def resize_single_png(input_path, output_path, target_size=(25, 25)):
    """
    Resizes a single PNG image to 25x25 while preserving transparency.
    """
    try:
        with Image.open(input_path) as img:
            # Ensure it's treated as a PNG (preserves RGBA/transparency channels)
            img = img.convert("RGBA")
            
            # Resize using LANCZOS for high quality downscaling
            resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
            
            # Save the result
            resized_img.save(output_path, "PNG")
            print(f"Successfully resized: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def batch_resize_pngs(input_folder, output_folder, target_size=(25, 25)):
    """
    Resizes all PNG images in a folder to 25x25.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            # Prepends 'resized_' to the original name, or change as you like
            output_path = os.path.join(output_folder, f"resized_{filename}")
            
            resize_single_png(input_path, output_path, target_size)

# --- Example Usage ---

# Choice A: Resize just one image
resize_single_png('orange_cone.png', 'orange_cone_25x25.png')
resize_single_png('blue_cone.png', 'blue_cone_25x25.png')

# Choice B: Resize an entire folder of PNGs (Uncomment to use)
# batch_resize_pngs('./input_images', './output_images')
