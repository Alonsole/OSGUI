#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import os
import tkinter.font as tkFont
import shutil

def win_show():
    """Окно ввода"""
    global entry_label_action
    global entry_label_go
    window = tk.Toplevel(root)
    window.geometry ('260x130')
    window.title("Input window")
    """С чем работаю файл или папка"""
    if Cbox_file_var.get() == 1:
        window_label_status = tk.Label(window, text="Работаю с файлом")
        file_check = "1"
    else:
        window_label_status = tk.Label(window, text="Работаю с папкой")
        file_check = "0"
    window_label_status.grid(row=0, column=0)

    entry_label_action = tk.Entry(window)
    
    """Какое действие будет выполнено и с чем (файл/папка)"""
    if Cbox_create_var.get() == 1 and Cbox_del_var.get() == 0  and Cbox_move_var.get() == 0 and Cbox_copy_var.get() == 0:
        window_label_action = tk.Label(window, text="Создаю. Укажите имя") 
        if file_check == "1":
            start_button = tk.Button(window, text="Подтверждаю", width = 17, command=create_file)
        else:
            start_button = tk.Button(window, text="Подтверждаю", width = 17, command=create_folder)
    elif Cbox_create_var.get() == 0 and Cbox_del_var.get() == 1  and Cbox_move_var.get() == 0 and Cbox_copy_var.get() == 0:
        window_label_action = tk.Label(window, text="Удаляю. Укажите имя") 
        if file_check == "1":
            start_button = tk.Button(window, text="Подтверждаю", width = 17, command=del_file)
        else:
            start_button = tk.Button(window, text="Подтверждаю", width = 17, command=del_folder)
    elif Cbox_create_var.get() == 0 and Cbox_del_var.get() == 0  and Cbox_move_var.get() == 1 and Cbox_copy_var.get() == 0:
        window_label_action = tk.Label(window, text="Перемещаю. Укажите источник/файл")  
        window_label_to = tk.Label(window, text="Укажите путь назначения") 
        window_label_to.grid(row=3, column=0)
        entry_label_go = tk.Entry(window)
        entry_label_go.grid(row=4, column=0,padx = 5)
        entry_label_go.config(width=40)
        if file_check == "1":
            start_button = tk.Button(window, text="Подтверждаю", width = 17, command=move_file)
        else:
            start_button = tk.Button(window, text="Подтверждаю", width = 17, command=move_folder)
    elif Cbox_create_var.get() == 0 and Cbox_del_var.get() == 0  and Cbox_move_var.get() == 0 and Cbox_copy_var.get() == 1:
        window_label_action = tk.Label(window, text="Копирую. Укажите имя")    
        if file_check == "1":
            start_button = tk.Button(window, text="Подтверждаю", width = 17, command=copy_file)
        else:
            start_button = tk.Button(window, text="Подтверждаю", width = 17, command=copy_folder)
    else:
        pass
    
    
    start_button.grid(row=5, column=0)
    entry_label_action.grid(row=2, column=0,padx = 5)
    entry_label_action.config(width=40)
    window_label_action.grid(row=1, column=0)

def create_file():
    """Создание текстового файла"""
    try:
        with open(entry_label_action.get()+".txt", "w") as file:
            file.write("MY FILE")
        status_work_ok()
    except:
        status_work_not_ok() 
        
def create_folder():
    """Создание папки"""
    try:
        os.mkdir(entry_label_action.get())
        status_work_ok()
    except:
        status_work_not_ok()   

def del_file():
    """Удаление текстового файла"""
    try:
        os.remove(entry_label_action.get()+".txt")
        status_work_ok()
    except:
        status_work_not_ok() 
        
def del_folder():
    """Удаление папки"""
    try:
        os.rmdir(entry_label_action.get())
        status_work_ok()
    except:
        status_work_not_ok() 

def copy_file():
    """Копия текстового файла"""
    try:
        shutil.copy(entry_label_action.get()+".txt", entry_label_action.get()+"copy.txt")
        status_work_ok()
    except:
        status_work_not_ok() 
        
