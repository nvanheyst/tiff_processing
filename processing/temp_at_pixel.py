import cv2


image_16bit = cv2.imread('thermal_image.tiff', cv2.IMREAD_UNCHANGED)

x, y = 100, 150  # Example pixel coordinates
raw_pixel_value = image_16bit[y, x]
scale_factor = 0.04  # Example scale factor
offset = -273.15  # Example offset to convert from Kelvin to Celsius

temperature_celsius = (raw_pixel_value * scale_factor) + offset

print(f"Temperature at pixel ({x}, {y}): {temperature_celsius:.2f}°C")
