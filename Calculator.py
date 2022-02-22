# Importing libraries that will be needed for the calculator
from tkinter import *
import math
import tkinter.messagebox

# Creating a tkinter window
window = Tk()
window.title("CST 1500 - Coursework3- Calculator")
window.geometry("350x395")
window.resizable(0, 0)  # resizing the window to 0,0, the user won't have the option to resize it (make it bigger)
photo = PhotoImage(file="icon.png")
window.iconphoto(False, photo)


# Exit function
def exit_program():
    # messagebox to confirm if yje user wants to exit the program
    exit = tkinter.messagebox.askyesno("CST 1500 - Coursework3- Calculator", "Are you sure you want to exit?")
    if exit > 0:
        # if yes, the program will end
        window.destroy()
        return


# Scientific Calculator Function
def scientific_calculator():
    # Size of the window
    window.geometry("350x725")


# Standard Calculator Function
def standard_calculator():
    # Size of the window
    window.geometry('350x395')


# Menu bar
menu_bar = Menu()
option_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Option", menu=option_menu)
option_menu.add_command(label="Standard Calculator", command=standard_calculator)
option_menu.add_separator()
option_menu.add_command(label="Scientific Calculator", command=scientific_calculator)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=exit_program)
window.config(menu=menu_bar)

# expression is used to store all mathematical expressions from the keys that the user press in the calculator
expression = ""
# text_entrybox used to hold a string and is used to display in the entrybox
text_entrybox = StringVar()


# to concatenate pressed buttons and to display them
def pressed_button(button_value):
    # 'global' to allow to modify the variable outside the function
    global expression
    expression += str(button_value)
    # .set used to display the mathematical operations to the entrybox
    text_entrybox.set(expression)


# to empty the entrybox and remove everything from the expression variable
def general_clear_entry():
    global expression
    expression = ''
    text_entrybox.set(expression)


# to output the answer of the mathematical operation to the entrybox
def equal():
    global expression
    final_result = str(eval(expression))
    text_entrybox.set(final_result)


# Function for the back space
def calculator_back_space():
    global expression
    initial_num = text_entrybox.get()
    new_num = initial_num[0:len(initial_num) - 1]
    expression = new_num
    text_entrybox.set(expression)


