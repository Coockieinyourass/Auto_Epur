from tkinter import *



XPADDING = 50
YPADDING = 50



def finish():
    root.destroy() # ручное закрытие окна и всего приложения
    print("Приложение закрыто")

def take_cords():
    # x = cords_taker_x.
    # y = cords_taker_y.get()

    print(cords_taker_x.get())

    print(f"Координаты получены: x = ; y = ;")

root = Tk() # Корневой объект - окно
root.title("Auto Epur maker") # Заголовок
root.protocol("WM_DELETE_WINDOW", finish) # первый аргумент, условие, при котором будет выполняться второй
root.geometry("1400x1200") # размеры окна
# root.attributes("-fullscreen", True) # А при -alpha чёт разницы не видно никакой

icon = PhotoImage(file = "2914917.png")
root.iconphoto(False, icon) # А так получилось
# root.iconbitmap(default="favicon.ico") # иконка программы (пока не получается сделать)



cords_taker_x = Entry().pack(side="right")
cords_taker_y = Entry().pack(side="right")

btn = Button(text="Enter", command=take_cords)
btn.pack(side="right") # Полёження

canvas = Canvas(bg="white", width=1100, height=1100) # Канвас...
canvas.pack(anchor="c")

canvas.create_line(XPADDING+500, YPADDING, XPADDING+500, YPADDING+1000, width=3.5) # Основные линии координат
canvas.create_line(XPADDING, YPADDING+500, XPADDING+1000, YPADDING+500, width=3.5)

for c in range (22): # сетка 
    canvas.create_line(c*50, YPADDING, c*50, 1050)
for r in range (22):
    canvas.create_line(XPADDING, r*50, 1050, r*50)


root.mainloop() # чтобы не закрывалось сразу