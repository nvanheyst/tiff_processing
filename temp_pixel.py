import cv2

# Load the 16-bit TIFF file
image_16bit = cv2.imread('thermal_image.tiff', cv2.IMREAD_UNCHANGED)

# Choose the pixel coordinates (x, y)
x, y = 100, 150  # Example pixel coordinates

# Access the raw pixel value
raw_pixel_value = image_16bit[y, x]

# Conversion factor and offset (example values; these will depend on your camera's specifications)
scale_factor = 0.04  # Example scale factor (check camera documentation)
offset = -273.15  # Example offset to convert from Kelvin to Celsius

# Calculate the temperature
temperature_celsius = (raw_pixel_value * scale_factor) + offset

print(f"Temperature at pixel ({x}, {y}): {temperature_celsius:.2f}°C")
