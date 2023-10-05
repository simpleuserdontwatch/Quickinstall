from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 250   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
root = Tk()
n = ttk.Style(root)
root.resizable(False,False)
root.iconbitmap('usb.ico')
root.title('Quickinstall')
def apply2():
    a = messagebox.askquestion('Question', 'Are you sure?')
    if a == 'yes':
        apply3()

def apply3():
    a = messagebox.askquestion('Warning', 'Are you actually sure? Data on the drive would be formatted')
    if a == 'yes':
        apply()
def apply():
    install_wim_path = a.get()
    drive = b.get()
    seven_zip_path = c.get()

    # Validate inputs
    if not os.path.isfile(install_wim_path):
        messagebox.showerror("Error", "Not a install.wim file")
        return
    if not os.path.exists(drive):
        messagebox.showerror("Error", "Invalid drive. Have you inserted the drive or specified the drive letter only?")
        return
    if not os.path.isfile(seven_zip_path) and not seven_zip_path.lower() == "7z":
        messagebox.showerror("Error", "Invalid 7z executable path")
        return
    os.system(f'format {drive}:')
    # Apply install.wim using 7-Zip
    command = f'{seven_zip_path} x -o{drive}: {install_wim_path}'
    os.system(command)

    os.system('bcdboot {drive}: /s {drive}: /f ALL')
    messagebox.showinfo('Done!', 'Installion is done\nYou may now inject the flash drive')
def easteregg(e):
    d.config(text='Microsoft QuickInstall')
    root.title('Microsoft QuickInstall')
    root.iconbitmap('MS.ico')
    n.theme_use('classic')
    root.config(bg='#d9d9d9')
d = ttk.Label(text='QuickInstall')
d.grid(column=1,row=1)
CreateToolTip(d, "Create windows partitions without having to boot from CD")
d.bind('<Button-3>', easteregg)
a = ttk.Entry()
b = ttk.Entry()
c = ttk.Entry()
ttk.Label(text='File:').grid(column=1,row=2)
ttk.Label(text='Drive:').grid(column=1,row=3)
ttk.Label(text='7z exceuteable path:').grid(column=1,row=4)
a.grid(column=2,row=2)
b.grid(column=2,row=3)
c.grid(column=2,row=4)
CreateToolTip(a,'Specify install.wim file path from windows\ninstallation CD.\nAlso you could extract install.wim from windows 7+ iso using 7z\nand specify in there')
CreateToolTip(b, 'On what drive would windows be installed? (Letter only)')
CreateToolTip(c, 'The 7z executeable path.\nIf you dont have 7z, then go to 7-zip.org/download.html and download it\nif it was installed, copy the files of 7z program\nthen put it in the path of program\nand specify 7z.exe')
ttk.Label(text='').grid(column=2,row=5)
ttk.Label(text='').grid(column=2,row=6)
ttk.Button(text='Install!', command=apply2).grid(column=2,row=7)

root.mainloop()
