from PIL import Image, ImageEnhance

def crop_and_adjust_brightness(image_path, output_path, upper_row, lower_row, brightness_factor):
    # Open the image
    img = Image.open(image_path)
    
    # Get the size of the image
    width, height = img.size
    
    # Ensure the lower_row is not out of bounds
    lower_row = min(lower_row, height - 1)
    
    # Ensure the upper_row is not out of bounds
    upper_row = max(upper_row, 0)
    
    # Crop the image from upper_row to lower_row (inclusive)
    cropped_img = img.crop((0, upper_row, width, lower_row + 1))
    
    # Adjust the brightness
    enhancer = ImageEnhance.Brightness(cropped_img)
    cropped_img = enhancer.enhance(brightness_factor)
    
    # Save the cropped and adjusted image
    cropped_img.save(output_path)

# Example usage:
# Adjust brightness by setting brightness_factor (1.0 means no change, <1.0 darkens, >1.0 brightens)
crop_and_adjust_brightness(
    "images/10-15-Night.jpg",
    "images/10-15-Night_crop.jpg",
    # "images/gray.jpg",
    # "images/gray_crop.jpg",
    upper_row=1834, lower_row=2537, brightness_factor=0.56)
