"""
Use the keyboard model to insert text and run command

@author: Tang142857
@project: workspace
@file: entry.py
@date: 2021-07-01
Copyright(c): DFSA Software Develop Center
"""
import time

import pyautogui
import tqdm


def exe_lines(command_list: list):
    if __name__ == "__main__":
        time.sleep(5)
    print(f'Over view totle {len(command_list)}')
    for command in tqdm.tqdm(command_list):
        # type command and press enter and release
        time.sleep(0.1)
        pyautogui.press('/')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write(command, interval=0.1)
        pyautogui.press('enter')


if __name__ == '__main__':
    commands = ['echo hello', 'echo hello']
    exe_lines(commands)
