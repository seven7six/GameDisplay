import requests
import json
import dictionary as d
import time

wled_ip = "192.168.0.32"  # Replace with your WLED device's IP


def assemble(grid, letter, line):
    """ the grid is my 32w x 16h LED display -1 denotes undefined, 1 is lit with a color, 0 is black, this display can write 2 lines, line can be 0,1"""

    # check if grid is full
    if line == 0:
        try:
            grid[0].index(-1)
        except:
            print("Error: Grid full")
            return grid
        if grid[0].index(-1)+len(letter[0]) > 32:
            print("Error: Grid full")
            return grid
    elif line == 1:
        try:
            grid[9].index(-1)
        except:
            print("Error: Grid full")
            return grid
        if grid[9].index(-1)+len(letter[0]) > 32:
            print("Error: Grid full")
            return grid

    # safety check passed push letter onto grid
    row = 0
    col = 0

    while row < len(grid):
        while col < len(grid[row]):
            if line == 0 and 1 <= row <= 7 and grid[row][col] == -1:
                z = 0
                while z < len(letter[row-1]) and col < 32:
                    grid[row][col] = letter[row-1][z]
                    z += 1
                    col += 1
                row += 1
                col = 0
            elif line == 1 and 9 <= row <= 15 and grid[row][col] == -1:
                z = 0
                while z < len(letter[row-9]):
                    grid[row][col] = letter[row-9][z]
                    z += 1
                    col += 1
                if row <15:
                    row += 1
                else:
                    return grid
                col = 0
            else:
                col += 1
        col = 0
        row += 1

    # troubleshooting only
    # for w in grid:
    #     print(w)

    return grid

