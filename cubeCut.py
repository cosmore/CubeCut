#!/usr/bin/env python3
__author__ = "cosmok holding"
__copyright__ = "Copyright 2017"
__credits__ = ["musiker-board.de"]
__license__ = "LGPL"
__version__ = "1.0.0"
__email__ = "chris@cosmok.de"

from flask import Flask, render_template
import pyautogui
import socket


def getLocalIp():
    return socket.gethostbyname(socket.gethostname())

# Thats all to configure for the app
AppName = "cubase"
WebPort = 5555
app = Flask(__name__)
app.config['WebPort'] = WebPort
app.config['IP'] = getLocalIp()
app.config['app'] = AppName


# TODO limit your whitelist
WhiteList = "0.0.0.0"

async def sendCommand(command):
    '''Parse the command string and construct the shortcut'''
    keys = []
    special = []

    # list of characters see pyautogui documentation
    # http://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
    # real + is 'plus' in this case :)

    specialKeys = ['alt', 'ctrl', 'shift',
                   'ctrlleft', 'ctrlright',
                   'shiftleft', 'shiftright',
                   'altleft', 'altright'
                   ]

    keyStrings = command.split('+')

    if 'plus' in keyStrings:
        keyStrings.append('+')
        keyStrings.remove('plus')

    for key in keyStrings:
        if key in specialKeys:
            special.append(key)
        else:
            keys.append(key)

    # Trigger keys:
    if len(special) > 0:
        for spec in special:
            pyautogui.keyDown(spec)

    for key in keys:
        pyautogui.keyDown(key)
    for key in keys:
        pyautogui.keyUp(key)

    if len(special) > 0:
        for spec in special:
            pyautogui.keyUp(spec)

    await print("sent")

#/sendCommand


# WebUi
@app.route('/{0}/view/index.html'.format(AppName))
def index():
    return render_template('index.html')

# RestApi


@app.route('/{0}/command/<command>'.format(AppName))
def triggerCommands(command):
    print("incoming command: {0}".format(command))
    sendCommand(command)
    return "200"


@app.route('/{0}/external/<command>'.format(AppName))
def triggerAppCommands(command):
    print("incoming exteral command: {0}".format(command))
    # TODO implement your systemcall or whatever here
    return "sent"

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True, host=WhiteList, port=WebPort)
