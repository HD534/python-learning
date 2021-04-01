import matplotlib.pyplot as plt
import numpy as np
import tkinter

# change 
plt.switch_backend('TkAgg')

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot

# plt.savefig("mygraph.png")  # save as file