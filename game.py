import pygame
import random
import os
import sys
from os import path


WIDTH = 1550
HEIGHT = 900
FPS = 60

pygame.init()
pygame.mixer.init()

true_answer = 0
new_round = False
FPS = 50
picture1 = ''
picture2 = ''
picture3 = ''
image_letter = ''
alphabet = {'а.png': 'а1.png', 'б.png': 'б1.png', 'в.png': 'в1.png', 'г.png': 'г1.png',
            'д.png': 'д1.png', 'е.png': 'е1.png', 'ё.png': 'ё1.png', 'ж.png': 'ж1.png',
            'з.png': 'з1.png', 'и.png': 'и1.png', 'й.png': 'й1.png', 'к.png': 'к1.png',
            'л.png': 'л1.png', 'м.png': 'м1.png', 'н.png': 'н1.png', 'о.png': 'о1.png',
            'п.png': 'п1.png', 'р.png': 'р1.png', 'с.png': 'с1.png', 'т.png': 'т1.png',
            'у.png': 'у1.png', 'ф.png': 'ф1.png', 'х.png': 'х1.png', 'ц.png': 'ц1.png',
            'ч.png': 'ч1.png', 'ш.png': 'ш1.png', 'щ.png': 'щ1.png', 'э.png': 'э1.png',
            'ю.png': 'ю1.png', 'я.png': 'я1.png'}
image_for_buttons = ['а1.png', 'б1.png',  'в1.png', 'г1.png', 'д1.png', 'е1.png', 'ё1.png', 'ж1.png',
                     'з1.png', 'и1.png',  'й1.png', 'к1.png', 'л1.png', 'м1.png', 'н1.png',  'о1.png',
                     'п1.png', 'р1.png',  'с1.png',  'т1.png', 'у1.png', 'ф1.png', 'х1.png',  'ц1.png',
                     'ч1.png', 'ш1.png',  'щ1.png', 'э1.png', 'ю1.png', 'я1.png']
image_for_buttons_copy = ['а1.png', 'б1.png',  'в1.png', 'г1.png', 'д1.png', 'е1.png', 'ё1.png', 'ж1.png',
                          'з1.png', 'и1.png',  'й1.png', 'к1.png', 'л1.png', 'м1.png', 'н1.png',  'о1.png',
                          'п1.png', 'р1.png',  'с1.png',  'т1.png', 'у1.png', 'ф1.png', 'х1.png',  'ц1.png',
                          'ч1.png', 'ш1.png',  'щ1.png', 'э1.png', 'ю1.png', 'я1.png']


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


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = "Нажмите, чтобы начать"
    fon = pygame.transform.scale(load_image('444.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(intro_text, 1, pygame.Color('orange'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 110
    intro_rect.x = 750
    screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS ** 2)


def end_screen():
    intro_text = "Ты выиграл! Поздравляю!"
    fon = pygame.transform.scale(load_image('444.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(intro_text, 1, pygame.Color('red'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 110
    intro_rect.x = 750
    screen.blit(string_rendered, intro_rect)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                                    event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()


def new():
    global image_letter
    global picture1
    global picture2
    global picture3
    global true_answer
    global alphabet
    image_letter = list(alphabet.keys())[0]
    true_answer = random.randint(1, 3)
    if true_answer == 1:
        picture1 = image_for_buttons[0]
        picture2 = random.choice(image_for_buttons_copy)
        picture3 = random.choice(image_for_buttons_copy)
        while picture3 == picture2 or picture3 == picture1 or picture1 == picture2:
            picture2 = random.choice(image_for_buttons_copy)
            picture3 = random.choice(image_for_buttons_copy)
    elif true_answer == 2:
        picture1 = random.choice(image_for_buttons_copy)
        picture3 = random.choice(image_for_buttons_copy)
        picture2 = image_for_buttons[0]
        while picture3 == picture2 or picture3 == picture1 or picture1 == picture2:
            picture1 = random.choice(image_for_buttons_copy)
            picture3 = random.choice(image_for_buttons_copy)
    else:
        picture3 = image_for_buttons[0]
        picture1 = random.choice(image_for_buttons_copy)
        picture2 = random.choice(image_for_buttons_copy)
        while picture3 == picture2 or picture3 == picture1 or picture1 == picture2:
            picture2 = random.choice(image_for_buttons_copy)
            picture1 = random.choice(image_for_buttons_copy)
    del alphabet[image_letter]


snd_dir = path.join(path.dirname(__file__))
task = pygame.mixer.Sound(path.join(path.dirname(__file__), 'task.wav'))
correct_answer = pygame.mixer.Sound(path.join(path.dirname(__file__), '++.wav'))
wrong_answer = pygame.mixer.Sound(path.join(path.dirname(__file__), '-.wav'))
new()


class Letter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 200))
        self.image = work_image(image_letter)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 250)

    def update(self):
        global image_letter
        self.image = work_image(image_letter)


class Tile(pygame.sprite.Sprite):
    def __init__(self, picture, center, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 200))
        self.picture = picture
        self.image = work_image(self.picture)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.width = 400
        self.height = 400
        self.true_answer = true_answer
        self.name = name

    def check_answer(self):
        global true_answer
        answers = {'t1': 1, 't2': 2, 't3': 3}
        if answers[self.name] == true_answer:
            return True

    def check(self):
        mouse = pygame.mouse.get_pos()
        if (self.rect.x < mouse[0] < self.rect.x + self.width) \
                and (self.rect.y < mouse[1] < self.rect.y + self.height):
            if self.check_answer():
                check_list.append(True)
            else:
                check_list.append(False)

    def update(self):
        self.picture = globals().get(f"picture{self.name[-1]}")
        self.image = work_image(self.picture)


expl_sounds = []
for snd in ['River Flows In You.mp3', 'Yiruma - Dream A Little Dream Of Me.mp3',
            'Yiruma - It`s Your Day.mp3', 'Yiruma - Memories In My Eyes.mp3',
            'Yiruma - Dream.mp3', 'Yiruma - Because I Love You.mp3']:
    expl_sounds.append(pygame.mixer.music.load(str(snd_dir) + "\\" + snd))
    pygame.mixer.music.set_volume(0.4)
score = 0
pygame.mixer.music.play(loops=-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Весёлая азбука")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
tile1 = Tile(picture1, (250, 650), 't1')
all_sprites.add(tile1)
tile2 = Tile(picture2, (750, 650), 't2')
all_sprites.add(tile2)
tile3 = Tile(picture3, (1250, 650), 't3')
all_sprites.add(tile3)
letter = Letter()
all_sprites.add(letter)
cursor_image = work_image('arrow.png')
cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()
pygame.mouse.set_visible(False)


running = True
number = 0
start_screen()
task.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cursor.rect.topleft = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_list = []
            tile1.check()
            tile2.check()
            tile3.check()
            if any(check_list):
                correct_answer.play()
                clock.tick(400)
                del image_for_buttons[0]
                if len(alphabet) != 0:
                    new()
                    task.play()
                    all_sprites.update()
            else:
                pass
                wrong_answer.play()
    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    if len(image_for_buttons) == 0:
        running = False
        end_screen()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()