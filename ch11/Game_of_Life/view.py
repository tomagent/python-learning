from tkinter import *
import game

cell_size = 5

def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice
    
    # Create GUI
    root = Tk()
    root.title("The Game of Life")

    # Set size
    grid_view = Canvas(root, width=game.width*cell_size, height=game.height*cell_size, borderwidth=0, highlightthickness=0, bg="white")

    # Add start and clear button
    start_button = Button(root, text="Start", width=12)
    clear_button = Button(root, text="Clear", width=12)

    # Option menu
    choice = StringVar(root)
    choice.set("Choose a Pattern")
    option = OptionMenu(root, choice, "Choose a Pattern", "glider", "glider gun", "random")
    option.config(width=20)

    # Layout
    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)

def update():
    global grid_view

    # Delete anything drawn on the canvas
    grid_view.delete(ALL)
    # Compute the next gen
    game.next_gen()
    # Iterate through every cell
    for i in range(0, game.height):
        for j in range(0, game.width):
            if game.grid_model[i][j] == 1: # If a cell at i, j is live, a black rectangle is drawn
                draw_cell(i, j, "black")


def draw_cell(row, col, color):
    global grid_view, cell_size

    # Aesthetic details
    if color == "black":
        outline = "grey"
    else:
        outline = "white"
    
    # Draw the rectangle
    grid_view.create_rectangle(row*cell_size, col*cell_size, row*cell_size+cell_size, col*cell_size+cell_size, fill=color, outline=outline)

    


if __name__ == "__main__":
    setup()
    update()
    mainloop()
