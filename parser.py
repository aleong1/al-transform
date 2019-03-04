from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, "r")
    lines = file.readlines()
    clearLines = [line.strip() for line in lines]  #clear spaces
    ctr = 0
    while ctr < len(clearLines):
        current = clearLines[ctr]
        if current == "line":  #commands w args
            arg = clearLines[ctr + 1].split()
            args = [int(a) for a in arg]
            add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
            ctr += 2
        elif current == "scale":
            arg = clearLines[ctr + 1].split()
            args = [int(a) for a in arg]
            matrix_mult(make_scale(args[0], args[1], args[2]), transform)
            ctr += 2
        elif current == "translate" or current == "move":
            arg = clearLines[ctr + 1].split()
            args = [int(a) for a in arg]
            matrix_mult(make_translate(args[0], args[1], args[2]), transform)
            ctr += 2
        elif current == "rotate":
            arg = clearLines[ctr + 1].split()
            if arg[0] == "x":
                m = make_rotX(int(arg[1]))
            elif arg[0] == "y":
                m = make_rotY(int(arg[1]))
            else:
                m = make_rotZ(int(arg[1]))
            matrix_mult(m, transform)
            ctr += 2
        elif current == "save":
            a = clearLines[ctr + 1]
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            save_extension(screen, a)
            ctr += 2
        else:  #no arg commands
            if current == "ident":
                ident(transform)
            elif current == "apply":
                matrix_mult(transform, points)
            elif current == "display":
                clear_screen(screen)
                draw_lines(points, screen, color)
                display(screen)
            elif current == "quit":
                ctr = len(clearLines)
            ctr += 1
