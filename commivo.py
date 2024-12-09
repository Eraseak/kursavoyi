import tkinter as tk
from tkinter import messagebox
import itertools
import math
from random import randint

points = []

def add_point(event):
    x, y = event.x, event.y
    points.append((x, y))
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
    update_info()

def rand_gen():
    clear_points()
    n = randint(2, 8)
    for i in range(n):
        x, y = randint(50, 350), randint(50, 350)
        points.append((x, y))
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
        update_info()

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * 2 + (p1[1] - p2[1]) * 2)

def solve_tsp():
    if len(points) < 2:
        messagebox.showerror("Ошибка", "Добавьте хотя бы два города.")
        return

    best_route = None
    min_distance = float("inf")

    for perm in itertools.permutations(points):
        current_distance = sum(distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))

        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm

    draw_route(best_route)
    distance_label.config(text=f"Общая длина маршрута: {min_distance:.2f}")

def draw_route(route):
    canvas.delete("line")
    for i in range(len(route) - 1):
        x1, y1 = route[i]
        x2, y2 = route[i + 1]
        canvas.create_line(x1, y1, x2, y2, fill="blue", tags="line", width=2)
        canvas.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5, fill="black")

    start_x, start_y = route[0]
    end_x, end_y = route[-1]
    canvas.create_oval(start_x - 6, start_y - 6, start_x + 6, start_y + 6, fill="green")
    canvas.create_oval(end_x - 6, end_y - 6, end_x + 6, end_y + 6, fill="yellow")

def clear_points():
    points.clear()
    canvas.delete("all")
    distance_label.config(text="Общая длина маршрута: 0")
    update_info()

def update_info():
    points_label.config(text=f"Количество городов: {len(points)}")

root = tk.Tk()
root.title("Игра: Задача Коммивояжера")

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

canvas.bind("<Button-1>", add_point)

solve_button = tk.Button(root, text="Найти короткий путь", command=solve_tsp)
solve_button.pack(side="left")

solve_button = tk.Button(root, text="rand gen", command=rand_gen)
solve_button.pack(side="left")

clear_button = tk.Button(root, text="Очистить все точки", command=clear_points)
clear_button.pack(side="right")

points_label = tk.Label(root, text="Количество городов: 0")
points_label.pack()

distance_label = tk.Label(root, text="Общая длина маршрута: 0")
distance_label.pack()

root.mainloop()