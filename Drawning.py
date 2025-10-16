from tkinter import *
import UI



def draw_spot(H, V, color, name, redraw):
    # Координаты для точки (овала)
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
            "name": text,
            "x": text_x,
            "y": text_y
        }
        UI.points.append(point_data)

def draw_line(X_spot_1, Y_spot_1, Z_spot_1, X_spot_2, Y_spot_2, Z_spot_2, redraw):
    UI.canvas.create_line(
        UI.SCALE.get() + 10*UI.SCALE.get() - X_spot_1[0]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - X_spot_1[1]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - X_spot_2[0]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - X_spot_2[1]*UI.SCALE.get(),
        fill="#f54242",
        width=2,
        tags="line"
    )

    UI.canvas.create_line(
        UI.SCALE.get() + 10*UI.SCALE.get() - Y_spot_1[0]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - Y_spot_1[1]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - Y_spot_2[0]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - Y_spot_2[1]*UI.SCALE.get(),
        fill="#5af542",
        width=2,
        tags="line"
    )

    UI.canvas.create_line(
        UI.SCALE.get() + 10*UI.SCALE.get() - Z_spot_1[0]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - Z_spot_1[1]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - Z_spot_2[0]*UI.SCALE.get(),
        UI.SCALE.get() + 10*UI.SCALE.get() - Z_spot_2[1]*UI.SCALE.get(),
        fill="#424bf5",
        width=2,
        tags="line"
    )

    if (redraw == False):
        line_data = {
            "X1": X_spot_1,
            "Y1": Y_spot_1,
            "Z1": Z_spot_1,
            "X2": X_spot_2,
            "Y2": Y_spot_2,
            "Z2": Z_spot_2
        }
        UI.lines.append(line_data)

def take_spot_cords():
    X = float(UI.cords_taker_x.get())
    Y = float(UI.cords_taker_y.get())
    Z = float(UI.cords_taker_z.get())
    name = UI.spot_name_taker.get()

    print(f"Координаты получены: x = {X};\ny = {Y};\nz = {Z};\nимя точки - {name}")
    redraw = False

    draw_spot(X, Z, "#f54242", name, redraw)
    draw_spot(X, -Y, "#5af542", name, redraw)
    draw_spot(-Y, Z, "#424bf5", name, redraw)

def take_line_cords():
    spot1 = UI.spot_taker_1.get()
    X_spot_1 = []
    Y_spot_1 = []
    Z_spot_1 = []

    spot2 = UI.spot_taker_2.get()
    X_spot_2 = []
    Y_spot_2 = []
    Z_spot_2 = []

    for i in UI.points:
        print(i)

        if spot1+"2" == i['name']:
            X_spot_1 = [i['H'], i['V']]
        elif spot1+"1" == i['name']:
            Y_spot_1 = [i['H'], i['V']]
        elif spot1+"3" == i['name']:
            Z_spot_1 = [i['H'], i['V']]
        elif spot2+"2" == i['name']:
            X_spot_2 = [i['H'], i['V']]
        elif spot2+"1" == i['name']:
            Y_spot_2 = [i['H'], i['V']]
        elif spot2+"3" == i['name']:
            Z_spot_2 = [i['H'], i['V']]

    draw_line(X_spot_1, Y_spot_1, Z_spot_1, X_spot_2, Y_spot_2, Z_spot_2, False)

def redraw_spots():
    for pt in UI.points:
        draw_spot(pt["H"], pt["V"], pt["color"], pt["name"][:-1], redraw=True)

def redraw_lines():
    for ln in UI.lines:
        draw_line(ln["X1"], ln["Y1"], ln["Z1"], ln["X2"], ln["Y2"], ln["Z2"], redraw=True)

def clear_spots():
    UI.canvas.delete("spot")
    UI.points.clear()

def clear_lines():
    UI.canvas.delete("line")
    UI.lines.clear()

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
    redraw_lines()



def pick_panel(list_of_panels, picked_panel):
    for i in list_of_panels:
        i.pack_forget()

    picked_panel.pack(anchor="se", side="bottom", padx=UI.SCALE.get(), pady=UI.SCALE.get()/5)