import tkinter as tk
import math


class PlayGame():
    
    first_circle = True
    def __init__(self, root):
        self.root = root
        self.root.title("Fill the box")
        self.root.geometry('400x400')
        self.root.resizable(False, False)
        self.create_canvas()

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg='lightblue')
        self.canvas.pack(expand=1, fill='both')
        self.circle_ids = {}
        self.id = 0
        self.d = []  # list with the distance between the existing circles and the new one
        self.score_number = 0
        self.score = tk.StringVar()
        self.score.set(str(0))
        self.l = tk.Label(self.canvas, textvariable=self.score, font='Calibri 16 bold italic', fg='blue')
        self.l.pack(side='top', fill='x')
        self.canvas.create_line(0, 32, 400, 32, fill='red')
        
        self.canvas.bind('<1>', self.place_outline)        
        self.canvas.bind('<ButtonRelease-1>', self.place_circle)
        self.canvas.bind('<2>', self.place_first_circle)
        self.canvas.bind('<3>', self.clear_canvas)
        
    def place_outline(self, event):
        self.outx = event.x
        self.outy = event.y
        self.id = self.canvas.create_oval(event.x-25, event.y-25, event.x+25, event.y+25, outline='red')
        
    def delete_outline(self):  ## Deletes the outlined circle if the user moves the mouse while the l-click is pressed
        self.canvas.delete(self.id)
        
    def place_first_circle(self, event):   # Creates the first circle (with middle click)
        if PlayGame.first_circle == True and (event.x >=25 and event.x <=375) and (event.y >=57 and event.y <=375):
            self.canvas.create_oval(event.x-25, event.y-25, event.x+25, event.y+25, fill='orange', outline='red')
            self.score_number += 10
            self.score.set(str(self.score_number))
            self.circle_ids[self.id] = [event.x, event.y]
            PlayGame.first_circle = False
            
    def place_circle(self, event):
        if self.outx == event.x and self.outy == event.y: # checks if the user moves the mouse while pressing
            for key in self.circle_ids:
                self.d.append(math.sqrt((event.x-self.circle_ids[key][0])**2 + (event.y-self.circle_ids[key][1])**2))

            if min(self.d) >= 50 and (event.x >=25 and event.x <=375) and (event.y >=57 and event.y <=375):
                self.canvas.create_oval(event.x-25, event.y-25, event.x+25, event.y+25, fill='orange', outline='red')
                self.score_number += 10
                self.score.set(str(self.score_number))               
                self.circle_ids[self.id] = [event.x, event.y]
            else:
                self.delete_outline()
                self.score_number -= 5
                self.score.set(str(self.score_number))
        else:
            self.delete_outline()
        
        while min(self.d) < 50:
            self.d.remove(min(self.d))
            break

    def clear_canvas(self, event):
        self.canvas.delete('all')
        self.score.set(str(0))
        self.circle_ids = {}
        self.id = 0
        self.d = []  # list with the distance between the existing circles and the new one
        self.score_number = 0
        PlayGame.first_circle = True


root = tk.Tk()
PlayGame(root)
root.mainloop()