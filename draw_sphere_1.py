import math
import cairo
import random

WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)


def draw_background(context):
    # Create a radial gradient for the background to add depth
    bg_gradient = cairo.RadialGradient(WIDTH / 2, HEIGHT / 2, WIDTH / 2, WIDTH / 2, HEIGHT / 2, 0)
    bg_gradient.add_color_stop_rgb(0, 0.05, 0.05, 0.1)  # Dark blue
    bg_gradient.add_color_stop_rgb(1, 0.0, 0.0, 0.0)    # Black
    context.set_source(bg_gradient)
    context.paint()


def draw_sphere(context, center_x, center_y, radius):
    # Sphere body gradient for 3D lighting effect
    sphere_gradient = cairo.RadialGradient(center_x, center_y, radius * 0.2, center_x, center_y, radius)
    sphere_gradient.add_color_stop_rgb(0, 0.9, 0.9, 1)  # Bright highlight
    sphere_gradient.add_color_stop_rgb(0.5, 0.5, 0.5, 0.8)  # Midtones
    sphere_gradient.add_color_stop_rgb(1, 0.2, 0.2, 0.3)  # Dark shadow

    # Draw sphere with gradient
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    context.set_source(sphere_gradient)
    context.fill()

    # Enhanced highlight effect
    for i in range(3):
        highlight_radius = radius * (0.08 - 0.02 * i)
        highlight_opacity = 0.5 - i * 0.15
        context.arc(center_x - radius * 0.3, center_y - radius * 0.3, highlight_radius, 0, 2 * math.pi)
        context.set_source_rgba(1, 1, 1, highlight_opacity)  # Semi-transparent white
        context.fill()

    # Add texture to the sphere's surface for realism
    context.set_source_rgba(0, 0, 0, 0.05)  # Very subtle, transparent black dots
    for _ in range(150):
        x = center_x + (random.uniform(-1, 1) * radius * 0.9)
        y = center_y + (random.uniform(-1, 1) * radius * 0.9)
        dot_radius = random.uniform(0.5, 1.5)
        context.arc(x, y, dot_radius, 0, 2 * math.pi)
        context.fill()


# Draw the scene
draw_background(context)
draw_sphere(context, WIDTH // 2, HEIGHT // 2, 200)

# Save the output to a PNG file
surface.write_to_png("3d_sphere_refined.png")

print("Refined 3D sphere image created!")