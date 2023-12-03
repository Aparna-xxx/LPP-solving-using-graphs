import tkinter as tk

def submit_values():

    x_input_values = [int(x_entry_vars[i].get()) if x_entry_vars[i].get() else 0 for i in range(num_entries.get())]
    #print("Entered values:", x_input_values)

    y_input_values = [int(y_entry_vars[i].get()) if y_entry_vars[i].get() else 0 for i in range(num_entries.get())]
    #print("Entered values:", y_input_values)

    rhs_input_values = [int(rhs_entry_vars[i].get()) if rhs_entry_vars[i].get() else 0 for i in range(num_entries.get())]

    #obj_input_values = [obj_entry_vars[i].get() for i in range(2)]
    obj_input_values = [int(obj_entry_vars[i].get()) if obj_entry_vars[i].get() else 0 for i in range(2)]


    with open('output_file.py', 'w') as file:
        file.write("x_input_values = " + str(x_input_values))
        file.write("\n")
        file.write("y_input_values = " + str(y_input_values))
        file.write("\n")
        file.write("rhs_input_values = " + str(rhs_input_values))
        file.write("\n")
        file.write("obj_input_values = " + str(obj_input_values))

# Create the main window
root = tk.Tk()
root.title("Solve LPP - Graphical method")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# Variable to store the number of entry fields
num_entries = tk.IntVar()

# Function to create entry fields based on user input
def create_entry_fields():
    num = num_entries.get()

    # Destroy any existing entry fields
    for widget in frame.winfo_children():
        widget.destroy()

    # Create new entry fields
    for i in range(num):
        label = tk.Label(frame, text=f"Entry {i + 1}:")
        label.grid(row=i, column=0, padx=5, pady=5)

        label = tk.Label(frame, text=f"X Entry:")
        label.grid(row=i, column=1, padx=5, pady=5)

        entry_var = tk.StringVar()
        x_entry_vars.append(entry_var)

        entry = tk.Entry(frame, textvariable=entry_var)
        entry.grid(row=i, column=2, padx=5, pady=5)

        label = tk.Label(frame, text=f"Y Entry:")
        label.grid(row=i, column=3, padx=5, pady=5)

        y_entry_var = tk.StringVar()
        y_entry_vars.append(y_entry_var)

        y_entry = tk.Entry(frame, textvariable=y_entry_var)
        y_entry.grid(row=i, column=4, padx=5, pady=5)

        label = tk.Label(frame, text=f"RHS Entry:")
        label.grid(row=i, column=5, padx=5, pady=5)

        rhs_entry_var = tk.StringVar()
        rhs_entry_vars.append(rhs_entry_var)

        rhs_entry = tk.Entry(frame, textvariable=rhs_entry_var)
        rhs_entry.grid(row=i, column=6, padx=5, pady=5)

#editing from here
    label = tk.Label(frame, text=f"Obj Entry 1:")
    label.grid(row=i+1, column=2, padx=5, pady=5)

    obj_entry_var1 = tk.StringVar()
    obj_entry_vars.append(obj_entry_var1)

    obj_entry1 = tk.Entry(frame, textvariable=obj_entry_var1)
    obj_entry1.grid(row=i+1, column=3, padx=5, pady=5)

    label = tk.Label(frame, text=f"Obj Entry 2:")
    label.grid(row=i+1, column=4, padx=5, pady=5)

    obj_entry_var2 = tk.StringVar()
    obj_entry_vars.append(obj_entry_var2)

    obj_entry2 = tk.Entry(frame, textvariable=obj_entry_var2)
    obj_entry2.grid(row=i+1, column=5, padx=5, pady=5)
        #editing ends here


# Label and entry for the number of input fields
num_label = tk.Label(root, text="Number of Constraints:")
num_label.pack(pady=5)

num_entry = tk.Entry(root, textvariable=num_entries)
num_entry.pack(pady=5)

# Button to create entry fields
create_button = tk.Button(root, text="Create Entry Fields", command=create_entry_fields)
create_button.pack(pady=10)

# Frame to contain dynamically generated entry fields
frame = tk.Frame(root)
frame.pack()

# Button to submit values
submit_button = tk.Button(root, text="Submit", command=submit_values)
submit_button.pack(pady=10)



# List to store StringVar objects associated with entry fields
x_entry_vars = []
y_entry_vars = []
rhs_entry_vars =[]
obj_entry_vars = []


# Start the Tkinter event loop
root.mainloop()
