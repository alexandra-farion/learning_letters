import pygame
import os


def work_image(name):
    if name != 'arrow.png':
        fullname = os.path.join(os.path.dirname(__file__), 'data', name)
        image = pygame.image.load(fullname)
    else:
        fullname = os.path.join(os.path.dirname(__file__), 'data', name)
        image = pygame.image.load(fullname).convert_alpha()
    return image


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image
