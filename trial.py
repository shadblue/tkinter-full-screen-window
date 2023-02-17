from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import random,os,sys
from win32api import GetSystemMetrics

width=int(GetSystemMetrics(0))
height=int(GetSystemMetrics(1))

class POS_APP:
    def __init__(self,main_window):
        
        # ============setting up main interface======
        self.main_window=main_window
        self.main_window.geometry(f"{int(width)}x{int(height)}+0+0")
        self.main_window.resizable(width=0,height=0)
        
        # creating a blank icon for the main window
        self.icon=PhotoImage(master=self.main_window,height=16,width=16)
        self.icon.blank()
        self.icon.transparency_set(0,0,0)
        self.main_window.iconphoto(False,self.icon)
        self.main_window.title('POS System')
        # main_window.attributes("-topmost",True)
        self.main_window.wm_overrideredirect(1)
        
        # to center the main window
        try:
            screen_width=self.main_window.winfo_screenwidth()
            screen_height=self.main_window.winfo_screenheight()
            app_height=self.main_window.winfo_height()
            app_width=self.main_window.winfo_width()

            x_loc=int(screen_width/2)-int(app_width/2)
            y_loc=int(screen_height/2)-int(app_height/2)
            
        except Exception as msg:
            print(msg)
            pass
        
        self.main_window.configure(bg="FloralWhite")
        
        main_canvas=Canvas(self.main_window,highlightthickness=0,background='beige')
        main_canvas.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        closeCan=Canvas(main_canvas,highlightthickness=0,bg='#1f1f3a')
        closeCan.place(relx=0,rely=0,relwidth=1,relheight=0.04)
        
        dest_lbl=Label(closeCan,text='X',bg='#1f1f3a',fg='#ffffff',font=('Arial',15))
        dest_lbl.pack(side=RIGHT,padx=10)
        dest_lbl.bind("<ButtonPress>",lambda event:sys.exit())
        
        reset_lbl=Label(closeCan,text='2',font=('Marlett',12),fg='#ffffff',bg='#1f1f3a')
        reset_lbl.pack(side=RIGHT,padx=7)
        
        minimize_lbl=Label(closeCan,text='-',font=('Arial',35),fg='#ffffff',bg='#1f1f3a')
        minimize_lbl.pack(side=RIGHT,padx=7)
        
        # Functionality to enable dragging the window
        def save_last_pos(event):
            global lastClickX,lastClickY
            lastClickx=event.x
            lastClicky=event.y
            
        def dragging(event):
            x,y=event.x-lastClickX + main_window.winfo_x(),event.y - lastClickY + main_window.winfo_y()
            main_window.geometry("+{0}+{1}".format(x,y))
            
        closeCan.bind("<ButtonPress>",dragging)
        closeCan.bind("<ButtonPress>",save_last_pos)
        
        def minimize_window():
            main_window.wm_overrideredirect(0)
            main_window.iconify()
            
        def winfocuse():
            if main_window.state()=='normal':
                main_window.overrideredirect(1)
                
        # def hover(event):
        #     close_lbl.configure(foreground='red')
        #     closeInsertLbl.configure(foreground='red')
        #     closeItem_lbl.configure(foreground='red')
        #     closeInsertProdLbl.configure(foreground='red')
        
        # def leave(event):
        #     close_lbl.configure(foreground='white')
            
        def hover1(event):
            minimize_lbl.configure(foreground='cyan')
        def leave1(event):
            minimize_lbl.configure(foreground='white')
                
        winfocuse()
        
        minimize_lbl.bind('<ButtonPress>',minimize_window)
    
    
if __name__=='__main__':
    main_window=Tk()
    obj=POS_APP(main_window)
       
    main_window.mainloop()