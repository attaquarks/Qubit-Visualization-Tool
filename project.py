import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
import numpy as np
import tkinter
from tkinter import LEFT, END, DISABLED, NORMAL
import warnings

warnings.filterwarnings('ignore')

# Define Window
root = tkinter.Tk()
root.title('Qubit Specs')


# Set the icon
root.iconbitmap(default ='logo.ico')
root.geometry('415x490')
root.resizable(0,0)


# Define colours and fonts
background = '#6b6353'
buttons = '#535b6b'
special = '#95a3c0'
button_font = ('Arial',20)
display_font = ('Arial', 34)


# Initialize the Quantum circuit
def initialize_circuit():
    global circuit
    circuit = QuantumCircuit(1)
    
initialize_circuit()
theta = 0


# Define Functions

# Function to display gates
def display_gate(gate_input):
    """
    Adds a corresponding gate notation in the display to track the operations.
    If the number of operations reach ten, all gate buttons are disabled.
    """
    # Insert the defined gate
    display.insert(END, gate_input)
    
    # Check if the number of operations has reached ten, if yes, disable all the gate buttons
    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates = list(input_gates)
    search_word = ["R", "D"]
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates_pressed -= sum(count_double_valued_gates)
    if num_gates_pressed == 10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, h_gate]
        for gate in gates:
            gate.config(state = DISABLED)


# Funtion of Clear button
def clear(circuit):
    """
    Clears the display!
    Checks if the gate buttons are disabled, if so, enables the buttons
    """
    # Clear the display
    display.delete(0, END)
    
    # Reset the circuit to initial state |0>
    initialize_circuit()
    
    # Enable the buttons
    if x_gate['state'] == DISABLED:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, h_gate]
        for gate in gates:
            gate.config(state=NORMAL)


# Function of About Button
def about():
    """
    Displays the info about the project!
    """
    info = tkinter.Tk()
    info.title('About')
    info.geometry('620x480')
    info.resizable(0,0)
    
    text = tkinter.Text(info, height=24, width=24)
    
    # Create label
    label = tkinter.Label(info, text="About Qubit Specs")
    label.config(font = ("Arial, 18"))
    
    text_to_display = """
    About: Visualization tool for Single Qubit Rotation on Bloch Sphere
    
    Created by : Harris & Atta
    Platforms used : Python, Tkinter, Qiskit
    
    Info about the gate buttons and corresponding qiskit commands:
    
    X = flips the Qubit state by rotating it around X-axis by PI radians
    Y = flips the Qubit state by rotating it around Y-axis by PI radians
    Z = flips the Qubit state by rotating it around Z-axis by PI radians
    Rx = parameterized ratation about the X-axis
    Ry = parameterized ratation about the Y-axis
    Rz = parameterized ratation about the Z-axis
    S = rotates the state vestor about Z-axis by PI/2 radians
    T = rotates the state vestor about Z-axis by PI/4 radians
    Sd = rotates the state vestor about Z-axis by -PI/2 radians
    Td = rotates the state vestor about Z-axis by -PI/4 radians
    H = creates the state of Superposition
    
    For Rx, Ry and Rz:
    Allowed range for theta (rotation angle) is [-2PI,2PI]
    
    In case of a visualization Error, the app closes automatically.
    This indicates that visualization of your circuit is not possible.
    
    At a time, only ten operations can be visualized.
    """
    label.pack()
    text.pack(fill='both', expand=True)
    
    # Insert the text
    text.insert(END, text_to_display)
    
    # Run the loop
    info.mainloop()


# Function of Visualize button
def visualize(circuit, window):
    """
    Visualizes the single qubit rotations corresponding to applied gates in a separate tkinter window.
    Handles any possible visualization Error.
    """
    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()


# Define the Parameterized Gates Layout

# Function to change_theta
def change_theta(num, window, circuit, key):
    """
    Changes the Global variable theta and destroys the window
    """
    global theta
    theta = num * np.pi
    if key == 'x':
        circuit.rx(theta,0)
        theta = 0
    elif key == 'y':
        circuit.ry(theta,0)
        theta = 0
    elif key == 'z':
        circuit.rz(theta,0)
        theta = 0
    window.destroy()

