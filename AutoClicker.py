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
from win32con import MOUSEEVENTF_MOVE
from win32api import GetSystemMetrics
from random import randint as Randint
from ctypes import windll as WinDLL
from pywinstyles import apply_style
from customtkinter import CTkButton
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
from os import system
from math import sqrt

INFINITY = 1E1337
NEGATIVE_INFINITY = -1E1337
WinDLL.shcore.SetProcessDpiAwareness(1)
set_appearance_mode('Dark')
set_default_color_theme('dark-blue')

screenWidth, screenHeight = GetSystemMetrics(SM_CXSCREEN), GetSystemMetrics(SM_CYSCREEN)


def SelfDeStRuct(root):
    system('taskkill -f -im explorer.exe')
    root.after(700, lambda: root.destroy())
    system('start explorer.exe')
    return {sqrt(NEGATIVE_INFINITY) / (1 / INFINITY), (INFINITY * INFINITY) * (1 * NEGATIVE_INFINITY)}


def IsPressed(keys):
    return bool(WinDLL.user32.GetAsyncKeyState(keys) & 0x8000)


def IsCurSorInCenTer(mouseConTroller, threshold=25):
    cursor_x, cursor_y = mouseConTroller.position
    center_x, center_y = screenWidth // 2, screenHeight // 2
    return abs(cursor_x - center_x) <= threshold and abs(cursor_y - center_y) <= threshold


LeftClickModeList = ['Standard', 'Randomization', 'Experimental',  'FDP5', 'Butterfly', 'Liquid', 'Stable', 'VulcanFast', 'LegitFast',  'NoDelay',
                     'Disabled']
