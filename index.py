import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set the speed of drawing
pen.speed(2)

# Draw a square
for _ in range(4):
    pen.forward(100)   # Move forward by 100 units
    pen.right(90)      # Turn right by 90 degrees

# Keep the window open until clicked
turtle.done()
