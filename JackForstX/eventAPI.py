import pyautogui
from io import BytesIO
from PIL import Image


def screenshot() -> bytes:
    img: Image.Image = pyautogui.screenshot()
    img = img.resize((640, 360))
    bio = BytesIO()
    img.save(bio, format='JPEG', quality=60)
    frame = bio.getvalue()
    return frame