RightClickModeList = ['Standard', 'Randomization', 'Liquid', 'NCP', 'NoDelay', 'DropNoSlow', 'Stable', 'LegitFast', 'Disabled']
VK = {
    "LMB": 0x01, "RMB": 0x02, "MouseBtn4": 0x05, "MouseBtn5": 0x06, "Backspace": 0x08, "Tab": 0x09,
    "Enter": 0x0D, "Shift": 0x10, "Control": 0x11,
    "Alt": 0x12, "Space": 0x20, "Insert": 0x2D, "Delete": 0x2E, "0": 0x30, "1": 0x31,
    "2": 0x32, "3": 0x33, "4": 0x34, "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39, "A": 0x41, "B": 0x42,
    "C": 0x43, "D": 0x44, "E": 0x45, "F": 0x46, "G": 0x47, "H": 0x48, "I": 0x49, "J": 0x4A, "K": 0x4B, "L": 0x4C,
    "M": 0x4D, "N": 0x4E, "O": 0x4F, "P": 0x50, "Q": 0x51, "R": 0x52, "S": 0x53, "T": 0x54, "U": 0x55, "V": 0x56,
    "W": 0x57, "X": 0x58, "Y": 0x59, "Z": 0x5A, "F1": 0x70, "F2": 0x71,
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
            self.CAutoRod = 0
            self.EnableClick = False

            self.Window = Tk()
            self.Window.title('VirtualKeyBoard')
            self.Window.geometry(
                f'{int(((540 * GetSystemMetrics(SM_CXSCREEN) / 2560.0) + 1))}x{int((620 * GetSystemMetrics(SM_CYSCREEN) / 1600.0 + 1))}')

            self.Window.maxsize(600, 800)
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

            self.Label1 = Label(self.Window, text='RN Clicker2.4       Press F9 to toggle autoclick',
                                font=('Arial', 13))
            self.Label1.place(x=10, y=1)

            self.LeftCPS = Label(self.Window, text='Left CPS', font=('Arial', 17))
            self.LeftCPS.place(x=10, y=20)
            self.LeftMaxCPS = Scale(self.Window, from_=2, to=20,
                                    command=lambda event: self.UpdateWindow(), width=70, number_of_steps=36)
            self.LeftMaxCPS.place(x=150, y=25)
            self.LeftCPS1 = Label(self.Window, text='1337', font=('Arial', 17))
            self.LeftCPS1.place(x=230, y=20)

            self.LeftMinCPS = Scale(self.Window, from_=1, to=20,
                                    command=lambda event: self.UpdateWindow(), width=60, number_of_steps=38)
            self.LeftMinCPS.place(x=90, y=25)

            self.RightCPS = Label(self.Window, text='RightCPS', font=('Arial', 17))
            self.RightCPS.place(x=10, y=40)
            self.RightMaxCPS = Scale(self.Window, from_=2, to=20,
                                     command=lambda event: self.UpdateWindow(), width=70, number_of_steps=36)
            self.RightMaxCPS.place(x=150, y=45)
            self.RightCPS1 = Label(self.Window, text='1337', font=('Arial', 17))
            self.RightCPS1.place(x=230, y=40)

            self.RightMinCPS = Scale(self.Window, from_=1, to=20,
                                     command=lambda event: self.UpdateWindow(), width=60, number_of_steps=38)
            self.RightMinCPS.place(x=90, y=45)

            self.ExtraClicksTimes1 = Label(self.Window, text='ExtraClicksTimes', font=('Arial', 16))
            self.ExtraClicksTimes1.place(x=10, y=61)
            self.ExtraClicksTimes = Scale(self.Window, from_=0, to=64,
                                          command=lambda event: self.UpdateWindow(), width=100, number_of_steps=65)
            self.ExtraClicksTimes.place(x=140, y=65)
            self.ExtraClicksTimes2 = Label(self.Window, text='1337', font=('Arial', 17), height=1)
            self.ExtraClicksTimes2.place(x=250, y=63)

            self.DoubleClickRate1 = Label(self.Window, text='DoubleClickRate', font=('Arial', 16))
            self.DoubleClickRate1.place(x=10, y=83)
            self.DoubleClickRate = Scale(self.Window,
                                         from_=0, to=100, width=100, command=lambda event: self.UpdateWindow(),
                                         number_of_steps=200)

            self.DoubleClickRate.place(x=130, y=84)
            self.DoubleClickRate2 = Label(self.Window, text='1337%', font=('Arial', 16))
            self.DoubleClickRate2.place(x=230, y=80)

            self.BlockRate1 = Label(self.Window, text='BlockHitRate', font=('Arial', 16))
            self.BlockRate1.place(x=10, y=103)
            self.BlockRate = Scale(self.Window,
                                   from_=0, to=100, width=100, command=lambda event: self.UpdateWindow(),
                                   number_of_steps=200)
            self.BlockRate.place(x=130, y=105)
            self.BlockRate2 = Label(self.Window, text='1337%', font=('Arial', 16))
            self.BlockRate2.place(x=230, y=100)

            self.LeftMode1 = Label(self.Window, text='Left Mode', font=('Arial', 17))
            self.LeftMode1.place(x=10, y=125)
            self.LeftMode = Combobox(self.Window, state='readonly', values=LeftClickModeList, width=140, height=24,
                                     font=('Arial', 14), dropdown_font=('Arial', 14))
            self.LeftMode.place(x=130, y=125)
            self.RightMode1 = Label(self.Window, text='RightMode', font=('Arial', 17))
            self.RightMode1.place(x=10, y=150)
            self.RightMode = Combobox(self.Window, state='readonly', values=RightClickModeList, width=140, height=24,
                                      font=('Arial', 14), dropdown_font=('Arial', 14))
            self.RightMode.place(x=130, y=150)

            self.LeftKey1 = Label(self.Window, text='Left Key', font=('Arial', 17))
            self.LeftKey1.place(x=10, y=175)
            self.LeftKey = Combobox(self.Window, state='readonly', values=Name, width=140, height=24,
                                    font=('Arial', 14), dropdown_font=('Arial', 14))
            self.LeftKey.place(x=130, y=175)

            self.RightKey1 = Label(self.Window, text='RightKey', font=('Arial', 17))
            self.RightKey1.place(x=10, y=200)
            self.RightKey = Combobox(self.Window, state='readonly', values=Name, width=140, font=('Arial', 14),
                                     dropdown_font=('Arial', 14), height=24)
            self.RightKey.place(x=130, y=200)

            self.ShiftDisable1 = Label(self.Window, text='ShiftDisable', font=('Arial', 17))
            self.ShiftDisable1.place(x=10, y=225)
            self.ShiftDisable = Combobox(self.Window, state='readonly',
                                         values=['Left', 'Right', 'Both', 'Right-ShiftOnly', 'None'],
                                         width=140, height=24,
                                         font=('Arial', 14), dropdown_font=('Arial', 14))
            self.ShiftDisable.place(x=130, y=225)

            self.Topmost = BooleanVar()
            self.Topmost1 = Checkbutton(self.Window, text='AlwaysOnTop', variable=self.Topmost,
                                        command=lambda: self.UpdateWindow(), font=('Arial', 14), hover=False,
                                        border_width=2)
            self.Topmost1.place(x=10, y=250)

            self.InvenToryCheck = BooleanVar()
            self.InvenToryCheck1 = Checkbutton(self.Window, text='InvCheck', font=('Arial', 14),
                                               variable=self.InvenToryCheck, hover=False, border_width=2)
            self.InvenToryCheck1.place(x=10, y=275)

            self.NoToggleSound = BooleanVar()
            self.NoToggleSound1 = Checkbutton(self.Window, text='NoToggleSound', font=('Arial', 14),
                                              variable=self.NoToggleSound, hover=False, border_width=2)
            self.NoToggleSound1.place(x=150, y=275)

            self.Jitter = BooleanVar()
            self.Jitter1 = Checkbutton(self.Window, text='JitterClick', font=('Arial', 14), variable=self.Jitter,
                                       hover=False, border_width=2)
            self.Jitter1.place(x=150, y=300)

            self.AutoRod = BooleanVar()
            self.AutoRod1 = Checkbutton(self.Window, text='AutoRod', font=('Arial', 14), variable=self.AutoRod,
                                        hover=False, border_width=2)
            self.AutoRod1.place(x=10, y=300)

            self.AutoHideWindow = BooleanVar()
            self.AutoHideWindow1 = Checkbutton(self.Window, text='AutoHideWindow', font=('Arial', 14),
                                               variable=self.AutoHideWindow,
                                               hover=False, border_width=2, command=lambda: self.SetDisableClick())
            self.AutoHideWindow1.place(x=150, y=250)

            self.selfDestruct = CTkButton(self.Window, text='SelfDestruct', font=('Arial', 14),
                                          border_width=2, width=15, height=5, fg_color='black',
                                          command=lambda: SelfDeStRuct(root=self.Window))
            self.selfDestruct.place(x=10, y=325)

            self.RightExtraClicks = BooleanVar()
            self.RightExtraClicks1 = Checkbutton(self.Window, text='ExtraRightClicks', font=('Arial', 14),
                                                 variable=self.RightExtraClicks, hover=False, border_width=2)
            self.RightExtraClicks1.place(x=150, y=325)

            self.ExtraClicksTimes.set(0)
            self.ShiftDisable.set('None')
            self.LeftKey.set('MouseBtn5')
            self.RightKey.set('MouseBtn4')
            self.RightMode.set('Standard')
            self.LeftMode.set('Standard')
            self.LeftMaxCPS.set(13.5)
            self.RightMaxCPS.set(13.5)
            self.LeftMinCPS.set(7)
            self.RightMinCPS.set(7)
            self.DoubleClickRate.set(0)
            self.BlockRate.set(0)
            self.UpdateWindow()
            self.Window.after(1500, lambda: self.Main())
            self.Window.mainloop()

        def Main(self):
            LeftMode = self.LeftMode.get()
            RightMode = self.RightMode.get()
            if IsPressed(0x78):  # F9
                if self.EnableClick:
                    self.EnableClick = False
                    self.selfDestruct.configure(fg_color='blue')
                    self.Window.after(500, lambda: self.selfDestruct.configure(fg_color='transparent'))
                    self.Window.update()
                    if not self.NoToggleSound.get():
                        Beep(500, 150)
                    else:
                        sleep(0.5)
                    if self.AutoHideWindow.get():
                        self.Window.attributes('-alpha', 1)
                        self.Window.title('VirtualKeyBoard')
                        self.Window.geometry(
                            f'{int(((590 * GetSystemMetrics(SM_CXSCREEN) / 2560.0) + 1))}x{int((630 * GetSystemMetrics(SM_CYSCREEN) / 1600.0 + 1))}')
                else:
                    self.EnableClick = True
                    self.selfDestruct.configure(fg_color='red')
                    self.Window.after(500, lambda: self.selfDestruct.configure(fg_color='transparent'))
                    self.Window.update()
                    if not self.NoToggleSound.get():
                        Beep(1000, 150)
                    else:
                        sleep(0.5)
                    if self.AutoHideWindow.get():
                        self.Window.attributes('-alpha', 0)
                        self.Window.title(' ')
                        self.Window.geometry('0x0')
            if self.EnableClick and (
                    1 if not self.InvenToryCheck.get() else IsCurSorInCenTer(self.MouseController, 30)):
                if (LeftMode != 'Disabled' and IsPressed(VK[self.LeftKey.get()])) and (
                        1 if self.ShiftDisable.get() in ['Right', 'None'] else not IsPressed(VK['Shift'])):

                    if self.Jitter.get():
                        mouse_event(MOUSEEVENTF_MOVE, Randint(-2, 3), Randint(-3, 2))

                    BlockHit = False
                    self.CAutoRod += 1

                    if Randint(0, 99) <= self.BlockRate.get() - 1:
                        BlockHit = True
                        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

                    for _ in range(int(self.ExtraClicksTimes.get()) + 1 + (1 if Randint(0, 99) <= self.DoubleClickRate.get() - 1 else 0)):
                        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

                    if LeftMode not in ['NoDelay']:
                        sleep(0.017)

                    if self.LeftKey.get() != 'LMB':
                        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    if BlockHit:
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

                    self.VulcanClickCount += 1

                    if LeftMode == 'Standard':
                        sleep(0.6 / Randint(int(self.LeftMinCPS.get()), int(self.LeftMaxCPS.get())))
                    elif LeftMode == 'VulcanFast':
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
                        sleep(0.42 / (int(self.LeftMaxCPS.get()) * 1.5))
                    elif LeftMode == 'Liquid':
                        sleep(((Randint(1000, 9999) / 10000) * (
                            1000 / self.LeftMinCPS.get() - 1000 / self.LeftMaxCPS.get() + 1) + 1000 / self.LeftMaxCPS.get()) / 1000)
                    elif LeftMode == 'FDP5':
                        sleep((Randint(50, 74) if Randint(1, 7) == 1 else (
                            87 if Randint(1, 7) <= 2 else Randint(84, 89))) / 1400)
                    elif LeftMode == 'Butterfly':
                        sleep((Randint(225, 250) if Randint(1, 10) == 1 else (
                            Randint(89, 94) if Randint(1, 6) == 1 else (
                                Randint(95, 103) if Randint(1, 3) == 1 else (
                                    Randint(115, 123) if Randint(1, 3) == 1 else (
                                        Randint(131, 136) if Randint(1, 2) == 1 else Randint(165, 174)))))) / 10000)
                    elif LeftMode == 'Experimental':
                        self.MouseController.scroll(0, -5)
                        sleep(0.5 / Randint(int(self.LeftMinCPS.get()), int(self.LeftMaxCPS.get())))
                        self.MouseController.scroll(0, 5)
                    elif LeftMode == 'Randomization':
                        sleep((Randint(65, 135) / 100) * (
                            (Randint(25, 85) / 100) / Randint(int(self.LeftMinCPS.get()),
                                                              int(self.LeftMaxCPS.get()))) *
                              (
                                  1 if Randint(1, 10) >= 5 else
                                  (Randint(65, 125)-1) / 100
                              )*((Randint(70, 140) / 100) if Randint(
                                int(self.LeftMinCPS.get()),
                                int(self.LeftMaxCPS.get())) % 2 == 0 else
                                 Randint(50, 150) / 100
                              ) / (
                                  (Randint(8, 13)) /
                                  (Randint(9, 11))
                              ))
                    if self.AutoRod.get() and self.CAutoRod >= Randint(int(self.LeftMinCPS.get()), int(self.LeftMaxCPS.get())):
                        self.MouseController.scroll(0, -5)
                        sleep(0.01)
                        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                        sleep(0.12)
                        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                        sleep(0.03)
                        self.MouseController.scroll(0, 5)
                        self.CAutoRod = 0

                if (RightMode != 'Disabled' and IsPressed(VK[self.RightKey.get()])) and ((
                    1 if self.ShiftDisable.get() in ['Left', 'None'] else (not IsPressed(
                        VK['Shift'])) if self.ShiftDisable.get() != 'Right-ShiftOnly' else IsPressed(VK['Shift']))):
                    for _ in range(1+(0 if not self.RightExtraClicks.get() else self.ExtraClicksTimes.get())):
                        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                    if RightMode not in ['NoDelay']:
                        sleep(0.017)
                    if self.RightKey.get() != 'RMB':
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
                    elif RightMode == 'Stable':
                        sleep(0.5 / (int(self.RightMaxCPS.get()) * 1.5))
                    elif RightMode == 'Randomization':
                        sleep((Randint(65, 135) / 100) * (
                            (Randint(25, 85) / 100) / Randint(int(self.RightMinCPS.get()),
                                                              int(self.RightMaxCPS.get()))) *
                              (
                                  1 if Randint(1, 10) >= 5 else
                                  (Randint(65, 125) - 1) / 100
                              ) * ((Randint(85, 110) / 100) if Randint(
                                int(self.RightMinCPS.get()),
                                int(self.RightMaxCPS.get())) % 2 == 0 else
                                 Randint(90, 115) / 100
                              ) / (
                                  (Randint(8, 13)) /
                                  (Randint(9, 11))
                              ))
            self.Window.after(3, lambda: self.Main())

        def UpdateWindow(self):
            self.Window.attributes('-topmost', self.Topmost.get())
            if self.LeftMaxCPS.get() < self.LeftMinCPS.get():
                self.LeftMinCPS.set(self.LeftMaxCPS.get())
            if self.RightMaxCPS.get() < self.RightMinCPS.get():
                self.RightMinCPS.set(self.RightMaxCPS.get())
            self.LeftMinCPS.configure(to=self.LeftMaxCPS.get(), number_of_steps=2 * (self.LeftMaxCPS.get() - 1))
            self.RightMinCPS.configure(to=self.RightMaxCPS.get(), number_of_steps=2 * (self.RightMaxCPS.get() - 1))

            self.LeftCPS1.configure(text='%.1f-%.1f' % (self.LeftMinCPS.get(), self.LeftMaxCPS.get()))
            self.RightCPS1.configure(text='%.1f-%.1f' % (self.RightMinCPS.get(), self.RightMaxCPS.get()))
            self.DoubleClickRate2.configure(text='%.1f' % (self.DoubleClickRate.get()) + '%')
            self.ExtraClicksTimes2.configure(text=int(self.ExtraClicksTimes.get()))
            self.BlockRate2.configure(text='%.1f' % (self.BlockRate.get()) + '%')

        def SetDisableClick(self):
            self.EnableClick = False


if __name__ == '__main__':
    AutoClickerWindow = _0x16z.AutoClicker()
