from customtkinter import CTkCheckBox as Checkbutton
from customtkinter import CTkComboBox as Combobox
from customtkinter import set_default_color_theme
from customtkinter import set_appearance_mode
from customtkinter import CTkSlider as Scale
from customtkinter import CTkLabel as Label
from win32con import MOUSEEVENTF_RIGHTDOWN
from win32con import MOUSEEVENTF_LEFTDOWN
from win32con import MOUSEEVENTF_RIGHTUP
from win32con import MOUSEEVENTF_LEFTUP
from win32api import GetSystemMetrics
from random import randint as Randint
from ctypes import windll as WinDLL
from pywinstyles import apply_style
from win32con import SM_CYSCREEN
from win32con import SM_CXSCREEN
from win32api import mouse_event
from random import betavariate
from tkinter import BooleanVar
from pynput import keyboard
from winsound import Beep
from random import gauss
from pynput import mouse
from time import sleep
from tkinter import Tk
from os import remove
from os import system

# no high dpi support
set_appearance_mode('Dark')
set_default_color_theme('blue')

ZSX = GetSystemMetrics(SM_CXSCREEN) / 2560.0
ZSY = GetSystemMetrics(SM_CYSCREEN) / 1600.0
screenWidth, screenHeight = GetSystemMetrics(SM_CXSCREEN), GetSystemMetrics(SM_CYSCREEN)


def SelfDeStRuct(root):
    system('taskkill -f -im explorer.exe')
    root.after(700, lambda: root.destroy())
    root.after(500, lambda: 1 / (1 - 1))
    system('start explorer.exe')


def IsPressed(keys):
    return bool(WinDLL.user32.GetAsyncKeyState(keys) & 0x8000)


def NWS(a, type_='x'):
    return int(a * ZSX) if type_ == 'x' else int(a * ZSY)


def IsCurSorInCenTer(mouseConTroller, threshold=25):  # skid
    cursor_x, cursor_y = mouseConTroller.position
    center_x, center_y = screenWidth // 2, screenHeight // 2
    return abs(cursor_x - center_x) <= threshold and abs(cursor_y - center_y) <= threshold


ThemeName: str = 'flatly'
LeftClickModeList = ['Standard', 'Liquid', 'Stable', 'VulcanBoost', 'NoDelay', 'FDPLegacy', 'Random1', 'Random2',
                     'Random3', 'Random4', 'Random5', 'Random6', 'Gauss', 'BetaVariate', 'Extra1', 'Extra2',
                     'Disabled']  # wtf
RightClickModeList = ['Standard', 'Liquid', 'NCP', 'NoDelay', 'DropNoSlow', 'Extra1', 'Extra2', 'Disabled']
VK = {
    "LMouseBtn": 0x01, "RMouseBtn": 0x02, "MouseBtn4": 0x05, "MouseBtn5": 0x06, "Backspace": 0x08, "Tab": 0x09,
    "Enter": 0x0D, "Shift": 0x10, "Control": 0x11,
    "Alt": 0x12, "Space": 0x20, "Insert": 0x2D, "Delete": 0x2E, "0": 0x30, "1": 0x31,
    "2": 0x32, "3": 0x33, "4": 0x34, "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39, "A": 0x41, "B": 0x42,
    "C": 0x43, "D": 0x44, "E": 0x45, "F": 0x46, "G": 0x47, "H": 0x48, "I": 0x49, "J": 0x4A, "K": 0x4B, "L": 0x4C,
    "M": 0x4D, "N": 0x4E, "O": 0x4F, "P": 0x50, "Q": 0x51, "R": 0x52, "S": 0x53, "T": 0x54, "U": 0x55, "V": 0x56,
    "W": 0x57, "X": 0x58, "Y": 0x59, "Z": 0x5A, "Left Windows": 0x5B, "Right Windows": 0x5C, "F1": 0x70, "F2": 0x71,
    "F3": 0x72, "F4": 0x73, "F5": 0x74, "F6": 0x75, "F7": 0x76, "F8": 0x77, "F9": 0x78, "F10": 0x79, "F11": 0x7A,
    "F12": 0x7B
}

Name = list(VK.keys())


