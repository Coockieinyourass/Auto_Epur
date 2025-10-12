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



def draw_spot(H, V, color, name):
    canvas.create_oval(XPADDING.get() + 10*SCALE.get() - H*SCALE.get() - SCALE.get()/5, # Генерация точки по x и y координатам
                        YPADDING.get() + 10*SCALE.get() - V*SCALE.get() - SCALE.get()/5, 
                        XPADDING.get() + 10*SCALE.get() - H*SCALE.get() + SCALE.get()/5,
                        YPADDING.get() + 10*SCALE.get() - V*SCALE.get() + SCALE.get()/5,
                        fill=color, tags="spot")
    if(color == "#f54242"):
        canvas.create_text(XPADDING.get() + 9.7*SCALE.get() - H*SCALE.get(),
                        YPADDING.get() + 9.7*SCALE.get() - V*SCALE.get(),
                        text=f"{name}2", tags="spot")
    elif(color == "#5af542"):
        canvas.create_text(XPADDING.get() + 9.7*SCALE.get() - H*SCALE.get(),
                        YPADDING.get() + 9.7*SCALE.get() - V*SCALE.get(),
                        text=f"{name}1", tags="spot")
    elif(color == "#424bf5"):
        canvas.create_text(XPADDING.get() + 9.7*SCALE.get() - H*SCALE.get(),
                        YPADDING.get() + 9.7*SCALE.get() - V*SCALE.get(),
                        text=f"{name}3", tags="spot")

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