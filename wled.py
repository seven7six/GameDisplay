import requests
import json
import dictionary as d

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
                while z < len(letter[row-1]):
                    grid[row][col] = letter[row-1][z]
                    z += 1
                    col += 1
                row += 1
                col = 0
            elif line == 1 and 9 <= row <= 15 and grid[row][col] == -1:
                z = 0
                while z < len(letter[row-9]):
                    # print(row)
                    grid[row][col] = letter[row-9][z]
                    z += 1
                    col += 1
                if row <15:
                    row += 1
                else:
                    break
                col = 0
            else:
                col += 1
            # print(f"{row},{col}")
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
        "v": True,
        "seg": {
            "i": led_map
        }
    }
    print(payload)

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

def static_wled_text(text_content, line, fg_color, bg_color):
    text_content = text_content.upper() # LED DISPLAY IS UPPERCASE ONLY but allow lowercase and convert it
    led_map = []
    grid = d.clear_grid # get the blank grid from the dictionary module
    for x in d.clear_grid:
        print(x)
    for letter in text_content:
        grid = assemble(grid, d.letter[letter], line)

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
    print(payload)

    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(f"http://{wled_ip}/json/state", data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Text '{text_content}' sent successfully to WLED.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending text to WLED: {e}")
# Examples
# set_wled_text("GO BEARS!")
# set_pixels("adf")
static_wled_text("line: 0",0,"ff2500","000000")
static_wled_text("line: 1",1,"ff2500","000000")
# static_wled_text("line: 2",0,"ff2500","000000")
# static_wled_text("line: 3",1,"ff2500","000000")
# clear_wled()
