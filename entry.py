"""
Use the keyboard model to insert text and run command

@author: Tang142857
@project: workspace
@file: entry.py
@date: 2021-07-01
Copyright(c): DFSA Software Develop Center
"""
from pynput import keyboard
import time
import tqdm


def exe_lines(command_list: list):
    time.sleep(10)
    ctr = keyboard.Controller()
    print(f'Over view totle {len(command_list)}')
    for command in tqdm.tqdm(command_list):
        # type command and press enter and release
        time.sleep(0.5)
        ctr.type(command)
        ctr.press(keyboard.Key.enter)
        ctr.release(keyboard.Key.enter)


if __name__ == '__main__':
    commands = ['echo hello', 'echo hello']
    exe_lines(commands)
