import pygame
import math
import random
import sys

# Initialize pygame and set up display
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Rotatable Sphere")

# Define colors
BACKGROUND_COLOR = (10, 10, 20)
SPHERE_COLOR = (200, 200, 255)

# Sphere settings
RADIUS = 200
POINTS_COUNT = 500  # Number of points on the sphere

# Camera and rotation settings
angle_x, angle_y = 0, 0
rotation_speed = 0.05  # Rotation speed for arrow keys

# Generate points on a sphere using spherical coordinates
def generate_sphere_points(radius, count):
    points = []
    for _ in range(count):
        theta = random.uniform(0, 2 * math.pi)
        phi = random.uniform(0, math.pi)
        x = radius * math.sin(phi) * math.cos(theta)
        y = radius * math.sin(phi) * math.sin(theta)
        z = radius * math.cos(phi)
        points.append([x, y, z])
    return points

# Rotate points around x-axis
def rotate_x(points, angle):
    cos_angle, sin_angle = math.cos(angle), math.sin(angle)
    for p in points:
        y = p[1] * cos_angle - p[2] * sin_angle
        z = p[1] * sin_angle + p[2] * cos_angle
        p[1], p[2] = y, z

# Rotate points around y-axis
def rotate_y(points, angle):
    cos_angle, sin_angle = math.cos(angle), math.sin(angle)
    for p in points:
        x = p[0] * cos_angle + p[2] * sin_angle
        z = -p[0] * sin_angle + p[2] * cos_angle
        p[0], p[2] = x, z

# Project 3D points onto the 2D screen
def project_points(points):
    projected_points = []
    for p in points:
        scale = RADIUS / (RADIUS + p[2])
        x_2d = int(WIDTH / 2 + p[0] * scale)
        y_2d = int(HEIGHT / 2 + p[1] * scale)
        projected_points.append((x_2d, y_2d))
    return projected_points

# Main loop
sphere_points = generate_sphere_points(RADIUS, POINTS_COUNT)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses for rotation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle_y -= rotation_speed
    if keys[pygame.K_RIGHT]:
        angle_y += rotation_speed
    if keys[pygame.K_UP]:
        angle_x -= rotation_speed
    if keys[pygame.K_DOWN]:
        angle_x += rotation_speed

    # Rotate the sphere points
    rotate_x(sphere_points, angle_x)
    rotate_y(sphere_points, angle_y)

    # Project points and draw them
    projected_points = project_points(sphere_points)
    for point in projected_points:
        pygame.draw.circle(screen, SPHERE_COLOR, point, 2)  # Draw each point as a small circle

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

# Quit pygame
pygame.quit()
sys.exit()
