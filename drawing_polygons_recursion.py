import turtle

# turtle settings
turtle.speed(20)


def main():
    # Get the number of sides
    poly_side = int(input("Enter number of sides for the polygon: "))
    poly_len = int(input("Enter the length of the polygon: "))

    polygon(poly_side, poly_len)
    turtle.exitonclick()


def polygon(sides, length):
    if length < 0:
        turtle.done()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)
    polygon(sides, length - 2)


# Call the main function.
main()