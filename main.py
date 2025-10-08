from tkinter import *



SCALE = 30
XPADDING = SCALE
YPADDING = SCALE



def draw_spot(H, V, color):
    canvas.create_oval(XPADDING + 10*SCALE - H*SCALE - SCALE/5, # Генерация точки по x и y координатам
                        YPADDING + 10*SCALE - V*SCALE - SCALE/5, 
                        XPADDING + 10*SCALE - H*SCALE + SCALE/5,
                        YPADDING + 10*SCALE - V*SCALE + SCALE/5,
                        fill=color)

def take_cords():
    X = float(cords_taker_x.get())
    print(cords_taker_x.get())
    Y = float(cords_taker_y.get())
    print(cords_taker_y.get())
    Z = float(cords_taker_z.get())
    print(cords_taker_z.get())

    print(f"Координаты получены: x = {cords_taker_x.get()}; y = {cords_taker_y.get()}; z = {cords_taker_z.get()};")

    draw_spot(X, Z, "#f54242")
    draw_spot(X, -Y, "#5af542")
    draw_spot(-Y, Z, "#424bf5")

root = Tk() # Корневой объект - окно
root.title("Auto Epur maker") # Заголовок
root.geometry("1400x1200") # размеры окна
# root.attributes("-fullscreen", True) # А при -alpha чёт разницы не видно никакой

icon = PhotoImage(file = "2914917.png")
root.iconphoto(False, icon) # А так получилось
# root.iconbitmap(default="favicon.ico") # иконка программы (пока не получается сделать)

btn = Button(text="Enter", command=take_cords)
btn.pack(anchor=SE, side="bottom", padx=XPADDING, pady=YPADDING/5) # Полёження

cords_taker_z = Entry()
cords_taker_z.pack(anchor=SE, side="bottom", padx=XPADDING, pady=YPADDING/5)
cords_taker_y = Entry()
cords_taker_y.pack(anchor=SE, side="bottom", padx=XPADDING, pady=YPADDING/5)
cords_taker_x = Entry()
cords_taker_x.pack(anchor=SE, side="bottom", padx=XPADDING, pady=YPADDING/5)



canvas = Canvas(bg="white", width=22*SCALE, height=22*SCALE) # Канвас...
canvas.pack(anchor="c", pady=5*SCALE, padx=5*SCALE)

canvas.create_line(XPADDING+10*SCALE, YPADDING, XPADDING+10*SCALE, YPADDING+20*SCALE, width=3.5) # Основные линии координат
canvas.create_line(XPADDING, YPADDING+10*SCALE, XPADDING+20*SCALE, YPADDING+10*SCALE, width=3.5)
canvas.create_line(XPADDING, YPADDING, XPADDING+20*SCALE, YPADDING+20*SCALE) # Диагональ

for c in range (22): # сетка 
    canvas.create_line(c*SCALE, YPADDING, c*SCALE, 21*SCALE)
for r in range (22):
    canvas.create_line(XPADDING, r*SCALE, 21*SCALE, r*SCALE)


root.mainloop() # чтобы не закрывалось сразу