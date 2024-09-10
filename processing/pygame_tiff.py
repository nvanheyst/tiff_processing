import pygame
import cv2

path = #path
image_name = #thermal_image.tiff

pygame.init()
image_16bit = cv2.imread(str(path+image_name), cv2.IMREAD_UNCHANGED)
image_8bit = cv2.normalize(image_16bit, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
image_rgb = cv2.cvtColor(image_8bit, cv2.COLOR_GRAY2RGB)
height, width = image_rgb.shape[:2]
screen = pygame.display.set_mode((width, height))
image_surface = pygame.surfarray.make_surface(image_rgb)

def get_temperature(raw_value, scale_factor=0.04, offset=-273.15):
    return (raw_value * scale_factor) + offset


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

      
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()  

        
            raw_pixel_value = image_16bit[y, x]

           
            temperature = get_temperature(raw_pixel_value)

            print(f"Temperature at pixel ({x}, {y}): {temperature:.2f}°C")

    screen.blit(image_surface, (0, 0))
    pygame.display.update()

pygame.quit()
