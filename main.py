from tkinter import *

def finish():
    root.destroy() # ручное закрытие окна и всего приложения
    print("Приложение закрыто")

def base_btn():
    print("Базовая кнопка была нажата")

root = Tk() # Корневой объект - окно
root.title("Test program") # Заголовок
root.protocol("WM_DELETE_WINDOW", finish) # первый аргумент, условие, при котором будет выполняться второй
root.geometry("1000x700") # размеры окна
# root.attributes("-fullscreen", True) # А при -alpha чёт разницы не видно никакой

icon = PhotoImage(file = "2914917.png")
root.iconphoto(False, icon) # А так получилось
# root.iconbitmap(default="favicon.ico") # иконка программы (пока не получается сделать)

label = Label(text="Hello Tkinter") # текстовая метка
label.pack() # размещение метки

btn = Button(text="Hello!", command=base_btn)
btn.pack()

root.mainloop() # чтобы не закрывалось сразу