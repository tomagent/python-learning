from tkinter import *
import game

cell_size = 5
is_running = False

def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice
    
    # Create GUI
    root = Tk()
    root.title("The Game of Life")

    # Set size
    grid_view = Canvas(root, width=game.width*cell_size, height=game.height*cell_size, borderwidth=0, highlightthickness=0, bg="white")

    # Add start 
    start_button = Button(root, text="Start", width=12)
    # Call start_handler when clicked
    start_button.bind("<Button-1>", start_handler)
    
    # Clear button
    clear_button = Button(root, text="Clear", width=12)
    # Call clear handler when clicked
    clear_button.bind("<Button-1>", clear_handler)

    # Option menu
    choice = StringVar(root)
    choice.set("Choose a Pattern")
    option = OptionMenu(root, choice, "Choose a Pattern", "glider", "glider gun", "random")
    option.config(width=20)

    # Layout
    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    # Grid view event
    grid_view.bind("<Button-1>", grid_handler)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)


# User clicks
def grid_handler(event):
    global grid_view, cell_size

    # Get x and y position of the cell clicked
    x = int(event.x / cell_size)
    y = int(event.y / cell_size)

    # If it's alive, zero it and color it white
    if (game.grid_model[x][y] == 1):
        game.grid_model[x][y] == 0
        draw_cell(x, y, "white")
    # If it isn't alive 
    else:
        game.grid_model == 1
        draw_cell(x, y, "black")

# Start event
def start_handler(event):
    global is_running, start_button

    # If it isn't running
    if is_running:
        is_running = False
        start_button.configure(text="Start")
    # If it is running
    else:
        is_running = True
        start_button.configure(text="Pause")
        update()

# Clear event
def clear_handler(event):
    global is_running, start_button

    # Turn off run it and dead all the cells (zero out them)
    is_running = False
    for i in range(0, game.height):
        for j in range(0 , game.width):
            game.grid_model[i][j] = 0

    start_button.configure(text="Start")
    update()
    

def update():
    global grid_view, root, is_running

    # Delete anything drawn on the canvas
    grid_view.delete(ALL)
    # Compute the next gen
    game.next_gen()
    # Iterate through every cell
    for i in range(0, game.height):
        for j in range(0, game.width):
            if game.grid_model[i][j] == 1: # If a cell at i, j is live, a black rectangle is drawn
                draw_cell(i, j, "black")
    # Call update in 100 miliseconds
    if (is_running):
        root.after(100, update)


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
