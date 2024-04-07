import os

if __name__ == "__main__":
    location = input('File name: ')
    scene = input('Scene: ')
    os.system('manim {} {}'.format(location, scene))
