from PIL import Image

def process_image(image_path, output_path, upper_row, lower_row):
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to RGB if it isn't already
    img = img.convert("RGB")
    
    # Get the size of the image
    width, height = img.size
    
    # Load pixel data
    pixels = img.load()
    
    # Process the image
    for y in range(height):
        for x in range(width):
            if y < upper_row or y > lower_row:
                pixels[x, y] = (0, 0, 0)  # Set to pure black
            else:
                pixels[x, y] = (255, 255, 255)  # Set to pure white
    
    # Save the edited image
    img.save(output_path)

# Example usage:
process_image("images/6016.png", "images/6016_whiterow.png", upper_row=1833, lower_row=2537)