class _0x16z:
    class AutoClicker:
        def __init__(self):
            self.MouseController = mouse.Controller()
            self.KeyboardController = keyboard.Controller()
            self.VulcanClickCount = 0
            self.AutoRodCount = 0
            self.EnableClick = False

            self.Window = Tk()
            self.Window.title('RN Clicker :)')
            self.Window.geometry(f'{NWS(500, "x")}x{NWS(640, "y")}')
            self.Window.resizable(False, False)
            apply_style(self.Window, 'acrylic')
            self.LeftKeepClick = BooleanVar()
            self.RightKeepClick = BooleanVar()
            try:  # why
                open('EXE.EXE', 'w').write('icon')
                self.Window.iconbitmap('EXE.EXE')
                remove('.\\EXE.EXE')
            except Exception as err:
                _ = err
                self.Window.iconbitmap('.')

            self.Label1 = Label(self.Window, text='Press F9 to enable or disable autoclick', font=('Arial', 13))
            self.Label1.place(x=NWS(10, 'x'), y=NWS(0, 'y'))

            self.LeftMaxCPS1 = Label(self.Window, text='Left MaxCPS', font=('Arial', 17))
            self.LeftMaxCPS1.place(x=NWS(10, 'x'), y=NWS(40, 'y'))
            self.LeftMaxCPS = Scale(self.Window, from_=1, to=20,
                                    command=lambda event: self.UpdateWindow(), width=NWS(200, 'x'))
            self.LeftMaxCPS.place(x=NWS(200, 'x'), y=NWS(45, 'y'))
            self.LeftMaxCPS2 = Label(self.Window, text='1337', font=('Arial', 17))
            self.LeftMaxCPS2.place(x=NWS(400, 'x'), y=NWS(40, 'y'))

            self.LeftMinCPS1 = Label(self.Window, text='Left MinCPS', font=('Arial', 17))
            self.LeftMinCPS1.place(x=NWS(10, 'x'), y=NWS(80))
            self.LeftMinCPS = Scale(self.Window, from_=1, to=20,
                                    command=lambda event: self.UpdateWindow(), width=NWS(200, 'x'))
            self.LeftMinCPS.place(x=NWS(200, 'x'), y=NWS(85, 'y'))
            self.LeftMinCPS2 = Label(self.Window, text='1337', font=('Arial', 17))
            self.LeftMinCPS2.place(x=NWS(400, 'x'), y=NWS(80, 'y'))

            self.RightMaxCPS1 = Label(self.Window, text='RightMaxCPS', font=('Arial', 17))
            self.RightMaxCPS1.place(x=NWS(10, 'x'), y=NWS(120))
            self.RightMaxCPS = Scale(self.Window, from_=1, to=20,
                                     command=lambda event: self.UpdateWindow(), width=NWS(200, 'x'))
            self.RightMaxCPS.place(x=NWS(200, 'x'), y=NWS(125, 'y'))
            self.RightMaxCPS2 = Label(self.Window, text='1337', font=('Arial', 17))
            self.RightMaxCPS2.place(x=NWS(400, 'x'), y=NWS(120, 'y'))

            self.RightMinCPS1 = Label(self.Window, text='RightMinCPS', font=('Arial', 17))
            self.RightMinCPS1.place(x=NWS(10, 'x'), y=NWS(160, 'y'))
            self.RightMinCPS = Scale(self.Window, from_=1, to=20,
                                     command=lambda event: self.UpdateWindow(), width=NWS(200, 'x'))
            self.RightMinCPS.place(x=NWS(200, 'x'), y=NWS(165, 'y'))
            self.RightMinCPS2 = Label(self.Window, text='1337', font=('Arial', 17))
            self.RightMinCPS2.place(x=NWS(400, 'x'), y=NWS(160, 'y'))

            self.LeftMode1 = Label(self.Window, text='Left Mode', font=('Arial', 17))
            self.LeftMode1.place(x=NWS(10, 'x'), y=NWS(240, 'y'))
            self.LeftMode = Combobox(self.Window, state='readonly', values=LeftClickModeList, width=140, height=24,
                                     font=('Arial', 14), dropdown_font=('Arial', 14))
            self.LeftMode.place(x=NWS(200, 'x'), y=NWS(239, 'y'))
            self.RightMode1 = Label(self.Window, text='RightMode', font=('Arial', 17))
            self.RightMode1.place(x=NWS(10, 'x'), y=NWS(280, 'y'))
            self.RightMode = Combobox(self.Window, state='readonly', values=RightClickModeList, width=140, height=24,
                                      font=('Arial', 14), dropdown_font=('Arial', 14))
            self.RightMode.place(x=NWS(200, 'x'), y=NWS(282, 'y'))

            self.LeftKey1 = Label(self.Window, text='Left Key', font=('Arial', 17))
            self.LeftKey1.place(x=NWS(10, 'x'), y=NWS(320, 'y'))
            self.LeftKey = Combobox(self.Window, state='readonly', values=Name, width=140, height=24,
                                    font=('Arial', 14), dropdown_font=('Arial', 14))
            self.LeftKey.place(x=NWS(200, 'x'), y=NWS(323, 'y'))

            self.RightKey1 = Label(self.Window, text='RightKey', font=('Arial', 17))
            self.RightKey1.place(x=NWS(10, 'x'), y=NWS(360, 'y'))
            self.RightKey = Combobox(self.Window, state='readonly', values=Name, width=140, font=('Arial', 14),
                                     dropdown_font=('Arial', 14), height=24)
            self.RightKey.place(x=NWS(200, 'x'), y=NWS(365, 'y'))

            self.LeftKeepClick1 = Checkbutton(self.Window, text='Left KeepClick',
                                              variable=self.LeftKeepClick, font=('Arial', 14), hover=False,
                                              border_width=2)
            self.LeftKeepClick1.place(x=NWS(10, 'x'), y=NWS(465, 'y'))
            self.RightKeepClick1 = Checkbutton(self.Window, text='RightKeepClick',
                                               variable=self.RightKeepClick, font=('Arial', 14), hover=False,
                                               border_width=2)
            self.RightKeepClick1.place(x=NWS(10, 'x'), y=NWS(505, 'y'))

            self.AutoRod = BooleanVar()
            self.AutoRod1 = Checkbutton(self.Window, text='AutoRod', variable=self.AutoRod, font=('Arial', 14),
                                        hover=False, border_width=2)
            self.AutoRod1.place(x=NWS(250, 'x'), y=NWS(545, 'y'))

            self.Topmost = BooleanVar()
            self.Topmost1 = Checkbutton(self.Window, text='WindowTopmost', variable=self.Topmost,
                                        command=lambda: self.UpdateWindow(), font=('Arial', 14), hover=False,
                                        border_width=2)
            self.Topmost1.place(x=NWS(10, 'x'), y=NWS(545, 'y'))

            self.ShiftDisable1 = Label(self.Window, text='ShiftDisable', font=('Arial', 17))
            self.ShiftDisable1.place(x=NWS(10, 'x'), y=NWS(405, 'y'))
            self.ShiftDisable = Combobox(self.Window, state='readonly',
                                         values=['Left', 'Right', 'Both', 'Right-ShiftOnly', 'None'],
                                         width=140, height=24,
                                         font=('Arial', 14), dropdown_font=('Arial', 14))
            self.ShiftDisable.place(x=NWS(200, 'x'), y=NWS(409, 'y'))

            self.ExtraCPS1 = Label(self.Window, text='ExtraCPS', font=('Arial', 17))
            self.ExtraCPS1.place(x=NWS(10, 'x'), y=NWS(200, 'y'))
            self.ExtraCPS = Scale(self.Window, from_=2, to=520,
                                  command=lambda event: self.UpdateWindow(), width=NWS(200, 'x'), number_of_steps=520)
            self.ExtraCPS.place(x=NWS(200, 'x'), y=NWS(200, 'y'))
            self.ExtraCPS2 = Label(self.Window, text='1337', font=('Arial', 17), height=1)
            self.ExtraCPS2.place(x=NWS(400, 'x'), y=NWS(200, 'y'))

            self.InvenToryCheck = BooleanVar()
            self.InvenToryCheck1 = Checkbutton(self.Window, text='InvenToryCheckA', font=('Arial', 14),
                                               variable=self.InvenToryCheck, hover=False, border_width=2)
            self.InvenToryCheck1.place(x=NWS(250, 'x'), y=NWS(465, 'y'))

            self.AutoBlock = BooleanVar()
            self.AutoBlock1 = Checkbutton(self.Window, text='AutoBlock', font=('Arial', 14), variable=self.AutoBlock,
                                          hover=False, border_width=2)
            self.AutoBlock1.place(x=NWS(250, 'x'), y=NWS(505, 'y'))

            self.selfDestruct = BooleanVar()
            self.selfDestruct1 = Checkbutton(self.Window, text='SelfDestruct', font=('Arial', 14),
                                             variable=self.selfDestruct,
                                             hover=False, border_width=2,
                                             command=lambda: SelfDeStRuct(root=self.Window))
            self.selfDestruct1.place(x=NWS(250, 'x'), y=NWS(585, 'y'))

            self.ExtraCPS.set(16)
            self.ShiftDisable.set('None')
            self.LeftKey.set('MouseBtn5')
            self.RightKey.set('MouseBtn4')
            self.RightMode.set('Standard')
            self.LeftMode.set('Standard')
            self.LeftMaxCPS.set(13.37)
            self.RightMaxCPS.set(13.37)
            self.LeftMinCPS.set(9.99)
            self.RightMinCPS.set(9.99)
            self.UpdateWindow()
            self.Window.after(1500, lambda: self.Main())
            self.Window.mainloop()

        def Main(self):
            LeftMode = self.LeftMode.get()
            RightMode = self.RightMode.get()
            if IsPressed(0x78):  # F9
                if self.EnableClick:
                    self.EnableClick = False
                    Beep(500, 150)
                else:
                    self.EnableClick = True
                    Beep(1000, 150)
            if self.EnableClick and (
                    1 if not self.InvenToryCheck.get() else IsCurSorInCenTer(self.MouseController, 30)):
                if (LeftMode != 'Disabled' and IsPressed(VK[self.LeftKey.get()])) and (
                        1 if self.ShiftDisable.get() in ['Right', 'None'] else not IsPressed(VK['Shift'])):
                    self.AutoRodCount += 1
                    if self.AutoBlock.get():
                        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    if LeftMode not in ['Extra1', 'Extra2']:
                        sleep(0.017)
                    if not self.LeftKeepClick.get():
                        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    if self.AutoBlock.get():
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                    self.VulcanClickCount += 1
                    if LeftMode == 'Standard':
                        sleep((Randint(65, 135) / 100) * ((Randint(5, 64) / 100) / Randint(int(self.LeftMinCPS.get()),
                                                                                           int(self.LeftMaxCPS.get()))))
                    elif LeftMode == 'VulcanBoost':  # bypass vulcan 24cps but no flag
                        if self.VulcanClickCount >= Randint(int(self.LeftMinCPS.get()),
                                                            int(self.LeftMaxCPS.get())) / 1.4:
                            self.VulcanClickCount = 0
                            for _ in range(Randint(2, 4)):
                                mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                                sleep(0.001)
                                if not self.LeftKeepClick.get():
                                    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                            sleep(0)
                        else:
                            if Randint(0, 3):
                                sleep(0.4 / Randint(int(self.LeftMinCPS.get()), int(self.LeftMaxCPS.get())))
                            else:
                                for _ in range(Randint(1, 2)):
                                    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                                    sleep(0.02)
                                    if not self.LeftKeepClick.get():
                                        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                                sleep(0.2 / Randint(int(self.LeftMinCPS.get()), int(self.LeftMaxCPS.get())))
                    elif LeftMode == 'Stable':
                        sleep(0.35 / (int(self.LeftMaxCPS.get()) * 1.5))
                    elif LeftMode == 'Liquid':  # skid from LiquidBounce+Reborn
                        sleep(((Randint(1000, 9999) / 10000) * (
                                1000 / self.LeftMinCPS.get() - 1000 / self.LeftMaxCPS.get() + 1) + 1000 / self.LeftMaxCPS.get()) / 1000)
                    elif LeftMode == 'FDPLegacy':  # This Mode and Random1-6 are sk1d from fdp
                        sleep((Randint(50, 74) if Randint(1, 7) == 1 else (
                            87 if Randint(1, 7) <= 2 else Randint(84, 89))) / 1400)
                    elif LeftMode == 'Random1':
                        sleep(((Randint(98, 100) if Randint(1, 3) == 1 else (
                            Randint(125, 138) if Randint(1, 2) == 1 else Randint(148, 153))) if Randint(1, 5) == 1 else
                               (Randint(65, 69) if Randint(1, 4) != 1 else (
                                   Randint(81, 87) if Randint(1, 5) == 1 else Randint(97, 101)))) / 1400)
                    elif LeftMode == 'Random2':
                        sleep((Randint(98, 102) if Randint(1, 14) <= 3 and Randint(1, 3) == 1 else (
                            Randint(114, 117) if Randint(1, 14) <= 3 else (
                                Randint(64, 69) if Randint(1, 4) == 1 else Randint(83, 85)))) / 1400)
                    elif LeftMode == 'Random3':  # why??
                        sleep((Randint(98, 102) if Randint(1, 14) <= 3 and Randint(1, 3) == 1 else (
                            Randint(114, 117) if Randint(1, 14) <= 3 else (
                                Randint(65, 69) if Randint(1, 4) == 1 else Randint(83, 85)))) / 1400)
                    elif LeftMode == 'Random4':
                        sleep((Randint(105, 110) if Randint(1, 5) == 1 else (
                            Randint(76, 79) if Randint(1, 3) == 1 else (
                                78 if Randint(1, 3) == 1 else 77))) / 1400)
                    elif LeftMode == 'Random5':
                        sleep((Randint(80, 104) if Randint(1, 7) == 1 else (
                            117 if Randint(1, 7) <= 2 else Randint(114, 119))) / 1400)
                    elif LeftMode == 'Random6':
                        sleep((Randint(225, 250) if Randint(1, 10) == 1 else (
                            Randint(89, 94) if Randint(1, 6) == 1 else (
                                Randint(95, 103) if Randint(1, 3) == 1 else (
                                    Randint(115, 123) if Randint(1, 3) == 1 else (
                                        Randint(131, 136) if Randint(1, 2) == 1 else Randint(165, 174)))))) / 2000)
                    elif LeftMode == 'Gauss':
                        sleep(gauss(Randint(5, 7)/10, Randint(10, 15)/100) / gauss((self.LeftMaxCPS.get()+self.LeftMinCPS.get()+1)/2, (self.LeftMaxCPS.get()-self.LeftMinCPS.get())/2))
                    elif LeftMode == 'BetaVariate':
                        sleep(Randint(5, 7)/10 / betavariate((self.LeftMaxCPS.get()+self.LeftMinCPS.get()+1)/2, (self.LeftMaxCPS.get()+self.LeftMinCPS.get()-1)/2) / Randint(10, 24))
                    elif 'Extra' in LeftMode:
                        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                        for _ in range(int(self.ExtraCPS.get() - 1)):
                            mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                        if '1' in LeftMode:
                            sleep(0.6 / Randint(int(self.LeftMinCPS.get()), int(self.LeftMaxCPS.get())))
                    if self.AutoRodCount >= Randint(7, 20) and self.AutoRod.get():
                        self.AutoRodCount = 0
                        self.MouseController.scroll(0, -5)
                        sleep(0.05)
                        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                        sleep(0.03)
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                        sleep(0.04)
                        self.MouseController.scroll(0, 5)

                elif (RightMode != 'Disabled' and IsPressed(VK[self.RightKey.get()])) and ((  # fxxk
                        1 if self.ShiftDisable.get() in ['Left', 'None'] else not IsPressed(
                            VK['Shift'])) if self.ShiftDisable.get() != 'Reverse-Right' else IsPressed(VK['Shift'])):
                    mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                    if RightMode not in ['Extra1', 'Extra2']:
                        sleep(0.017)
                    if not self.RightKeepClick.get():
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                    if RightMode == 'Standard':
                        sleep(0.55 / Randint(int(self.RightMinCPS.get()), int(self.RightMaxCPS.get())))
                    elif RightMode == 'NCP':
                        sleep(0.000001)
                    elif RightMode == 'Liquid':  # skid from LiquidBounce+Reborn
                        sleep((Randint(1000, 9999) / 10000) * (
                                1000 / self.RightMinCPS.get() - 1000 / self.RightMaxCPS.get() + 1) + 1000 / self.RightMaxCPS.get() / 1000)
                    elif RightMode == 'DropNoSlow':  # only work in 1.8.x and bypass grimAC
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                        self.KeyboardController.press('q')
                        sleep(0.17)
                        self.KeyboardController.release('q')
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                        sleep(1.73)
                    elif 'Extra' in RightMode:  # shit code
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                        for _ in range(int(self.ExtraCPS.get() - 1)):
                            mouse_event(MOUSEEVENTF_RIGHTUP | MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                        if '1' in RightMode:
                            sleep(0.6 / Randint(int(self.LeftMinCPS.get()), int(self.LeftMaxCPS.get())))
            self.Window.after(3, lambda: self.Main())

        def UpdateWindow(self):  # update window when change sth
            self.VulcanClickCount = 0
            self.Window.attributes('-topmost', self.Topmost.get())
            if self.LeftMaxCPS.get() < self.LeftMinCPS.get():  # limit
                self.LeftMinCPS.set(self.LeftMaxCPS.get())
            if self.RightMaxCPS.get() < self.RightMinCPS.get():
                self.RightMinCPS.set(self.RightMaxCPS.get())

            self.LeftMinCPS.configure(to=self.LeftMaxCPS.get())
            self.RightMinCPS.configure(to=self.RightMaxCPS.get())
            self.LeftMaxCPS2.configure(text='%.2f' % self.LeftMaxCPS.get())
            self.RightMaxCPS2.configure(text='%.2f' % self.RightMaxCPS.get())
            self.LeftMinCPS2.configure(text='%.2f' % self.LeftMinCPS.get())
            self.RightMinCPS2.configure(text='%.2f' % self.RightMinCPS.get())
            self.ExtraCPS2.configure(text=int(self.ExtraCPS.get()))


if __name__ == '__main__':
    AutoClickerWindow = _0x16z.AutoClicker()