def clear_wled():
    led_map = []
    count = 0
    while count < 512:
        led_map.append("undefined")
        count += 1

    payload = {
        "on": True,
        "bri": 128,
        "ps": -1,
        "pl": -1,
        "v": True,
        "seg": {
            "i": led_map
        }
    }
    # print(payload)

    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(f"http://{wled_ip}/json/state", data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Clear command sent successfully to WLED.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending text to WLED: {e}")

def scroll_wled_text(text_content, effect_id=122, speed=128):
    payload = {
        "on": True,
        "bri": 200,
        "seg": [
            {
                "id": 0,
                "n": text_content,
                "fx": effect_id,
                "sx": speed,
                "col": [[0, 0, 0],[255,55,0]]
            }
        ]
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(f"http://{wled_ip}/json/state", data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Text '{text_content}' sent successfully to WLED.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending text to WLED: {e}")

def static_wled_text(text_content1, text_content2, fg_color, bg_color, special=None):
    """text_content1 is the first line of text
    text_content2 is the second line of text
    fg_color is foreground color
    bg_color is background color
    special is the ability to place a letter anywhere (no error checking!!!) on the grid send a dictionary containing:
     {'x': 27,
      'y': 6,
      'val': "FINAL"}
      where x and y are the coordinates and val is the letter or symbol in the dictionary to place"""
    text_content1 = text_content1.upper() # LED DISPLAY IS UPPERCASE ONLY but allow lowercase and convert it
    text_content2 = text_content2.upper() # LED DISPLAY IS UPPERCASE ONLY but allow lowercase and convert it

    led_map = []
    # grid = d.clear_grid # get the blank grid from the dictionary module
    grid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

    for letter in text_content1:
        grid = assemble(grid, d.letter[letter],0)
    for letter in text_content2:
        grid = assemble(grid, d.letter[letter],1)

    if special is not None:
        for valuey in range(len(d.letter[special['val']][0])):
            for valuex in range(len(d.letter[special['val']])):
                grid[special['x']+valuex][special['y']+valuey] = d.letter[special['val']][valuex][valuey]

    for y in grid:
        for x in y:
            if x == -1:
                led_map.append("undefined")
            elif x == 1:
                led_map.append(fg_color)
            elif x == 0:
                led_map.append(bg_color)

    payload = {
        "on": True,
        "bri": 128,
        "v": True,
        "seg": {
            "i": led_map
        }
    }
    # print(payload)

    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(f"http://{wled_ip}/json/state", data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Text '{text_content1}' / '{text_content2}' sent successfully to WLED.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending text to WLED: {e}")

def celebrate():
    """create a preset using https://github.com/ajotanc/PixelMagicTool then find the id and modify these:
    'ps': 5, 'repeat': 3 as needed. I used this tool to resize my gif selecting center and crop
    https://ezgif.com/resize/ezgif-325e8de265b55d.gif"""
    # payload = {
    #     'on': True,
    #     'bri': 128,
    #     'transition': 7,
    #     'ps': -1,
    #     'pl': -1,
    #     'ledmap': 0,
    #     'AudioReactive': {'on': False},
    #     'nl': {'on': False, 'dur': 60, 'mode': 1, 'tbri': 0, 'rem': -1},
    #     'udpn': {'send': False, 'recv': True, 'sgrp': 1, 'rgrp': 1},
    #     'lor': 0,
    #     'mainseg': 0,
    #     'seg': [{
    #         'id': 0,
    #         'start': 0,
    #         'stop': 32,
    #         'startY': 0,
    #         'stopY': 16,
    #         'len': 32,
    #         'grp': 1,
    #         'spc': 0,
    #         'of': 0,
    #         'on': True,
    #         'frz': False,
    #         'bri': 255,
    #         'cct': 127,
    #         'set': 0,
    #         'n': 'hello',
    #         'col': [[255, 94, 242], [0, 0, 0], [0, 0, 0]],
    #         'fx': 167,
    #         'sx': 128,
    #         'ix': 128,
    #         'pal': 0,
    #         'c1': 128,
    #         'c2': 128,
    #         'c3': 16,
    #         'sel': True,
    #         'rev': False,
    #         'mi': False,
    #         'rY': False,
    #         'mY': False,
    #         'tp': False,
    #         'o1': False,
    #         'o2': False,
    #         'o3': False,
    #         'si': 0,
    #         'm12': 0
    #     }]
    # }
    payload = {
        'on': True,
        'bri': 128,
        'transition': 7,
        'ps': 5,
        'repeat': 3,
        'ledmap': 0,
        'AudioReactive': {'on': False},
        'nl': {'on': False, 'dur': 60, 'mode': 1, 'tbri': 0, 'rem': -1},
        'udpn': {'send': False, 'recv': True, 'sgrp': 1, 'rgrp': 1},
        'lor': 0,
        'mainseg': 0,
        'seg': [
            {'id': 0,
             'start': 0,
             'stop': 32,
             'startY': 0,
             'stopY': 16,
             'len': 32,
             'grp': 1,
             'spc': 0,
             'of': 0,
             'on': True,
             'frz': True,
             'bri': 255,
             'cct': 127,
             'set': 0,
             'col': [[255, 160, 0], [0, 0, 0], [0, 0, 0]],
             'fx': 0,
             'sx': 128,
             'ix': 128,
             'pal': 0,
             'c1': 128,
             'c2': 128,
             'c3': 16,
             'sel': True,
             'rev': False,
             'mi': False,
             'rY': False,
             'mY': False,
             'tp': False,
             'o1': False,
             'o2': False,
             'o3': False,
             'si': 0,
             'm12': 0
             }
        ]
}
    # print(payload)

    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(f"http://{wled_ip}/json/state", data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Layers sent successfully to WLED.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending text to WLED: {e}")
    time.sleep(6) # let the animation run tweak this longer if the animation is frozen to the screen after playing
    clear_wled()

# Examples
# set_wled_text("GO BEARS!")
# set_pixels("adf")
# static_wled_text("line: 0","line: 1","ff2500","000000")
# static_wled_text("line: 1","line: 2","ff2500","000000")
# clear_wled()
# celebrate()
#
# # get state
# response = requests.get(f"http://{wled_ip}/json/state")
# print(response.json())