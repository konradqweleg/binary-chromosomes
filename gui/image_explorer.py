import tkinter as tk
from copy import deepcopy
from tkinter import messagebox
from PIL import Image, ImageTk
import os


class ImageExplorer:
    def __init__(self, root, result_time, best_chromosome_value, last_fitness_value, number_runs_program):
        self.root = root
        self.root.title("Image Explorer")

        self.number_runs_program = number_runs_program
        self.images = []
        self.current_image_index = 0

        self.label = tk.Label(root)
        self.label.pack(pady=10)

        self.result_label = tk.Label(root, text=f'Calculation time: {round(result_time, 3)}s')
        self.result_label.pack(padx=20, pady=20)
        self.result_label = tk.Label(root, text=f'Number runs: {number_runs_program+1}')
        self.result_label.pack(padx=20, pady=20)

        rounded_strings = [f"{round(num, 3)}" for num in best_chromosome_value]
        result_string = ", ".join(rounded_strings)

        self.best_chromosome_value_label = tk.Label(root, text=f'Result: {result_string}')
        self.best_chromosome_value_label.pack(padx=20, pady=20)

        self.fitness_result_label = tk.Label(root, text=f'Fitness Result: {round(last_fitness_value, 3)}')
        self.fitness_result_label.pack(padx=20, pady=20)

        self.previous_button = tk.Button(root, text="Previous", command=self.show_previous_image)
        self.previous_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.next_button = tk.Button(root, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, padx=20, pady=20)
        self.root =tk.Canvas(root, width=400, height=400)
        self.load_images()



    def load_images(self):
        folder_path = 'results'
        self.images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
                       f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        if not self.images:
            messagebox.showwarning("No Images", "No images found in the selected folder.")
            return

        self.current_image_index = 0
        self.show_image()

    def show_image(self):
        image_path = self.images[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((800, 500))
        self.tk_image = ImageTk.PhotoImage(image)
        self.label.config(image=self.tk_image)

    def show_previous_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_image()

    def show_next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_image()


if __name__ == "__main__":
    root = tk.Tk()
    explorer = ImageExplorer(
        root=root,
        result_time=3.456,
        best_chromosome_value=[1.234, 5.678, 9.012],
        last_fitness_value=0.123,
        number_runs_program=0
    )
    root.mainloop()
