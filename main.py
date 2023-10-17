import os
import json
import time
from time import sleep
from screen import *
import random
from pynput.mouse import Button, Controller

def bounce(release_list, timing_list, mouse):
    mouse.position = (333, 444)

    if len(release_list) != 0 and len(timing_list) != 0:
        timing_time = 0
        for release_time in range(len(release_list)):
            timing_time += 1
            timing_var = timing_list[timing_time - 1]
            release_var = release_list[release_time - 1]
            sleep(timing_var)
            mouse.press(Button.left)
            sleep(release_var)
            mouse.release(Button.left)

    timing_var = random.uniform(0.3, 3)
    release_var = random.uniform(0.5, 2)
    timing_list.append(timing_var)
    release_list.append(release_var)
    sleep(timing_var)
    mouse.press(Button.left)
    sleep(release_var)
    mouse.release(Button.left)

def save(path, data):
    with open (path, 'w') as file:
        json.dump(data, file)

def load(path):
    with open (path, 'r') as file:
        var = json.load(file)
        return var
    
def is_able_to_read(path):
    return os.path.getsize(path)


def main():
    mouse = Controller()

    if not is_able_to_read('memory/memory retray/timing memory.json'):
        release_list = []
        timing_list = []
    else:
        release_list = load('memory/memory retray/release memory.json')
        timing_list = load('memory/memory retray/timing memory.json')
    death_counter = 0
    passing = True



    #main loop
    while passing:

        last_release_list = release_list

        first_screenshot = get_screen()
        sleep(0.007)
        second_screenshot = get_screen()

        if not isalive(first_screenshot, second_screenshot):
            if len(release_list) != 0 and len(timing_list) != 0:
                release_list.pop()
                timing_list.pop()
                if len(last_release_list) == len(release_list):
                    death_counter += 1
                    if death_counter == 5:
                        release_list.pop()
                        timing_list.pop()
                        death_counter = 0
                        last_release_list = release_list
            mouse.position = (270, 590)
            sleep(0.3)
            mouse.click(Button.left)

        bounce(release_list, timing_list, mouse)

            
        print(f'TIMING LIST: {timing_list}')
        print(f'RELEASE LIST: {release_list}')
        print('-------------------------------------------------------------------------------------------------------')

        save('memory/memory retray/timing memory.json', timing_list)
        save('memory/memory retray/release memory.json', release_list)



if __name__ == '__main__':
    main()