# Funtion to define the values of theta
def user_input(circuit, key):
    """
    Takes the user input for rotation angle (theta) for parameterized rotation  of gates Rx, Ry, Rz.
    """
    #Initialize and define the window
    input = tkinter.Tk()
    input.title('Get theta')
    input.geometry('415x180')
    input.resizable(0,0)
    
    val1 = tkinter.Button(input, height=3, width=12, bg=buttons, font=("Arial",10), text='PI/4', command=lambda: change_theta(0.25, input, circuit, key))
    val1.grid(row=0, column=0)
    
    val2 = tkinter.Button(input, height=3, width=12, bg=buttons, font=("Arial",10), text='PI/2', command=lambda: change_theta(0.5, input, circuit, key))
    val2.grid(row=0, column=1)
    
    val3 = tkinter.Button(input, height=3, width=12, bg=buttons, font=("Arial",10), text='PI', command=lambda: change_theta(1.0, input, circuit, key))
    val3.grid(row=0, column=2)
    
    val4 = tkinter.Button(input, height=3, width=12, bg=buttons, font=("Arial",10), text='2PI', command=lambda: change_theta(2.0, input, circuit, key))
    val4.grid(row=0, column=3, sticky='w')
    
    nval1 = tkinter.Button(input, height=3, width=12, bg=buttons, font=("Arial",10), text='-PI/4', command=lambda: change_theta(-0.25, input, circuit, key))
    nval1.grid(row=1, column=0)
    
    nval2 = tkinter.Button(input, height=3, width=12, bg=buttons, font=("Arial",10), text='-PI/2', command=lambda: change_theta(-0.5, input, circuit, key))
    nval2.grid(row=1, column=1)
    
    nval3 = tkinter.Button(input, height=3, width=12, bg=buttons, font=("Arial",10), text='-PI', command=lambda: change_theta(-1.0, input, circuit, key))
    nval3.grid(row=1, column=2)
    
    nval4 = tkinter.Button(input, height=3, width=12, bg=buttons, font=("Arial",10), text='-2PI', command=lambda: change_theta(-2.0, input, circuit, key))
    nval4.grid(row=1, column=3, sticky='w')
    
    text = tkinter.Text(input, height=4, width=8, bg="light cyan")
    note = """
    SELECT THE VALUE FOR theta 
    The value has the range [-2PI, 2PI] """
    text.grid(sticky='we', columnspan=4)
    text.insert(END, note)
    
    # Run the loop
    input.mainloop()


# Define Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both', expand=True)


# Define the Layout

# Define the display frame layout
display = tkinter.Entry (display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify=LEFT)
display.pack(padx=3, pady=4)

# Define the button frame layout

# Define the first row of buttons
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X', command=lambda: [display_gate('X'), circuit.x(0)])
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y', command=lambda: [display_gate('Y'), circuit.y(0)])
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z', command=lambda: [display_gate('Z'), circuit.z(0)])
x_gate.grid(row=0, column=0, ipadx=48, pady=1, sticky='we')
y_gate.grid(row=0, column=1, ipadx=48, pady=1, sticky='we')
z_gate.grid(row=0, column=2, ipadx=48, pady=1, sticky='we')

# Define the second row of buttons
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RX', command=lambda: [display_gate('Rx'), user_input(circuit, 'x')])
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RY', command=lambda: [display_gate('Ry'), user_input(circuit, 'y')])
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RZ', command=lambda: [display_gate('Rz'), user_input(circuit, 'z')])
Rx_gate.grid(row=1, column=0, columnspan=1, pady=1, sticky='we')
Ry_gate.grid(row=1, column=1, columnspan=1, pady=1, sticky='we')
Rz_gate.grid(row=1, column=2, columnspan=1, pady=1, sticky='we')

# Define the third row of buttons
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S', command=lambda: [display_gate('S'), circuit.s(0)])
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD', command=lambda: [display_gate('SD'), circuit.sdg(0)])
h_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H', command=lambda: [display_gate('H'), circuit.h(0)])
s_gate.grid(row=2, column=0, columnspan=1, pady=1, sticky='we')
sd_gate.grid(row=2, column=1, columnspan=1, pady=1, sticky='we')
h_gate.grid(row=2, column=2, rowspan=2, pady=1, sticky='wens')

# Define the fifth row of buttons
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T', command=lambda: [display_gate('S'), circuit.t(0)])
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD', command=lambda: [display_gate('SD'), circuit.tdg(0)])
t_gate.grid(row=3, column=0, columnspan=1, pady=1, sticky='we')
td_gate.grid(row=3, column=1, columnspan=1, pady=1, sticky='we')

# Define the Visualize and Clear buttons
visualize_button = tkinter.Button(button_frame, font=button_font, bg=special, text='Visualize', command=lambda: visualize(circuit, root))
clear_button = tkinter.Button(button_frame, font=button_font, bg=special, text='Clear', command=lambda: clear(circuit))
visualize_button.grid(row=4, column=0, columnspan=2, ipadx=5, pady=1, sticky='we')
clear_button.grid(row=4, column=2, columnspan=1, pady=1, sticky='we')

# Define the About button
about_button = tkinter.Button(button_frame, font=button_font, bg=special, text='About', command=about)
about_button.grid(row=5, column=0, columnspan=3, sticky='we')

# Define the Quit button
quit = tkinter.Button(button_frame, font=button_font, bg=special, text='Quit', command=root.destroy)
quit.grid(row=6, column=0, columnspan=3, sticky='we')


# Run the main loop
root.mainloop()

 