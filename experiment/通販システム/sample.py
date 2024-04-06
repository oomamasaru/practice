import tkinter

class ParentFrame(tkinter.Frame) :
    def __init__(self,root:tkinter.Tk) :
        super().__init__(root,width=500,height=300)
        self.pack()
        self.propagate(0)
        self.root = root
    
    def create_widgets(self) :
        quit_btn = tkinter.Button(self)
        quit_btn["text"] = "終了"
        quit_btn["command"] = self.root.destroy
        quit_btn.pack(side="top")

root = tkinter.Tk()
print(type(root))
root.title("Sample")
root.geometry("1000x600")
parent_Frame = ParentFrame(root)
parent_Frame.mainloop()





