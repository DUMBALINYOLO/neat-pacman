import sys
import pygame
from settings import *

pygame.init()
vec = pygame.math.Vector2


class App:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'


    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False


            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


####################HELPER FUNCTIONS ################################
    def draw_text(
                self,
                screen,
                size,
                color,
                font_name,
                text,
                position,
                centered=False
            ):

        font = pygame.font.SysFont(font_name, START_TEXT_SIZE)
        words = font.render(text, False, color)
        text_size = words.get_size()
        if centered:
            position[0] = position[0] - text_size[0]//2
            position[1] = position[1] - text_size[1]//2
        screen.blit(words, position)



# #################INTRO FUNCTIONS ###############################
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'



    def start_update(self):
        pass


    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text(
                screen = self.screen,
                size = START_TEXT_SIZE,
                color = (170, 132, 52),
                font_name = START_FONT,
                text = 'PUSH SPACE BUTTON',
                position = [200, HEIGHT //2],
                centered=True
            )

        self.draw_text(
                screen = self.screen,
                size = START_TEXT_SIZE,
                color = (33, 137, 120),
                font_name = START_FONT,
                text = '1 PLAYER ONLY',
                position = [200, HEIGHT //2 +50],
                centered=True
            )
        self.draw_text(
                screen = self.screen,
                size = START_TEXT_SIZE,
                color = (222, 222, 222),
                font_name = START_FONT,
                text = 'HIGH SCORE',
                position = [4, 0],
                centered=False
            )
        pygame.display.update()



# #################PLAYING FUNCTIONS ###############################
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False



    def playing_update(self):
        pass


    def playing_draw(self):
        self.screen.fill(RED)
        pygame.display.update()
