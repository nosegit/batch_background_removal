import rembg
import numpy as np
from PIL import Image
import os
from multiprocessing import Pool, cpu_count


# Paths
dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(dir_path, "images", "input")
output_path = os.path.join(dir_path, "images", "output")

# Ensure the output directory exists
# os.makedirs(output_path, exist_ok=True)

# Function to process a single image
def process_image(filename):
    try:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # Load the input image
            input_image = Image.open(os.path.join(input_path, filename))

            # Convert the input image to a numpy array
            input_array = np.array(input_image)

            # Apply background removal using rembg
            output_array = rembg.remove(input_array)

            # Create a PIL Image from the output array
            output_image = Image.fromarray(output_array)

            # Save the output image
            output_image.save(os.path.join(output_path, filename[:-3] + "png"))
            print(f"Processed: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Main function for multiprocessing
if __name__ == "__main__":

    print("loading images...")
    # Get the list of image files
    image_files = [f for f in os.listdir(input_path) if f.endswith((".png", ".jpg"))]

    print(f"processing {len(image_files)} images")
    # Use a pool of processes to process images in parallel
    with Pool(cpu_count()) as pool:
        pool.map(process_image, image_files)

    print("Processing complete.")
