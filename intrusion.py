import pygame
import pygame.camera
import numpy as np

# Initialize Pygame and Camera
pygame.init()
pygame.camera.init()

# Set up camera (use the first available one)
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (640, 480))
cam.start()

# Create display surface
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Intrusion Detection")

# Initialize Pygame mixer for sound
pygame.mixer.init()

# Load warning sound (make sure the path to the file is correct)
warning_sound = pygame.mixer.Sound("/home/rohith/intrusion_detection_project/warning.wav")

# Yellow line y-position
LINE_Y = 300
threshold = 40  # Pixel change threshold

# Previous frame placeholder
prev_frame = None
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current frame from camera
    current_surface = cam.get_image()
    screen.blit(current_surface, (0, 0))
    current_array = pygame.surfarray.array3d(current_surface)

    # Draw yellow line
    pygame.draw.line(screen, (255, 255, 0), (0, LINE_Y), (640, LINE_Y), 2)

    # Intrusion detection
    if prev_frame is not None:
        diff = np.abs(current_array.astype(int) - prev_frame.astype(int))
        mask = np.any(diff > threshold, axis=2)

        # Detect motion below the yellow line
        intrusion_points = []
        for y in range(LINE_Y, current_array.shape[1]):
            for x in range(current_array.shape[0]):
                if mask[x, y]:
                    intrusion_points.append((x, y))

        if intrusion_points:
            xs, ys = zip(*intrusion_points)
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)
            # Draw red bounding box
            pygame.draw.rect(screen, (255, 0, 0), (min_x, min_y, max_x - min_x, max_y - min_y), 2)
            print("Intrusion Detected!")

            # Play the warning sound
            warning_sound.play()

    # Update display
    pygame.display.update()
    clock.tick(30)  # Limit to 30 FPS

    # Save current frame for next comparison
    prev_frame = current_array

# Cleanup
cam.stop()
pygame.quit()