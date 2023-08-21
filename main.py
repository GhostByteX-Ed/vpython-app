from vpython import *
import random
# Constants
width = 1000    # Width of the screen (units)
height = 600    # Height of the screen (units)
screen_res = (width, height)
port_number = 8080
# Create the scene
scene = canvas(port=8080, width=width, height=height, center=vector(0, 0, 0), background=color.black)
# Create the ball object
ball = sphere(pos=vector(100, 100, 0), radius=40, color=color.red)
# Random initial velocity of the ball
initial_velocity = vector(random.uniform(-1, 1), random.uniform(-1, 1), 0) * 3
# Animation loop
while True:
    rate(100)  # Limit the animation speed
    
    # Update the ball's position based on its velocity
    ball.pos = ball.pos + initial_velocity
    
    # Check if the ball hits the screen edge and handle the bounce
    if abs(ball.pos.x) >= width / 2 - ball.radius:
        initial_velocity.x = -initial_velocity.x
    
    if abs(ball.pos.y) >= height / 2 - ball.radius:
        initial_velocity.y = -initial_velocity.y
