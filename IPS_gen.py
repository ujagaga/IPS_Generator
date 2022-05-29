#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Written for python3. Formated for Serbian language, but feel free to adjust for any other.
'''

from tkinter import PhotoImage, BOTTOM, Tk, Button, Label, Entry, Toplevel, BitmapImage
import sys
from os import path
from icon_data import icon_image
import pyqrcode

# Default configuration
recipient = "Radina Radionica"
account_no = 265000000036411673
transaction_code = 189
default_msg = "Unesite iznos za plaćanje"

# Language specific messages in serbian:
RECIPIENT = "primaoc"
ACCOUNT = "racun"
CODE = "sifra"

if 'linux' in sys.platform:
    OS_PLATFORM = 'linux'
else:
    OS_PLATFORM = 'windows'

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    current_path = path.dirname(sys.executable)
    if "windows" in OS_PLATFORM:
        extension = ".exe"
    else:
        extension = ""
elif __file__:
    current_path = path.dirname(path.realpath(__file__))
    extension = ".py"

cfg_file = path.join(current_path, "config.txt")


APP_TITLE = "IPS Generator"
COLOR_BACKGROUND = "#424344"
COLOR_LABEL_BACKGROUND_LIGHT = "#424344"
COLOR_LABEL_BACKGROUND_DARK = "#383939"
COLOR_LABEL_TEXT = "#FFF0E7"
COLOR_BTN_BACKGROUND = "#424344"
COLOR_BTN_TEXT = "#f48642"
COLOR_BTNPANEL_BACKGROUND = "#424344"
COLOR_DAY_BACKGROUND = "#111111"
COLOR_LABEL_TITLE_BACKGROUND = "#111111"
COLOR_LABEL_HOVER = "#908D8D"


class InfoBox(Tk):
    def __init__(self, value, bitmap_image):
        global icon_image
        global APP_TITLE
        global COLOR_LABEL_BACKGROUND_LIGHT
        global COLOR_LABEL_BACKGROUND_DARK
        global COLOR_BACKGROUND
        global COLOR_LABEL_TEXT
        global COLOR_BTN_TEXT
        global COLOR_BTN_BACKGROUND
        global COLOR_BTNPANEL_BACKGROUND
        global COLOR_DAY_BACKGROUND
        global COLOR_LABEL_TITLE_BACKGROUND
        global account_no
        global recipient
        global transaction_code

        Toplevel.__init__(self)

        self.call('wm', 'iconphoto', self._w, PhotoImage(data=icon_image))
        self.attributes("-topmost", True)
        self.title(APP_TITLE)
        self.minsize(300, 50)
        self.configure(background=COLOR_BACKGROUND)

        img_lbl = Label(self, bg='#FFFFFF', image=bitmap_image)
        img_lbl.pack(padx=50, pady=50)
        Label(self, text="Iznos: {}".format(value), wraplength=600, bg=COLOR_BTN_BACKGROUND, fg=COLOR_BTN_TEXT).pack(padx=10, pady=10)
        Button(self, text="U redu", command=self.dismiss, width=10).pack(side=BOTTOM, padx=10, pady=10)

        self.focus_force()
        self.bind('<KP_Enter>', self.dismiss)
        self.bind('<Return>', self.dismiss)
        self.bind('<Escape>', self.dismiss)

    def dismiss(self, event=None):
        self.wm_withdraw()
        self.destroy()
        self.quit()


class MainWindow(Tk):
    def __init__(self):
        global icon_image
        global APP_TITLE
        global COLOR_LABEL_BACKGROUND_LIGHT
        global COLOR_LABEL_BACKGROUND_DARK
        global COLOR_BACKGROUND
        global COLOR_LABEL_TEXT
        global COLOR_BTN_TEXT
        global COLOR_BTN_BACKGROUND
        global COLOR_BTNPANEL_BACKGROUND
        global COLOR_DAY_BACKGROUND
        global COLOR_LABEL_TITLE_BACKGROUND
        global default_msg
        global account_no
        global recipient
        global transaction_code

        Tk.__init__(self)

        self.call('wm', 'iconphoto', self._w, PhotoImage(data=icon_image))
        self.attributes("-topmost", True)
        self.title(APP_TITLE)
        self.minsize(300, 50)
        self.configure(background=COLOR_BACKGROUND)

        Label(self, text=default_msg, wraplength=600, bg=COLOR_BTN_BACKGROUND, fg=COLOR_BTN_TEXT).pack(padx=10, pady=10)

        self.input_text = Entry(self, width=50)
        self.input_text.pack(padx=10, pady=10)

        Button(self, text="OK", command=self.apply, width=10, bg=COLOR_BTN_BACKGROUND, fg=COLOR_BTN_TEXT).pack(padx=10, pady=5)

        self.focus_force()

        self.input_text.focus_set()
        self.bind('<Return>', self.apply)
        self.bind('<KP_Enter>', self.apply)
        self.bind('<Escape>', self.dismiss)

    def dismiss(self, event=None):
        self.wm_withdraw()
        self.destroy()
        self.quit()

    def apply(self, event=None):
        try:
            user_input = float(self.input_text.get().replace(',', '.'))

        except:
            user_input = float(0)

        payment_amounth = "{:.2f}".format(user_input).replace('.', ',')

        ips_data = "K:PR|V:01|C:1|R:{}|N:{}|SF:{}|I:RSD{}" \
                   "".format(account_no, recipient, transaction_code, payment_amounth).encode('utf-8')
        qr = pyqrcode.create(ips_data)
        img = BitmapImage(data=qr.xbm(scale=8))
        info = InfoBox(value=payment_amounth, bitmap_image=img)
        info.mainloop()

        self.wm_withdraw()
        self.destroy()
        self.quit()


try:
    if not path.exists(cfg_file):
        print("Writing initial configuration.")
        file = open(cfg_file, 'w+')
        file.write("{}={}".format(RECIPIENT, recipient))
        file.write("\n")
        file.write("{}={}".format(ACCOUNT, account_no))
        file.write("\n")
        file.write("{}={}".format(CODE, transaction_code))
        file.close()

    configfile = open(cfg_file, 'r')
    content = configfile.readlines()
    configfile.close()

    for line in content:
        line = line.strip()
        if not line.startswith("#"):
            data = line.split("=")
            name = data[0].strip()
            val = data[1].strip()

            if RECIPIENT in name:
                recipient = val
            elif ACCOUNT in name:
                account_no = int(val)
            elif CODE in name:
                transaction_code = int(val)

except:
    pass

main_app = MainWindow()
main_app.mainloop()