# to change the sign of the number
def math_plus_minus():
    global expression
    expression = str(-(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating cos
def math_cos():
    global expression
    expression = str(math.cos(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating cosh
def math_cosh():
    global expression
    expression = str(math.cosh(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating acosh
def math_acosh():
    global expression
    expression = str(math.acosh(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating tan
def math_tan():
    global expression
    expression = str(math.tan(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating tanh
def math_tanh():
    global expression
    expression = str(math.tanh(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating sin
def math_sin():
    global expression
    expression = str(math.sin(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating sinh
def math_sinh():
    global expression
    expression = str(math.sinh(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating asin
def math_asinh():
    global expression
    expression = str(math.asinh(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating ln
def math_ln():
    global expression
    expression = str(math.log(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating log2
def math_log2():
    global expression
    expression = str(math.log2(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating log10
def math_log10():
    global expression
    expression = str(math.log10(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating cube root
def math_cube_root():
    global expression
    expression = str(float(text_entrybox.get())**(1/3))
    text_entrybox.set(expression)


# Function for calculating exp
def math_exp():
    global expression
    expression = str(math.exp(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating sqrt
def math_sqrt():
    global expression
    expression = str(math.sqrt(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating pi
def math_pi():
    global expression
    expression = str(math.pi)
    text_entrybox.set(expression)


# Function for calculating pi2
def math_pi_2():
    global expression
    expression = str(math.tau)
    text_entrybox.set(expression)


# Function for calculating e
def math_e():
    global expression
    expression = str(math.e)
    text_entrybox.set(expression)


# Function for calculating rad
def math_rad():
    global expression
    expression = str(math.radians(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Function for calculating degree
def math_degree():
    global expression
    expression = str(math.degrees(float(text_entrybox.get())))
    text_entrybox.set(expression)


# Creating a 'entry frame' in the window
entry_frame = Frame()
entry_frame.pack()
# Entry box which will be on the top of the calculator
# and will display the numbers entered by the user as well as the output
output_widget = Entry(entry_frame, font=('Time New Roman', 20, 'bold'),  width=22,justify=RIGHT,bg='grey29', fg='white',
                      textvariable=text_entrybox)
output_widget.grid(row=0, column=0)
output_widget.grid(ipady=10)
output_widget.insert(0, "0")


# Creating a button frame where will be all the button
button_frame = Frame(bg='LightSkyBlue3')
button_frame.pack()
# Row 1 .. Buttons +-, ⌫, CE, C
plus_minus = Button(button_frame, text=chr(177), width=6, cursor="hand2", height=2,font=('Time New Roman', 16, 'bold'),
                    bg="LightSkyBlue3", fg='black', command=lambda: math_plus_minus())
plus_minus.grid(row=1, column=3, pady=1)

back_space = Button(button_frame, text='⌫', width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
                    bg="LightSkyBlue3", fg='black', command=lambda: calculator_back_space())
back_space.grid(row=1, column=0, pady=1)

button_clear_entry = Button(button_frame, text='CE', width=13, height=2, font=('Time New Roman', 16, 'bold'),
                            bg="LightSkyBlue3", fg='black',cursor="hand2", command=lambda:general_clear_entry())
button_clear_entry.grid(row=1, column=1, columnspan=2, pady=1)

# Row 2 .. Buttons 7 to 9 and +
num7 = Button(button_frame, text="7", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda:pressed_button(7))
num7.grid(row=2, column=0, pady=1)

num8 = Button(button_frame, text="8", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda: pressed_button(8))
num8.grid(row=2, column=1, pady=1)

num9 = Button(button_frame, text="9", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda: pressed_button(9))
num9.grid(row=2, column=2, pady=1)

plus = Button(button_frame, text='+', width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue3', fg='black', command=lambda: pressed_button('+'))
plus.grid(row=2, column=3, pady=1)

# Row 3 .. Buttons 4 to 6 and -
num4 = Button(button_frame, text="4", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda: pressed_button(4))
num4.grid(row=3, column=0, pady=1)

num5 = Button(button_frame, text="5", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda: pressed_button(5))
num5.grid(row=3, column=1, pady=1)

num6 = Button(button_frame, text="6", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black',command=lambda: pressed_button(6))
num6.grid(row=3, column=2, pady=1)

minus = Button(button_frame, text='-', width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
               bg='LightSkyBlue3', fg='black', command=lambda: pressed_button('-'))
minus.grid(row=3, column=3, pady=1)

# Row 4 .. Buttons 1 to 3 and *
num1 = Button(button_frame, text="1", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda: pressed_button(1))
num1.grid(row=4, column=0, pady=1)

num2 = Button(button_frame, text="2", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda: pressed_button(2))
num2.grid(row=4, column=1, pady=1)

num3 = Button(button_frame, text="3", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda: pressed_button(3))
num3.grid(row=4, column=2, pady=1)

times = Button(button_frame, text='*', width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
               bg='LightSkyBlue3', fg='black', command=lambda: pressed_button('*'))
times.grid(row=4, column=3, pady=1)

# Row 5.. Buttons 0 , /, ., =
zero = Button(button_frame, text="0", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue1', fg='black', command=lambda: pressed_button(0))
zero.grid(row=5, column=1, pady=1)

divide = Button(button_frame, text='/', width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
                bg='LightSkyBlue3', fg='black', command=lambda: pressed_button('/'))
divide.grid(row=5, column=3, pady=1)

decimal = Button(button_frame, text='.', width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
                 bg='LightSkyBlue3', fg='black', command=lambda: pressed_button('.'))
decimal.grid(row=5, column=0, pady=1)

equal_sign = Button(button_frame, text='=', width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
                    bg='LightSkyBlue3', fg='black', command=lambda: equal())
equal_sign.grid(row=5, column=2, pady=1)

# Scientific Part
# Row 6 .. Button sin, cos, tan, pi
sin = Button(button_frame, text="sin", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
             bg='LightSkyBlue4', fg='black', command=lambda: math_sin())
sin.grid(row=6, column=0, pady=1)

tan = Button(button_frame, text="tan", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
             bg='LightSkyBlue4', fg='black',command=lambda: math_tan())
tan.grid(row=6, column=1, pady=1)

cos = Button(button_frame, text="cos", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
             bg='LightSkyBlue4', fg='black', command=lambda: math_cos())
cos.grid(row=6, column=2, pady=1)

pi = Button(button_frame, text="π", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
            bg='LightSkyBlue4', fg='black', command=lambda: math_pi())
pi.grid(row=6, column=3, pady=1)

# Row 7 .. Button sinh, cosh, tanh, 2pi
sinh = Button(button_frame, text="sinh", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue4', fg='black', command=lambda: math_sinh())
sinh.grid(row=7, column=0, pady=1)

tanh = Button(button_frame, text="tanh", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue4', fg='black', command=lambda: math_tanh())
tanh.grid(row=7, column=1, pady=1)

cosh = Button(button_frame, text="cosh", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue4', fg='black', command=lambda: math_cosh())
cosh.grid(row=7, column=2, pady=1)

button_2pi = Button(button_frame, text="2π", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
                    bg='LightSkyBlue4', fg='black', command=lambda: math_pi_2())
button_2pi.grid(row=7, column=3, pady=1)

# Row 8 .. Button e, mod, exp, ln
e = Button(button_frame, text="e", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
           bg='LightSkyBlue4', fg='black', command=lambda: math_e())
e.grid(row=8, column=0, pady=1)

mod = Button(button_frame, text="mod", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
             bg='LightSkyBlue4', fg='black', command=lambda: pressed_button('%'))
mod.grid(row=8, column=1, pady=1)

exp = Button(button_frame, text="e^", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
             bg='LightSkyBlue4', fg='black', command=lambda: math_exp())
exp.grid(row=8, column=2, pady=1)

loge = Button(button_frame, text="ln", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'),
              bg='LightSkyBlue4', fg='black', command=lambda: math_ln())
loge.grid(row=8, column=3, pady=1)

# Row 9 .. Button asinh, acosh, deg, log2
asinh = Button(button_frame, text="asinh", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'), bg='LightSkyBlue4', fg='black', command=lambda: math_asinh())
asinh.grid(row=9, column=0, pady=1)

acosh = Button(button_frame, text="acosh", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'), bg='LightSkyBlue4', fg='black', command=lambda: math_acosh())
acosh.grid(row=9, column=1, pady=1)

deg = Button(button_frame, text="deg", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'), bg='LightSkyBlue4', fg='black', command=lambda: math_degree())
deg.grid(row=9, column=2, pady=1)

log2 = Button(button_frame, text="log2", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'), bg='LightSkyBlue4', fg='black', command=lambda: math_log2())
log2.grid(row=9, column=3, pady=1)

# Row 10 .. Button rad, sqrt, cuberoot, log10
rad = Button(button_frame, text="Rad", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'), bg='LightSkyBlue4', fg='black', command=lambda: math_rad())
rad.grid(row=10, column=0, pady=1)

sqrt = Button(button_frame, text="√", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'), bg='LightSkyBlue4', fg='black', command=lambda: math_sqrt())
sqrt.grid(row=10, column=1, pady=1)

cuberoot = Button(button_frame, text="3√", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'), bg='LightSkyBlue4', fg='black', command=lambda: math_cube_root())
cuberoot.grid(row=10, column=2, pady=1)

log10 = Button(button_frame, text="log10", width=6, height=2, cursor="hand2", font=('Time New Roman', 16, 'bold'), bg='LightSkyBlue4', fg='black', command=lambda: math_log10())
log10.grid(row=10, column=3, pady=1)

# Method to execute the code when we will run the program
window.mainloop()
