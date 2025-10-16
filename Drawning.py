from tkinter import *
import UI



def draw_spot(H, V, color, name, redraw):
    # Координаты для точки
    x1 = UI.SCALE.get() + 10*UI.SCALE.get() - H*UI.SCALE.get() - UI.SCALE.get()/5
    y1 = UI.SCALE.get() + 10*UI.SCALE.get() - V*UI.SCALE.get() - UI.SCALE.get()/5
    x2 = UI.SCALE.get() + 10*UI.SCALE.get() + UI.SCALE.get()/5 - H*UI.SCALE.get()
    y2 = UI.SCALE.get() + 10*UI.SCALE.get() + UI.SCALE.get()/5 - V*UI.SCALE.get()

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

    text_x = UI.SCALE.get() + 9.7*UI.SCALE.get() - H*UI.SCALE.get()
    text_y = UI.SCALE.get() + 9.7*UI.SCALE.get() - V*UI.SCALE.get()

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
        UI.points.append(point_data)

def take_2_spots():
    # spot1 = spot_taker_1.get()
    # spot2 = spot_taker_2.get()
    # name = line_name_taker.get()
    pass

def redraw_spots():
    # Перерисовываем все сохраненные точки
    for pt in UI.points:
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
    UI.canvas.config(bg="white", width=22*UI.SCALE.get(), height=22*UI.SCALE.get()) # Канвас...
    UI.canvas.delete("all")

    xp = UI.SCALE.get()
    yp = UI.SCALE.get()

    UI.canvas.create_line(xp+10*UI.SCALE.get(), yp, xp+10*UI.SCALE.get(), yp+20*UI.SCALE.get(), width=3.5) # Основные линии координат
    UI.canvas.create_line(xp, yp+10*UI.SCALE.get(), xp+20*UI.SCALE.get(), yp+10*UI.SCALE.get(), width=3.5)
    UI.canvas.create_line(xp, yp, xp+20*UI.SCALE.get(), yp+20*UI.SCALE.get()) # Диагональ

    for c in range (22): # сетка 
        UI.canvas.create_line(c*UI.SCALE.get(), yp, c*UI.SCALE.get(), 21*UI.SCALE.get())
    for r in range (22):
        UI.canvas.create_line(xp, r*UI.SCALE.get(), 21*UI.SCALE.get(), r*UI.SCALE.get())

    redraw_spots()