def copy_folder():
    """Копия папки"""
    try:
        shutil.copytree(entry_label_action.get(), "copy"+entry_label_action.get())
        status_work_ok()
    except:
        status_work_not_ok() 
        
def move_file():
    """Перемещение текстового файла"""
    try:
        shutil.move(entry_label_action.get()+".txt", entry_label_go.get()+".txt")
        status_work_ok()
    except:
        status_work_not_ok() 
        
def move_folder():
    """Перемещение папки"""
    try:
        shutil.move(entry_label_action.get(), entry_label_go.get())
        status_work_ok()
    except:
        status_work_not_ok() 
        
def status_work_ok():
    """Успешный статус в окне"""
    status_window_ok = tk.Toplevel(root)
    status_window_ok.geometry ('220x20')
    status_window_ok.title("Status")
    status_window_ok_label = tk.Label(status_window_ok, text="Успешно выполнил задачу")
    status_window_ok_label.grid(row=0, column=0)

def status_work_not_ok():
    """Статус о неудаче в окне"""
    status_window_not_ok = tk.Toplevel(root)
    status_window_not_ok.geometry ('220x20')
    status_window_not_ok.title("Status")
    status_window_not_ok = tk.Label(status_window_not_ok, text="Я не смог выполнить задачу")
    status_window_not_ok.grid(row=0, column=0)
    
def start_work():
    """Контролим параметры и запускаем функции"""
    if Cbox_file_var.get() == 0 and Cbox_folder_var.get() == 0:
        pass
    elif Cbox_file_var.get() == 1 and Cbox_folder_var.get()  == 1:
        pass
    elif Cbox_create_var.get() == 1 and Cbox_del_var.get() == 0  and Cbox_move_var.get() == 0 and Cbox_copy_var.get() == 0:
        if Cbox_folder_var.get() == 1:
            win_show()
        else:
            win_show()

    elif Cbox_create_var.get() == 0 and Cbox_del_var.get() == 1 and Cbox_move_var.get() == 0 and Cbox_copy_var.get() == 0:
        if Cbox_folder_var.get() == 1:
            win_show()
        else:
            win_show()

    elif Cbox_create_var.get() == 0 and Cbox_del_var.get() == 0 and Cbox_move_var.get() == 1 and Cbox_copy_var.get() == 0:
        if Cbox_folder_var.get() == 1:
            win_show()
        else:
            win_show()

    elif Cbox_create_var.get() == 0 and Cbox_del_var.get() == 0 and Cbox_move_var.get() == 0 and Cbox_copy_var.get() == 1:
        if Cbox_folder_var.get() == 1:
            win_show()
        else:
            win_show()
        
