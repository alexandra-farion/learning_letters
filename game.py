import random
from os import path

from future.moves import sys

from material import *
from work_with_img import *
from work_with_sounds import *

pygame.init()
pygame.mixer.init()


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


def terminate():
    pygame.quit()
    sys.exit()


def distribution_pictures():
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


distribution_pictures()

pygame.mixer.music.load(str(path.join(path.dirname(__file__))) + "\music\\" + 'Yiruma - Because I Love You.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

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
task = load_sound('task.wav')
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
                load_sound('++.wav').play()
                clock.tick(400)
                del image_for_buttons[0]
                if len(alphabet) != 0:
                    distribution_pictures()
                    task.play()
                    all_sprites.update()
            else:
                pass
                load_sound('-.wav').play()
    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    if len(image_for_buttons) == 0:
        running = False
        end_screen()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
