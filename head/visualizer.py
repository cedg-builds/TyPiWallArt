import tkinter as tk
from tkinter import messagebox

class Visualizer():

    cell_scale = 12
    buffer_scale = 3
    heightCount = 40
    widthCount = 120

    cells = []

    currentFrame = 0
    totalFrame = 5

    def paint(self):
        for wIndex in range(0, self.widthCount):
            for hIndex in range(0, self.heightCount):
                #left, top, width, height
                x = wIndex*(self.cell_scale + self.buffer_scale)
                y = hIndex * (self.cell_scale + self.buffer_scale)
                self.canvas.create_rectangle(x, y, x + self.cell_scale, y + self.cell_scale, fill="blue", outline = 'blue')


    def update_gui(self):
        """Function to update GUI elements."""
        # Example: Update a label's text
        current_time = tk.StringVar()
        current_time.set(current_time)  # Replace with actual data update logic
        self.currentFrame += 1
        print("Painting frame")
        if(self.currentFrame == self.totalFrame):
            print("Quitting")
            self.root.quit()
        
        self.paint()

        self.root.after(1000, self.update_gui)

    def play(self):

        # Create the main window
        self.root = tk.Tk()
        self.root.title("TyPi Visualizer")

        # Create a label to display updates
        self.canvas = tk.Canvas(self.root, width=(self.cell_scale + self.buffer_scale) *  self.widthCount, height=(self.cell_scale + self.buffer_scale) *  self.heightCount)
        self.update_gui()
        self.canvas.pack(pady=40, padx=40)

        self.root.after(1000, self.update_gui)


        # Start the periodic updates

        # Run the Tkinter event loop
        self.root.mainloop()


Visualizer().play()