from tkinter import *
import Globals as G
import UI



def draw_spot(H, V, color, name, redraw):
    # Координаты для точки
    x1 = G.SCALE.get() + 10*G.SCALE.get() - H*G.SCALE.get() - G.SCALE.get()/5
    y1 = G.SCALE.get() + 10*G.SCALE.get() - V*G.SCALE.get() - G.SCALE.get()/5
    x2 = G.SCALE.get() + 10*G.SCALE.get() + G.SCALE.get()/5 - H*G.SCALE.get()
    y2 = G.SCALE.get() + 10*G.SCALE.get() + G.SCALE.get()/5 - V*G.SCALE.get()

    UI.canvas.create_oval(x1, y1, x2, y2, fill=color, tags="spot")
    # Индексирование в зависимости от плоскости проекции
    if color == "#f54242":
        text = f"{name}2"
    elif color == "#5af542":
        text = f"{name}1"
    elif color == "#424bf5":
        text = f"{name}3"
    else:
        text = name

    text_x = G.SCALE.get() + 9.7*G.SCALE.get() - H*G.SCALE.get()
    text_y = G.SCALE.get() + 9.7*G.SCALE.get() - V*G.SCALE.get()

    UI.canvas.create_text(text_x, text_y, text=text, tags="spot")

    if (redraw == False):
        point_data = {
            "H": H,
            "V": V,
            "color": color,
            "name": name,
            "x": text_x,
            "y": text_y
        }
        G.points.append(point_data)

def take_2_spots():
    # spot1 = spot_taker_1.get()
    # spot2 = spot_taker_2.get()
    # name = line_name_taker.get()
    pass

def redraw_spots():
    # Перерисовываем все сохраненные точки
    for pt in G.points:
        draw_spot(pt["H"], pt["V"], pt["color"], pt["name"], redraw=True)

def take_cords():
    X = float(UI.cords_taker_x.get())
    Y = float(UI.cords_taker_y.get())
    Z = float(UI.cords_taker_z.get())
    name = UI.spot_name_taker.get()

    print(f"Координаты получены: x = {X};\ny = {Y};\nz = {Z};\nимя точки - {name}")
    redraw = False

    draw_spot(X, Z, "#f54242", name, redraw)
    draw_spot(X, -Y, "#5af542", name, redraw)
    draw_spot(-Y, Z, "#424bf5", name, redraw)

def clear_spots():
    UI.canvas.delete("spot")
    UI.points.clear()

def resize_canvas(event=None):
    UI.canvas.config(bg="white", width=22*G.SCALE.get(), height=22*G.SCALE.get()) # Канвас...
    UI.canvas.delete("all")

    xp = G.SCALE.get()
    yp = G.SCALE.get()

    UI.canvas.create_line(xp+10*G.SCALE.get(), yp, xp+10*G.SCALE.get(), yp+20*G.SCALE.get(), width=3.5) # Основные линии координат
    UI.canvas.create_line(xp, yp+10*G.SCALE.get(), xp+20*G.SCALE.get(), yp+10*G.SCALE.get(), width=3.5)
    UI.canvas.create_line(xp, yp, xp+20*G.SCALE.get(), yp+20*G.SCALE.get()) # Диагональ

    for c in range (22): # сетка 
        UI.canvas.create_line(c*G.SCALE.get(), yp, c*G.SCALE.get(), 21*G.SCALE.get())
    for r in range (22):
        UI.canvas.create_line(xp, r*G.SCALE.get(), 21*G.SCALE.get(), r*G.SCALE.get())

    redraw_spots()