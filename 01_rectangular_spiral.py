import turtle

"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE

for i in range(1,100):
    turtle.forward(50*i)
    turtle.right(90)

### YOUR CODE ENDS HERE

turtle.exitonclick()