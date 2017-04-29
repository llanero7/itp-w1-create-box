"""This is the entry point of the program."""

def create_box(height, width, character):
    box = ""
    for i in range(height):
        line = ""
        for j in range(width): #if width is 4 we want this loop to run 4 times, and add 4 characters to our line
            line += character
        box += line + '\n'
    return box