from tkinter import ttk
import tkinter as tk
from win32api import GetSystemMetrics
import os

import function.open as open 
global window 
window = tk.Tk()
window.title("Semester 1 2021/2022")

screenWidth = str(GetSystemMetrics(0))#get screen resolution(width) -> into string
screenHeight = str(GetSystemMetrics(1))#get screen resolution(height) -> into string
window.geometry(screenWidth+"x"+screenHeight)#widthxheight format
#window.iconbitmap('./icon.ico')

global tabControl
tabControl = ttk.Notebook(window)

tab0 = ttk.Frame(tabControl)
tabControl.add(tab0, text='Main')
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='BCS2243 WE 1-A')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='BCN2023 DNS 3-A')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='BCS2213 FM 1-B')
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='BUM2413 AS 18-P')
tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='UHL2422 ET 10-P')
tab6 = ttk.Frame(tabControl)
tabControl.add(tab6, text='About')


tabControl.pack(expand=1, fill="both")

#tab0
welcomeDisplay = tk.Label(tab0, text="Welcome User 4301")
welcomeDisplay.grid(row=0, column=0)
meetBtn = tk.Button(tab0, text="Open GMeet",command=lambda:open.openGmeet())
meetBtn.grid(row=0, column=1)
whatBtn = tk.Button(tab0, image = "./img/logo/wa.png",command=lambda:open.openGmeet())
whatBtn.grid(row=0, column=2)

window.mainloop()



