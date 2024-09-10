import pygame
import cv2

# Initialize Pygame
pygame.init()

# Load the 16-bit TIFF image using OpenCV
image_16bit = cv2.imread('thermal_image.tiff', cv2.IMREAD_UNCHANGED)

# Convert the image to 8-bit for display purposes (scaling for better visualization)
image_8bit = cv2.normalize(image_16bit, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Convert the image to RGB format for Pygame
image_rgb = cv2.cvtColor(image_8bit, cv2.COLOR_GRAY2RGB)

# Get the image dimensions
height, width = image_rgb.shape[:2]

# Set up the Pygame display
screen = pygame.display.set_mode((width, height))

# Convert the OpenCV image to a Pygame surface
image_surface = pygame.surfarray.make_surface(image_rgb)

# Function to convert raw pixel value to temperature
def get_temperature(raw_value, scale_factor=0.04, offset=-273.15):
    return (raw_value * scale_factor) + offset

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the user clicks the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()  # Get the coordinates of the click

            # Get the raw pixel value from the 16-bit image at the clicked coordinates
            raw_pixel_value = image_16bit[y, x]

            # Convert the raw pixel value to temperature
            temperature = get_temperature(raw_pixel_value)

            print(f"Temperature at pixel ({x}, {y}): {temperature:.2f}°C")

    # Display the image on the Pygame window
    screen.blit(image_surface, (0, 0))
    pygame.display.update()

# Quit Pygame
pygame.quit()
