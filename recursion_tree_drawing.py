import turtle

# turtle settings
turtle.left(90)
turtle.speed(150)


def main():
    # Get the number of branches
    fractal_tree(100)
    turtle.done()


def fractal_tree(i):
    if i < 10:
        return
    else:
        turtle.forward(i)
        turtle.left(30)
        fractal_tree(3 * i / 4)
        turtle.right(60)
        fractal_tree(3 * i / 4)
        turtle.left(30)
        turtle.backward(i)

# Call the main function.
main()