class App:
    """Дизайн приложения и элементы управления. Главная. Расположение элементов"""
    def __init__(self, root):
        """Глобальные ЧБоксы для проверки статуса ЧБокса (выбран/не выбран)"""
        global Cbox_create_var
        global Cbox_file_var
        global Cbox_folder_var
        global Cbox_del_var
        global Cbox_move_var
        global Cbox_copy_var
       
        #setting title
        root.title("os")
        #setting window size
        width=180
        height=180
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        """Тест Лейбл"""
        Label_one=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Label_one["font"] = ft
        Label_one["fg"] = "#333333"
        Label_one["justify"] = "center"
        Label_one["text"] = "Выбор действия с:"
        Label_one.place(x=0,y=0,width=137,height=30)
        
        """ЧБокс Создать"""
        Cbox_create_var =tk.IntVar()
        Cbox_create=tk.Checkbutton(root, variable=Cbox_create_var)
        ft = tkFont.Font(family='Times',size=10) 
        Cbox_create["font"] = ft 
        Cbox_create["fg"] = "#333333"
        Cbox_create["justify"] = "center" 
        Cbox_create["text"] = "Создать"
        Cbox_create.place(x=10,y=60,width=70,height=30)
        Cbox_create["offvalue"] = "0"
        Cbox_create["onvalue"] = "1"
        #Cbox_create["command"] = self.Cbox_create_command
        
        """ЧБокс Удалить"""
        Cbox_del_var =tk.IntVar()
        Cbox_del=tk.Checkbutton(root, variable=Cbox_del_var)
        ft = tkFont.Font(family='Times',size=10)
        Cbox_del["font"] = ft
        Cbox_del["fg"] = "#333333"
        Cbox_del["justify"] = "center"
        Cbox_del["text"] = "Удалить"
        Cbox_del.place(x=10,y=80,width=70,height=30)
        Cbox_del["offvalue"] = "0"
        Cbox_del["onvalue"] = "1"
        #Cbox_del["command"] = self.Cbox_del_command
        
        """ЧБокс Переместить"""
        Cbox_move_var =tk.IntVar()
        Cbox_move=tk.Checkbutton(root, variable=Cbox_move_var)
        ft = tkFont.Font(family='Times',size=10)
        Cbox_move["font"] = ft
        Cbox_move["fg"] = "#333333"
        Cbox_move["justify"] = "left"
        Cbox_move["text"] = "Переместить"
        Cbox_move.place(x=81,y=60,width=90,height=30)
        Cbox_move["offvalue"] = "0"
        Cbox_move["onvalue"] = "1"
        #Cbox_move["command"] = self.Cbox_move_command

        """ЧБокс Копировать"""
        Cbox_copy_var =tk.IntVar()
        Cbox_copy=tk.Checkbutton(root, variable=Cbox_copy_var)
        ft = tkFont.Font(family='Times',size=10)
        Cbox_copy["font"] = ft
        Cbox_copy["fg"] = "#333333"
        Cbox_copy["justify"] = "center"
        Cbox_copy["text"] = "Копировать"
        Cbox_copy.place(x=80,y=80,width=90,height=30)
        Cbox_copy["offvalue"] = "0"
        Cbox_copy["onvalue"] = "1"
        #Cbox_copy["command"] = self.Cbox_copy_command

        Label_three=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Label_three["font"] = ft
        Label_three["fg"] = "#333333"
        Label_three["justify"] = "center"
        Label_three["text"] = "Действие:"
        Label_three.place(x=10,y=40,width=70,height=25)

        """ЧБокс Работа с Файлом"""
        Cbox_file_var =tk.IntVar()
        Cbox_file=tk.Checkbutton(root, variable=Cbox_file_var)
        ft = tkFont.Font(family='Times',size=10)
        Cbox_file["font"] = ft
        Cbox_file["fg"] = "#333333"
        Cbox_file["justify"] = "center"
        Cbox_file["text"] = "Файлом"
        Cbox_file.place(x=10,y=22,width=70,height=25)
        Cbox_file["offvalue"] = "0"
        Cbox_file["onvalue"] = "1"
        #Cbox_file["command"] = self.Cbox_file_command

        """ЧБокс Работа с Папкой"""
        Cbox_folder_var =tk.IntVar()
        Cbox_folder=tk.Checkbutton(root, variable=Cbox_folder_var)
        ft = tkFont.Font(family='Times',size=10)
        Cbox_folder["font"] = ft
        Cbox_folder["fg"] = "#333333"
        Cbox_folder["justify"] = "center"
        Cbox_folder["text"] = "Папкой"
        Cbox_folder.place(x=80,y=22,width=70,height=25)
        Cbox_folder["offvalue"] = "0"
        Cbox_folder["onvalue"] = "1"
        #Cbox_folder["command"] = self.Cbox_folder_command

        """Запуск"""
        Button_start=tk.Button(root)
        Button_start["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_start["font"] = ft
        Button_start["fg"] = "#000000"
        Button_start["justify"] = "center"
        Button_start["text"] = "Выполнить"
        Button_start.place(x=60,y=120,width=70,height=25)
        Button_start["command"] = self.Button_start_command

    def Button_start_command(self):
        start_work()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# In[ ]:





# In[ ]:




