import requests
import json

wled_ip = "192.168.0.32"  # Replace with your WLED device's IP

def set_wled_text(text_content, effect_id=50, speed=128):
    payload = {
        "on": True,
        "bri": 200,
        "seg": [
            {
                "id": 0,
                "n": text_content,
                "fx": effect_id,
                "sx": speed
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

# Example usage
set_wled_text("GO BEARS!")