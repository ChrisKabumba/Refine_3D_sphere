<h1>3D Rotating Bouncing Sphere Simulation</h1>
This project simulates a 3D rotating and bouncing sphere using Python and pygame. It uses simple 3D transformations to project points onto a 2D screen, creating an illusion of depth and movement in a 3D space. The sphere can rotate, bounce within the screen, and be color-shaded based on distance to enhance the 3D effect.

Features
3D Rotation: The sphere continuously rotates around the x, y, and z axes, creating a realistic 3D appearance.
Bouncing Effect: The sphere bounces off the edges of the screen, changing direction when it reaches the boundary.
Dynamic Shading: Each point on the sphere is shaded based on its depth, creating a sense of lighting and enhancing the 3D illusion.
Adjustable Rotation Speed: You can increase or decrease the rotation speed using the arrow keys.
Controls
Up Arrow: Increases the rotation speed.
Down Arrow: Decreases the rotation speed.
How It Works
Generating 3D Points: The surface of the sphere is represented by randomly distributed points in 3D space, calculated using spherical coordinates to ensure uniform distribution around the sphere.

3D Rotation: The points are rotated around the x, y, and z axes based on user-controlled angles. This is done with trigonometric rotation formulas for each axis, simulating a 3D rotating effect.

Projection to 2D: After rotation, each 3D point is projected onto a 2D screen using a perspective formula. The depth of each point affects its position and size, creating a sense of perspective.

Depth-Based Shading: Each point’s color changes based on its distance from the viewer (z-coordinate), making points farther away appear darker. This depth shading creates a subtle lighting effect on the sphere.

Bouncing Logic: The sphere’s center moves across the screen with a set velocity. When it reaches the screen edges, it reverses direction to simulate bouncing within a confined space.

Setup and Execution
Requirements: Make sure you have pygame installed. You can install it with:

pip install pygame
Running the Program: Run the script using Python:

python bouncing_sphere.py
Exiting: Close the window or press ESC to exit the simulation.

Example Output
The program displays a 3D-like sphere with points rotating, shading, and bouncing within the screen. Adjust the rotation speed using the arrow keys to see different effects.
