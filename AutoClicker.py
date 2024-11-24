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
from tkinter import BooleanVar
from pynput import keyboard
from winsound import Beep
from pynput import mouse
from time import sleep
from tkinter import Tk
from os import remove

set_appearance_mode('Dark')
set_default_color_theme('blue')

ZSX = GetSystemMetrics(SM_CXSCREEN) / 2560.0
ZSY = GetSystemMetrics(SM_CYSCREEN) / 1600.0
H_yaw = GetSystemMetrics(SM_CYSCREEN)


def IsPressed(keys):
    return bool(WinDLL.user32.GetAsyncKeyState(keys) & 0x8000)


def NWS(a, type_='x'):
    return int(a * ZSX) if type_ == 'x' else int(a * ZSY)


ThemeName: str = 'flatly'
LeftClickModeList = ['Standard', 'Liquid', 'Stable', 'VulcanBoost', 'NoDelay', 'FDPLegacy', 'Extra1', 'Extra2', 'Disabled']
RightClickModeList = ['Standard', 'Liquid', 'NCP', 'NoDelay', 'DropNoSlow', 'Extra1', 'Extra2', 'Disabled']
VK = {
    "LMouseBtn": 0x01, "RMouseBtn": 0x02, "Backspace": 0x08, "Tab": 0x09, "Enter": 0x0D, "Shift": 0x10, "Control": 0x11,
    "Alt": 0x12, "Space": 0x20, "Insert": 0x2D, "Delete": 0x2E, "0": 0x30, "1": 0x31,
    "2": 0x32, "3": 0x33, "4": 0x34, "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39, "A": 0x41, "B": 0x42,
    "C": 0x43, "D": 0x44, "E": 0x45, "F": 0x46, "G": 0x47, "H": 0x48, "I": 0x49, "J": 0x4A, "K": 0x4B, "L": 0x4C,
    "M": 0x4D, "N": 0x4E, "O": 0x4F, "P": 0x50, "Q": 0x51, "R": 0x52, "S": 0x53, "T": 0x54, "U": 0x55, "V": 0x56,
    "W": 0x57, "X": 0x58, "Y": 0x59, "Z": 0x5A, "Left Windows": 0x5B, "Right Windows": 0x5C, "F1": 0x70, "F2": 0x71,
    "F3": 0x72, "F4": 0x73, "F5": 0x74, "F6": 0x75, "F7": 0x76, "F8": 0x77, "F9": 0x78, "F10": 0x79, "F11": 0x7A,
    "F12": 0x7B
}

