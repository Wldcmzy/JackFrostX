import pyautogui
from io import BytesIO
from PIL import Image


def screenshot(size: tuple[int, int]) -> bytes:
    img: Image.Image = pyautogui.screenshot()
    img = img.resize(size)
    bio = BytesIO()
    img.save(bio, format='JPEG', quality=60)
    frame = bio.getvalue()
    return frame
