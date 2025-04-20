import turtle

def draw_branch(t, branch_length, depth, angle_left, angle_right, reduction_factor):
    """
    Recursively draws branches of a fractal tree.
    
    Parameters:
    t                -- turtle object
    branch_length    -- current length of the branch
    depth            -- how many more levels of branching to draw
    angle_left       -- angle (in degrees) for the left branch
    angle_right      -- angle (in degrees) for the right branch
    reduction_factor -- fraction by which each branch length is reduced
    """
    if depth == 0:
        return

    # Draw the current branch
    t.forward(branch_length)

    # Turn left and draw the left subtree
    t.left(angle_left)
    draw_branch(t, branch_length * reduction_factor, depth - 1, angle_left, angle_right, reduction_factor)
    t.right(angle_left)

    # Turn right and draw the right subtree
    t.right(angle_right)
    draw_branch(t, branch_length * reduction_factor, depth - 1, angle_left, angle_right, reduction_factor)
    t.left(angle_right)

    # Go back to the original position
    t.backward(branch_length)

def main():
    # Prompt the user for parameters
    angle_left = float(input("Enter the left angle (in degrees): "))
    angle_right = float(input("Enter the right angle (in degrees): "))
    start_length = float(input("Enter the starting branch length: "))
    depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor: "))

    # Set up the turtle
    screen = turtle.Screen()
    screen.title("Recursive Tree with Turtle Graphics")
    t = turtle.Turtle()
    t.speed(0)       # 0 means "fastest"
    t.left(90)       # Turn the turtle to face 'up' before drawing

    # Draw the tree
    draw_branch(t, start_length, depth, angle_left, angle_right, reduction_factor)

    # Click on the window to exit
    screen.exitonclick()

if __name__ == "__main__":
    main()
