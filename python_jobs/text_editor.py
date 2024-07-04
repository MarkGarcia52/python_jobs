"We need to import the graphics library."

import tkinter as tk # alysis
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window, text_edit):
    "Open a file, replace contents of old contents"

    # File type will be python, text, etc
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt.")])

    if not filepath:
        return
    
    # 1 means line 1, and 0 is the first character
    # We deleted all the content
    text_edit.delete(1.0,tk.END)

        # Open the file
    with open(filepath, "r") as f:

        # Read the file
        content = f.read()

        # Insert all of the content
        # End will be the very beginning of the file
        text_edit.insert(tk.END, content)

    window.title(f"Open File: {filepath}")
    

def save_file(window, text_edit):
    "Save a file with 'old contents'."
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt.")])
    
    if not filepath:
        return 
    
    with open(filepath, "w") as f:
        # Get from beginning to the end of the file
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open FIle: {filepath}")



def main():
    "Write a bulk of the tkinter code"
    "We will create tkinter window"
    window = tk.Tk()
    # Set the title of the window 
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    # We will create buttons within the text editor.

    # Build text editor widget
    text_edit = tk.Text(window, font="Helvetica 18") # We have to pass the window argument so we can have this in the window

    # We want to render ^ on the screen

    # Tkinter uses a grid system, this allows you to lay things out on a row and column system
    # 0,0 is top left corner

    # .grid will place this element onto grid of parent
    # That's bc text edit component right, and components on the left
    # It will automatically fill the entire screen (top left)

    text_edit.grid(row=0, column=1)

    # Create the buttons and set them on the screen

    # relief makes 3d objects, and raise makes it look 3 dimensional
    # bd stands for boarder

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    # We are placing button on the frame

    # We will use lambda to write the function in one line
    # Lambda will call the open_file function with the arguments, window, and text edit
    #   So open button will use the lambda function which will call it and then call the open file function w arguments.

    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    # We call the buttons to the grid and specify the location

    # Pad gives it some space from the column specified
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    # Expand horizontal direction
    open_button.grid(row=1, column=0, padx=5, sticky="ew")

    # We will pass sticky so the button sticks to the frame and ns expands it to the north and the south into whatever it
    #   it's inside of
    frame.grid(row=0, column=0, sticky="ns")

    # Hot Keys

    # BInd a command to keypress
    # Lambda is a function, x is an argument.
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda y: save_file(window, text_edit))

    # This will loop keep the window open until the user closes it.
    window.mainloop()

# We call the main function.
main()