Name = [
    "LMouseBtn", "RMouseBtn", "Backspace", "Tab", "Enter", "Shift", "Control", "Alt", "Space", "Insert", "Delete",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Left Windows", "Right Windows", "F1", "F2", "F3",
    "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"
]


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
            self.Window.geometry(f'{NWS(500, "x")}x{NWS(600, "y")}')
            self.Window.resizable(False, False)
            apply_style(self.Window, 'acrylic')
            self.LeftKeepClick = BooleanVar()
            self.RightKeepClick = BooleanVar()
            try:
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
                                    command=lambda event: self.UpdateWindow(), width=NWS(120, 'x'))
            self.LeftMaxCPS.place(x=NWS(200, 'x'), y=NWS(45, 'y'))
            self.LeftMaxCPS2 = Label(self.Window, text='1337', font=('Arial', 17))
            self.LeftMaxCPS2.place(x=NWS(320, 'x'), y=NWS(40, 'y'))

            self.LeftMinCPS1 = Label(self.Window, text='Left MinCPS', font=('Arial', 17))
            self.LeftMinCPS1.place(x=NWS(10, 'x'), y=NWS(80))
            self.LeftMinCPS = Scale(self.Window, from_=1, to=20,
                                    command=lambda event: self.UpdateWindow(), width=NWS(120, 'x'))
            self.LeftMinCPS.place(x=NWS(200, 'x'), y=NWS(85, 'y'))
            self.LeftMinCPS2 = Label(self.Window, text='1337', font=('Arial', 17))
            self.LeftMinCPS2.place(x=NWS(320, 'x'), y=NWS(80, 'y'))

            self.RightMaxCPS1 = Label(self.Window, text='RightMaxCPS', font=('Arial', 17))
            self.RightMaxCPS1.place(x=NWS(10, 'x'), y=NWS(120))
            self.RightMaxCPS = Scale(self.Window, from_=1, to=20,
                                     command=lambda event: self.UpdateWindow(), width=NWS(120, 'x'))
            self.RightMaxCPS.place(x=NWS(200, 'x'), y=NWS(125, 'y'))
            self.RightMaxCPS2 = Label(self.Window, text='1337', font=('Arial', 17))
            self.RightMaxCPS2.place(x=NWS(320, 'x'), y=NWS(120, 'y'))

            self.RightMinCPS1 = Label(self.Window, text='RightMinCPS', font=('Arial', 17))
            self.RightMinCPS1.place(x=NWS(10, 'x'), y=NWS(160, 'y'))
            self.RightMinCPS = Scale(self.Window, from_=1, to=20,
                                     command=lambda event: self.UpdateWindow(), width=NWS(120, 'x'))
            self.RightMinCPS.place(x=NWS(200, 'x'), y=NWS(165, 'y'))
            self.RightMinCPS2 = Label(self.Window, text='1337', font=('Arial', 17))
            self.RightMinCPS2.place(x=NWS(320, 'x'), y=NWS(160, 'y'))

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
                                              variable=self.LeftKeepClick)
            self.LeftKeepClick1.place(x=NWS(10, 'x'), y=NWS(465, 'y'))
            self.RightKeepClick1 = Checkbutton(self.Window, text='RightKeepClick',
                                               variable=self.RightKeepClick)
            self.RightKeepClick1.place(x=NWS(10, 'x'), y=NWS(505, 'y'))

            self.AutoRod = BooleanVar()
            self.AutoRod1 = Checkbutton(self.Window, text='AutoRod', variable=self.AutoRod)
            self.AutoRod1.place(x=NWS(250, 'x'), y=NWS(540, 'y'))

            self.AutoWTAP = BooleanVar()
            self.AutoWTAP1 = Checkbutton(self.Window, text='AutoWTAP', variable=self.AutoWTAP)
            self.AutoWTAP1.place(x=NWS(250, 'x'), y=NWS(500, 'y'))

            self.Topmost = BooleanVar()
            self.Topmost1 = Checkbutton(self.Window, text='WindowTopmost', variable=self.Topmost,
                                        command=lambda: self.UpdateWindow())
            self.Topmost1.place(x=NWS(10, 'x'), y=NWS(545, 'y'))

            self.ShiftDisable1 = Label(self.Window, text='ShiftDisable', font=('Arial', 17))
            self.ShiftDisable1.place(x=NWS(10, 'x'), y=NWS(405, 'y'))
            self.ShiftDisable = Combobox(self.Window, state='readonly', values=['Left', 'Right', 'Both', 'Reverse-Right', 'None'],
                                         width=140, height=24,
                                         font=('Arial', 14), dropdown_font=('Arial', 14))
            self.ShiftDisable.place(x=NWS(200, 'x'), y=NWS(409, 'y'))

            self.ExtraCPS1 = Label(self.Window, text='ExtraCPS', font=('Arial', 17))
            self.ExtraCPS1.place(x=NWS(10, 'x'), y=NWS(200, 'y'))
            self.ExtraCPS = Scale(self.Window, from_=2, to=520,
                                    command=lambda event: self.UpdateWindow(), width=NWS(120, 'x'))
            self.ExtraCPS.place(x=NWS(200, 'x'), y=NWS(200, 'y'))
            self.ExtraCPS2 = Label(self.Window, text='1337', font=('Arial', 17), height=1)
            self.ExtraCPS2.place(x=NWS(323, 'x'), y=NWS(200, 'y'))

            self.ExtraCPS.set(16)
            self.ShiftDisable.set('None')
            self.LeftKey.set('R')
            self.RightKey.set('G')
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
            if IsPressed(0x78):
                if self.EnableClick:
                    self.EnableClick = False
                    Beep(500, 150)
                else:
                    self.EnableClick = True
                    Beep(1000, 150)
            if self.EnableClick:
                if (LeftMode != 'Disabled' and IsPressed(VK[self.LeftKey.get()])) and (1 if self.ShiftDisable.get() in ['Right', 'None'] else not IsPressed(VK['Shift'])):
                    OnStop = 0
                    if self.AutoWTAP.get() and IsPressed(VK['W']):
                        self.KeyboardController.release('w')
                        OnStop = 1
                        sleep(0.024)
                    self.AutoRodCount += 1
                    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    if LeftMode not in ['Extra1', 'Extra2']:
                        sleep(0.017)
                    if not self.LeftKeepClick.get():
                        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    self.VulcanClickCount += 1
                    if LeftMode == 'Standard':
                        sleep((Randint(65, 135) / 100) * ((Randint(5, 64) / 100) / Randint(int(self.LeftMinCPS.get()),
                                                                                           int(self.LeftMaxCPS.get()))))
                    elif LeftMode == 'VulcanBoost':
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
                        if self.LeftMaxCPS.get() > 1:
                            for _ in range(int(self.LeftMaxCPS.get()) - 1):
                                mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                                if not self.LeftKeepClick.get():
                                    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                        sleep(0.97)
                    elif LeftMode == 'Liquid':
                        sleep(((Randint(1000, 9999) / 10000) * (
                                1000 / self.LeftMinCPS.get() - 1000 / self.LeftMaxCPS.get() + 1) + 1000 / self.LeftMaxCPS.get()) / 1000)
                    elif LeftMode == 'FDPLegacy':
                        sleep((Randint(50, 74) if Randint(1, 7) == 1 else (
                            87 if Randint(1, 7) <= 2 else Randint(84, 89))) / 1000)
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
                    if self.AutoWTAP.get() and OnStop:
                        sleep(0.04)
                        self.KeyboardController.press('w')

                elif (RightMode != 'Disabled' and IsPressed(VK[self.RightKey.get()])) and ((1 if self.ShiftDisable.get() in ['Left', 'None'] else not IsPressed(VK['Shift'])) if self.ShiftDisable.get() != 'Reverse-Right' else IsPressed(VK['Shift'])):
                    mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                    if RightMode not in ['Extra1', 'Extra2']:
                        sleep(0.017)
                    if not self.RightKeepClick.get():
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                    if RightMode == 'Standard':
                        sleep(0.55 / Randint(int(self.RightMinCPS.get()), int(self.RightMaxCPS.get())))
                    elif RightMode == 'NCP':
                        sleep(0.000001)
                    elif RightMode == 'Liquid':
                        sleep((Randint(1000, 9999) / 10000) * (
                                1000 / self.RightMinCPS.get() - 1000 / self.RightMaxCPS.get() + 1) + 1000 / self.RightMaxCPS.get() / 1000)
                    elif RightMode == 'DropNoSlow':
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                        self.KeyboardController.press('q')
                        sleep(0.17)
                        self.KeyboardController.release('q')
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                        sleep(1.73)
                    elif 'Extra' in RightMode:
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                        for _ in range(int(self.ExtraCPS.get() - 1)):
                            mouse_event(MOUSEEVENTF_RIGHTUP | MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                        if '1' in RightMode:
                            sleep(0.6 / Randint(int(self.LeftMinCPS.get()), int(self.LeftMaxCPS.get())))
            self.Window.after(3, lambda: self.Main())

        def UpdateWindow(self):
            self.VulcanClickCount = 0
            self.Window.attributes('-topmost', self.Topmost.get())
            if self.LeftMaxCPS.get() < self.LeftMinCPS.get():
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
