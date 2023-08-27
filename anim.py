import tkinter as tk

class CoordinateSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coordinate System")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        
        self.x_min_label = tk.Label(root, text="Min X:")
        self.x_min_label.pack()
        
        self.x_min_entry = tk.Entry(root)
        self.x_min_entry.pack()
        
        self.plot_button = tk.Button(root, text="Plot", command=self.plot_point)
        self.plot_button.pack()
        
        self.points = []
        
    def draw_coordinate_system(self):
        self.canvas.create_line(50, 350, 350, 350, width=2)  # X-axis
        self.canvas.create_line(50, 350, 50, 50, width=2)    # Y-axis
        
        # Additional code to draw ticks, labels, etc.
        
    def plot_point(self):
        x_min = float(self.x_min_entry.get())
        x_value = float(input("Enter x-coordinate of the point: "))
        y_value = float(input("Enter y-coordinate of the point: "))
        
        x_pixel = 50 + (x_value - x_min) * 25  # Adjust scale and offset
        y_pixel = 350 - y_value * 25            # Adjust scale
        
        point = self.canvas.create_oval(x_pixel - 3, y_pixel - 3, x_pixel + 3, y_pixel + 3, fill="red")
        self.points.append(point)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateSystemApp(root)
    app.draw_coordinate_system()
    root.mainloop()

