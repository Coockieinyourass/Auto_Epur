from tkinter import *



root = Tk() # Корневой объект - окно
root.title("Auto Epur maker")
root.geometry("1400x1200")

try:
    icon = PhotoImage(file = "2914917.png")
    root.iconphoto(False, icon)
except (TclError):
    pass

SCALE = IntVar(value=40)
XPADDING = SCALE
YPADDING = SCALE
points = []



def draw_spot(H, V, color, name):
    # Координаты для точки
    x1 = XPADDING.get() + 10*SCALE.get() - H*SCALE.get() - SCALE.get()/5
    y1 = YPADDING.get() + 10*SCALE.get() - V*SCALE.get() - SCALE.get()/5
    x2 = XPADDING.get() + 10*SCALE.get() + SCALE.get()/5 - H*SCALE.get()
    y2 = YPADDING.get() + 10*SCALE.get() + SCALE.get()/5 - V*SCALE.get()

    canvas.create_oval(x1, y1, x2, y2, fill=color, tags="spot")
    # Индексирование в зависимости от плоскости проекции
    if color == "#f54242":
        text = f"{name}2"
    elif color == "#5af542":
        text = f"{name}1"
    elif color == "#424bf5":
        text = f"{name}3"
    else:
        text = name

    text_x = XPADDING.get() + 9.7*SCALE.get() - H*SCALE.get()
    text_y = YPADDING.get() + 9.7*SCALE.get() - V*SCALE.get()

    canvas.create_text(text_x, text_y, text=text, tags="spot")

    # Сохраняем данные о точке
    point_data = {
        "H": H,
        "V": V,
        "color": color,
        "name": name,
        "x": text_x,
        "y": text_y
    }
    points.append(point_data)

def redraw_points():
    # Удаляем старые точки
    canvas.delete("spot")
    # Перерисовываем все сохраненные точки
    for pt in points:
        draw_spot(pt["H"], pt["V"], pt["color"], pt["name"])

def take_cords():
    X = float(cords_taker_x.get())
    Y = float(cords_taker_y.get())
    Z = float(cords_taker_z.get())
    name = spot_name_taker.get()

    print(f"Координаты получены: x = {X};\ny = {Y};\nz = {Z};\nимя точки - {name}")

    draw_spot(X, Z, "#f54242", name)
    draw_spot(X, -Y, "#5af542", name)
    draw_spot(-Y, Z, "#424bf5", name)

def clear_spots():
    canvas.delete("spot")

def resize_canvas(event=None):
    canvas.config(bg="white", width=22*SCALE.get(), height=22*SCALE.get()) # Канвас...
    canvas.delete("all")

    canvas.create_line(XPADDING.get()+10*SCALE.get(), YPADDING.get(), XPADDING.get()+10*SCALE.get(), YPADDING.get()+20*SCALE.get(), width=3.5) # Основные линии координат
    canvas.create_line(XPADDING.get(), YPADDING.get()+10*SCALE.get(), XPADDING.get()+20*SCALE.get(), YPADDING.get()+10*SCALE.get(), width=3.5)
    canvas.create_line(XPADDING.get(), YPADDING.get(), XPADDING.get()+20*SCALE.get(), YPADDING.get()+20*SCALE.get()) # Диагональ

    for c in range (22): # сетка 
        canvas.create_line(c*SCALE.get(), YPADDING.get(), c*SCALE.get(), 21*SCALE.get())
    for r in range (22):
        canvas.create_line(XPADDING.get(), r*SCALE.get(), 21*SCALE.get(), r*SCALE.get())

    redraw_points()



frame_optns = Frame(root)
frame_optns.pack(anchor="ne", padx=XPADDING.get(), pady=YPADDING.get()/5)

grid_scale = Scale(frame_optns, orient=HORIZONTAL, length=300, from_=10.0, to=50.0, variable=SCALE, command=resize_canvas)
grid_scale.pack()



frame_btns = Frame(root)
frame_btns.pack(anchor="se", side="bottom", padx=XPADDING.get(), pady=YPADDING.get()/5)

Clear_btn  = Button(frame_btns, text="Clear", command=clear_spots)
Clear_btn.pack(side="left")

Enter_btn = Button(frame_btns, text="Enter", command=take_cords)
Enter_btn.pack(side="left")



frame_z = Frame(root)
frame_z.pack(anchor="se", side="bottom", padx=XPADDING.get(), pady=YPADDING.get()/5)
z_label = Label(frame_z, text="Z = ")
z_label.pack(side="left")
cords_taker_z = Entry(frame_z)
cords_taker_z.pack(side="left")

frame_y = Frame(root)
frame_y.pack(anchor="se", side="bottom", padx=XPADDING.get(), pady=YPADDING.get()/5)
y_label = Label(frame_y, text="Y = ")
y_label.pack(side="left")
cords_taker_y = Entry(frame_y)
cords_taker_y.pack(side="left")

frame_x = Frame(root)
frame_x.pack(anchor="se", side="bottom", padx=XPADDING.get(), pady=YPADDING.get()/5)
x_title = Label(frame_x, text="X = ")
x_title.pack(side="left")
cords_taker_x = Entry(frame_x)
cords_taker_x.pack(side="left")

frame_spot_name = Frame(root)
frame_spot_name.pack(anchor="se", side="bottom", padx=XPADDING.get(), pady=YPADDING.get()/5)
spot_name_title = Label(frame_spot_name, text="Имя точки: ")
spot_name_title.pack(side="left")
spot_name_taker = Entry(frame_spot_name)
spot_name_taker.pack(side="left")



canvas = Canvas(bg="white", width=22*SCALE.get(), height=22*SCALE.get()) # Канвас...
canvas.pack(anchor="sw")

canvas.create_line(XPADDING.get()+10*SCALE.get(), YPADDING.get(), XPADDING.get()+10*SCALE.get(), YPADDING.get()+20*SCALE.get(), width=3.5) # Основные линии координат
canvas.create_line(XPADDING.get(), YPADDING.get()+10*SCALE.get(), XPADDING.get()+20*SCALE.get(), YPADDING.get()+10*SCALE.get(), width=3.5)
canvas.create_line(XPADDING.get(), YPADDING.get(), XPADDING.get()+20*SCALE.get(), YPADDING.get()+20*SCALE.get()) # Диагональ

for c in range (22): # сетка 
    canvas.create_line(c*SCALE.get(), YPADDING.get(), c*SCALE.get(), 21*SCALE.get())
for r in range (22):
    canvas.create_line(XPADDING.get(), r*SCALE.get(), 21*SCALE.get(), r*SCALE.get())


root.mainloop() # чтобы не закрывалось сразу