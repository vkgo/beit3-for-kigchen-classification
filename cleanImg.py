from PIL import Image
import os

def check_images(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            check_images(filepath)
        else:
            try:
                with Image.open(filepath) as img:
                    img.verify()
            except (IOError, SyntaxError) as e:
                print(f"{filepath} cannot be opened: {e}")
                os.remove(filepath)
                

def check_truncated_images(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            check_truncated_images(filepath)
        else:
            try:
                with Image.open(filepath) as img:
                    img.load()
            except OSError as e:
                print(f"{filepath} is truncated: {e}")
                os.remove(filepath)
        

targetdir = "./data/kitchen"
check_images(targetdir)
check_truncated_images(targetdir)
