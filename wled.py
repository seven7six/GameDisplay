import requests
import json
import dictionary as d

wled_ip = "192.168.0.32"  # Replace with your WLED device's IP

def clear_wled():
    # TODO write this
    pass

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
    clear_wled()
    text_content = text_content.upper() # LED DISPLAY IS UPPERCASE ONLY
    led_map = ''
    grid = d.grid
    for letter in text_content:
        grid = d.assemble(grid, d.letter[letter], line)

    # testing only
    for x in grid:
        print(x)
    # TODO - format i in payload properly substituting fg_color for 1 and bg_color for 0

    payload = {
        "on": True,
        "bri": 128,
        "v": True,
        "seg": {
            "i":[grid]
        }
    }

    print(payload)

    # headers = {'Content-Type': 'application/json'}
    # try:
    #     response = requests.post(f"http://{wled_ip}/json/state", data=json.dumps(payload), headers=headers)
    #     response.raise_for_status()  # Raise an exception for bad status codes
    #     print(f"Text '{text_content}' sent successfully to WLED.")
    # except requests.exceptions.RequestException as e:
    #     print(f"Error sending text to WLED: {e}")
# Example
# set_wled_text("GO BEARS!")
# set_pixels("adf")
static_wled_text("AB12:",0,"ffffff","000000")

