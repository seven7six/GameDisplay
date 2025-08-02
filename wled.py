import requests
import json

wled_ip = "192.168.0.32"  # Replace with your WLED device's IP

def set_wled_text(text_content, effect_id=122, speed=128):
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

def set_pixels(text_content):
    payload = {
        "on": True,
        "bri": 128,
        "v": True,
        "seg": {
            "i":["undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","000000","000000","ff2500","ff2500","ff2500","undefined","ff2500","undefined","ff2500","undefined","ff2500","000000","000000","undefined","undefined","undefined","000000","ff2500","ff2500","ff2500","000000","ff2500","ff2500","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","000000","undefined","ff2500","undefined","undefined","undefined","ff2500","undefined","ff2500","undefined","ff2500","undefined","000000","undefined","undefined","undefined","undefined","undefined","000000","ff2500","000000","ff2500","000000","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","000000","undefined","ff2500","undefined","undefined","undefined","ff2500","ff2500","ff2500","undefined","ff2500","undefined","000000","000000","ff2500","ff2500","undefined","ff2500","ff2500","ff2500","000000","ff2500","000000","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","000000","undefined","ff2500","undefined","undefined","undefined","ff2500","undefined","ff2500","undefined","ff2500","undefined","000000","undefined","undefined","undefined","undefined","undefined","000000","ff2500","000000","ff2500","000000","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","000000","000000","ff2500","ff2500","ff2500","000000","ff2500","undefined","ff2500","undefined","ff2500","000000","000000","undefined","undefined","undefined","000000","ff2500","ff2500","ff2500","000000","ff2500","ff2500","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","ff2500","ff2500","000000","ff2500","undefined","ff2500","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","ff2500","ff2500","undefined","ff2500","ff2500","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","undefined","ff2500","undefined","ff2500","undefined","ff2500","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","ff2500","ff2500","undefined","ff2500","ff2500","ff2500","undefined","ff2500","undefined","undefined","undefined","ff2500","ff2500","undefined","ff2500","ff2500","ff2500","undefined","ff2500","ff2500","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","undefined","undefined","undefined","ff2500","undefined","ff2500","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","undefined","undefined","undefined","ff2500","undefined","ff2500","undefined","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","ff2500","ff2500","ff2500","undefined","ff2500","ff2500","ff2500","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined","undefined"]
        }
    }

    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(f"http://{wled_ip}/json/state", data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(f"Text '{text_content}' sent successfully to WLED.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending text to WLED: {e}")
# Example
# set_wled_text("GO BEARS!")
# set_pixels("adf")

