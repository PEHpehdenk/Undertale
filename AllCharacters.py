import pygame
import random
from os import path


class Player(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load("TheHurt.png"), (50, 50))

    def __init__(self, group):
        super().__init__(group)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = 190
        self.rect.y = 640
        self.health = 50
        self.ButtonWasClicked = 0
        self.damage_sound = pygame.mixer.Sound(path.join('damage2.wav'))

    def update(self, moving=4, theStory=0, enemies=pygame.sprite.Group()):
        if theStory == 0:
            if moving == 0:
                if self.rect.x + 500 < 1000:
                    self.rect.x += 500
            if moving == 1:
                if self.rect.y + 70 < 720:
                    self.rect.y += 70
            if moving == 2:
                if self.rect.y - 70 == 640:
                    self.rect.y -= 70
            if moving == 3:
                if self.rect.x - 500 == 190:
                    self.rect.x -= 500
        if theStory == 1:
            if moving == 0:
                if self.rect.x + 1 < 804:
                    self.rect = self.rect.move(1, 0)
            if moving == 1:
                if self.rect.y + 1 < 854:
                    self.rect = self.rect.move(0, 1)
            if moving == 2:
                if self.rect.y - 1 > 392:
                    self.rect = self.rect.move(0, -1)
            if moving == 3:
                if self.rect.x - 1 > 144:
                    self.rect = self.rect.move(-1, 0)
            if pygame.sprite.spritecollideany(self, enemies):
                self.health -= 0.2
                self.damage_sound.play()
                if self.health < 0:
                    self.health = 0
        if theStory == 2:
            if pygame.sprite.spritecollideany(self, enemies):
                self.ButtonWasClicked = 1


class Bones(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load("ItogBone.png"), (100, 300))

    def __init__(self, group):
        super().__init__(group)
        self.image = Bones.image
        self.rect = self.image.get_rect()
        self.rect.x = 790
        self.rect.y = 400
        self.pozition = 1
        self.numOfBones = 0

    def update(self, *args):
        if self.rect.x > 120:
            self.rect = self.rect.move(-2, 0)
        else:
            self.rect.x = 790
            if self.pozition % 2 == 0:
                self.rect.y = 400
            else:
                self.rect.y = 600
            self.pozition += 1
            self.numOfBones += 1


class LongBones(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load("longBone.png"), (400, 100))

    def __init__(self, group):
        super().__init__(group)
        self.image = LongBones.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 400
        self.pozition = 1
        self.numOfBones = 6

    def update(self, *args):
        if self.rect.y < 800:
            self.rect = self.rect.move(0, 2)
        else:
            self.rect.y = 400
            if self.pozition % 2 == 0:
                self.rect.x = 100
            else:
                self.rect.x = 500
            self.pozition += 1
            self.numOfBones += 1


class Determination(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load("TryAgainButton.png"), (200, 200))

    def __init__(self, group):
        super().__init__(group)
        self.image = Determination.image
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

