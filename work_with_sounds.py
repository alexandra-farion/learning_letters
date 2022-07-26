import pygame
import os
sounds_folder = "sounds"


def load_sound(name, volume=1):
    sound = pygame.mixer.Sound(os.path.join(sounds_folder, name))
    sound.set_volume(volume)
    return sound
