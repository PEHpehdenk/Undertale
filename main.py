import pygame
import AllCharacters
from os import path

pygame.init()

sc = pygame.display.set_mode((1000, 1000))

# здесь будут рисоваться фигуры
allSprites = pygame.sprite.Group()
sans = pygame.image.load('sansik.png')
PlaceOfSans = sans.get_rect(bottomright=(600, 500))
sc.blit(sans, PlaceOfSans)
TheMenu = pygame.Rect((150, 620, 700, 175))
TheStory = 0
pygame.display.update()
ThePlayer = AllCharacters.Player(allSprites)
HealthBar = pygame.Rect((650, 820, 4 * ThePlayer.health, 30))
pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
pygame.draw.rect(sc, (0, 255, 0), HealthBar)
pygame.draw.rect(sc, (255, 255, 255), (650, 820, 200, 30), 3)
size = pygame.font.SysFont('serif', 20)
textOfHp = size.render(str(ThePlayer.health) + '/50', 0, (0, 180, 0))
sizeOfNameChara = pygame.font.SysFont('serif', 30)
textOfNameChara = sizeOfNameChara.render('Chara. level 19', 0, (255, 0, 0))
sizeOfNameFrisk = pygame.font.SysFont('serif', 30)
textOfNameFrisk = sizeOfNameFrisk.render('Frisk. level 19', 0, (0, 0, 255))
sizeSansWords = pygame.font.SysFont('serif', 30)
textOfSans = sizeSansWords.render('Are you ready to start?', 0, (255, 255, 255))
sizeofAnswerNumber1 = pygame.font.SysFont('serif', 40)
textOfAnswer1 = sizeofAnswerNumber1.render('YES', 0, (255, 255, 255))
sc.blit(textOfHp, (800, 860))
sc.blit(textOfSans, (400, 100))
sc.blit(textOfAnswer1, (250, 655))
sc.blit(textOfAnswer1, (750, 655))
sc.blit(textOfAnswer1, (250, 725))
sc.blit(textOfAnswer1, (750, 725))
sc.blit(textOfNameChara, (150, 820))
atacks = pygame.sprite.Group()
atack = AllCharacters.Bones(atacks)
k = 0
CanIPlayMyMusic = 0
CanIPlayEndMusic = 0
CanIPlayPatifistMusic = 0
TheSizeOfEndText = pygame.font.SysFont('serif', 30)
TheEndText = TheSizeOfEndText.render('You lose. I' + "'" + 'm not suprised', 0, (0, 255, 0))
TheSizeOfPacifistText = pygame.font.SysFont('serif', 30)
ThePacifistText = TheSizeOfEndText.render('Wow. You' + "'" + 're nice child', 0, (0, 0, 255))
buttons = pygame.sprite.Group()
typeOFBones = 0
TheNumOFHils = 0
# allSprites.draw(sc)
# allSprites.update()
choice_sound = pygame.mixer.Sound(path.join('choice.wav'))
health_sound = pygame.mixer.Sound(path.join('health.wav'))
numOfWins = 10


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if TheStory == 0:
                    while TheMenu[3] != 501:
                        pygame.Surface.fill(sc, (0, 0, 0))
                        TheMenu[3] += 2
                        pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
                        pygame.display.update()
                        pygame.Surface.fill(sc, (0, 0, 0))
                    while TheMenu[1] != 400:
                        pygame.Surface.fill(sc, (0, 0, 0))
                        pygame.Surface.fill(sc, (0, 0, 0))
                        TheMenu[1] -= 2
                        pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
                        pygame.display.update()
                    pygame.display.update()
                    TheStory += 1
            if TheStory == 0:
                if i.key == pygame.K_DOWN:
                    ThePlayer.update(1)
                    pygame.Surface.fill(sc, (0, 0, 0))
                    pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
                    choice_sound.play()
                if i.key == pygame.K_RIGHT:
                    ThePlayer.update(0)
                    pygame.Surface.fill(sc, (0, 0, 0))
                    pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
                    choice_sound.play()
                if i.key == pygame.K_UP:
                    ThePlayer.update(2)
                    pygame.Surface.fill(sc, (0, 0, 0))
                    pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
                    choice_sound.play()
                if i.key == pygame.K_LEFT:
                    ThePlayer.update(3)
                    pygame.Surface.fill(sc, (0, 0, 0))
                    pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
                    choice_sound.play()
    if TheStory == 0:
        sc.blit(sans, PlaceOfSans)
        sc.blit(textOfNameChara, (150, 820))
        pygame.draw.rect(sc, (0, 255, 0), HealthBar)
        pygame.draw.rect(sc, (255, 255, 255), (650, 820, 200, 30), 3)
        text2 = size.render(str(ThePlayer.health) + '/30', 0, (0, 180, 0))
        sc.blit(textOfHp, (800, 860))
        allSprites.draw(sc)
        allSprites.update()
        if TheStory == 0:
            sizeofChosenAnswerNumber1 = pygame.font.SysFont('serif', 40)
            textOfChosenAnswer1 = sizeofChosenAnswerNumber1.render('YES', 0, (0, 255, 0))
            sc.blit(textOfSans, (400, 100))
            if ThePlayer.rect.x == 690:
                sc.blit(textOfAnswer1, (250, 725))
                sc.blit(textOfAnswer1, (250, 655))
                if ThePlayer.rect.y != 640:
                    sc.blit(textOfAnswer1, (750, 655))
                    sc.blit(textOfChosenAnswer1, (750, 725))
                else:
                    sc.blit(textOfAnswer1, (750, 725))
                    sc.blit(textOfChosenAnswer1, (750, 655))
            else:
                sc.blit(textOfAnswer1, (750, 725))
                sc.blit(textOfAnswer1, (750, 655))
                if ThePlayer.rect.y != 640:
                    sc.blit(textOfAnswer1, (250, 655))
                    sc.blit(textOfChosenAnswer1, (250, 725))
                else:
                    sc.blit(textOfAnswer1, (250, 725))
                    sc.blit(textOfChosenAnswer1, (250, 655))
        pygame.display.flip()
    if TheStory == 1:
        if CanIPlayMyMusic == 0:
            pygame.mixer.music.load('megalovania.mp3')
            pygame.mixer.music.play()
            CanIPlayMyMusic = 1
        allSprites.update(4, 1, atacks)
        atacks.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            ThePlayer.update(1, 1)
        if keys[pygame.K_RIGHT]:
            ThePlayer.update(0, 1)
        if keys[pygame.K_UP]:
            ThePlayer.update(2, 1)
        if keys[pygame.K_LEFT]:
            ThePlayer.update(3, 1)
        pygame.Surface.fill(sc, (0, 0, 0))
        pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
        PlaceOfSans = sans.get_rect(bottomright=(600, 350))
        sc.blit(sans, PlaceOfSans)
        sc.blit(textOfNameChara, (150, 920))
        pygame.draw.rect(sc, (255, 255, 255), (650, 920, 200, 30), 3)
        textOfHp2 = size.render(str(int(round(ThePlayer.health))) + '/50', 0, (0, 180, 0))
        sc.blit(textOfHp2, (800, 960))
        allSprites.draw(sc)
        atacks.draw(sc)
        HealthBar = pygame.Rect((650, 920, 4 * ThePlayer.health, 30))
        pygame.draw.rect(sc, (0, 255, 0), HealthBar)
        pygame.display.flip()
        if ThePlayer.health == 0:
            TheStory = 2
            atacks = pygame.sprite.Group()
            determinationButton = AllCharacters.Determination(buttons)
        if atack.numOfBones > 5:
            if typeOFBones != 0:
                if atack.numOfBones > 19:
                    if ThePlayer.health <= 45:
                        ThePlayer.health += 5
                    else:
                        ThePlayer.health = 50
                    health_sound.play()
                    atacks = pygame.sprite.Group()
                    atack = AllCharacters.Bones(atacks)
                    typeOFBones = 0
                    TheNumOFHils += 1
                if TheNumOFHils == numOfWins:
                    TheStory = 3
            else:
                atacks = pygame.sprite.Group()
                atack = AllCharacters.LongBones(atacks)
                typeOFBones = 1
    if TheStory == 2:
        allSprites.update(4, 1)
        if CanIPlayEndMusic == 0:
            pygame.mixer.music.load('TheEnd.mp3')
            pygame.mixer.music.play()
            CanIPlayEndMusic = 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            ThePlayer.update(1, 1)
        if keys[pygame.K_RIGHT]:
            ThePlayer.update(0, 1)
        if keys[pygame.K_UP]:
            ThePlayer.update(2, 1)
        if keys[pygame.K_LEFT]:
            ThePlayer.update(3, 1)
        if keys[pygame.K_SPACE]:
            allSprites.update(4, 2, buttons)
            if ThePlayer.ButtonWasClicked == 1:
                allSprites = pygame.sprite.Group()
                TheMenu = pygame.Rect((150, 620, 700, 175))
                TheStory = 0
                pygame.display.update()
                ThePlayer = AllCharacters.Player(allSprites)
                PlaceOfSans = sans.get_rect(bottomright=(600, 500))
                HealthBar = pygame.Rect((650, 820, 4 * ThePlayer.health, 30))
                pygame.draw.rect(sc, (0, 255, 0), HealthBar)
                pygame.draw.rect(sc, (255, 255, 255), (650, 820, 200, 30), 3)
                size = pygame.font.SysFont('serif', 20)
                textOfHp = size.render(str(ThePlayer.health) + '/50', 0, (0, 180, 0))
                sizeOfNameChara = pygame.font.SysFont('serif', 30)
                textOfNameChara = sizeOfNameChara.render('Chara. level 19', 0, (255, 0, 0))
                sizeSansWords = pygame.font.SysFont('serif', 30)
                textOfSans = sizeSansWords.render('Are you ready to start?', 0, (255, 255, 255))
                sizeofAnswerNumber1 = pygame.font.SysFont('serif', 40)
                textOfAnswer1 = sizeofAnswerNumber1.render('YES', 0, (255, 255, 255))
                sc.blit(textOfHp, (800, 860))
                sc.blit(sans, PlaceOfSans)
                sc.blit(textOfSans, (400, 100))
                sc.blit(textOfAnswer1, (250, 655))
                sc.blit(textOfAnswer1, (750, 655))
                sc.blit(textOfAnswer1, (250, 725))
                sc.blit(textOfAnswer1, (750, 725))
                sc.blit(textOfNameChara, (150, 820))
                atacks = pygame.sprite.Group()
                atack = AllCharacters.Bones(atacks)
                k = 0
                CanIPlayMyMusic = 0
                CanIPlayEndMusic = 0
                TheSizeOfEndText = pygame.font.SysFont('serif', 30)
                TheEndText = TheSizeOfEndText.render('You lose. I' + "'" + 'm not suprised', 0, (0, 255, 0))
                buttons = pygame.sprite.Group()
                pygame.Surface.fill(sc, (0, 0, 0))
                pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
                pygame.display.flip()
                typeOFBones = 0
                TheNumOFHils = 0
                if numOfWins > 5:
                    numOfWins -= 1
                continue
        pygame.Surface.fill(sc, (0, 0, 0))
        pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
        PlaceOfSans = sans.get_rect(bottomright=(600, 350))
        sc.blit(sans, PlaceOfSans)
        sc.blit(textOfNameChara, (150, 920))
        pygame.draw.rect(sc, (255, 255, 255), (650, 920, 200, 30), 3)
        textOfHp2 = size.render(str(ThePlayer.health) + '/50', 0, (0, 180, 0))
        sc.blit(textOfHp2, (800, 960))
        allSprites.draw(sc)
        HealthBar = pygame.Rect((650, 920, 4 * ThePlayer.health, 30))
        pygame.draw.rect(sc, (0, 255, 0), HealthBar)
        sc.blit(TheEndText, (600, 100))
        buttons.update()
        buttons.draw(sc)
        pygame.display.flip()
    if TheStory == 3:
        allSprites.update(4, 1)
        if CanIPlayPatifistMusic == 0:
            pygame.mixer.music.load('ThePacifist.mp3')
            pygame.mixer.music.play()
            CanIPlayPatifistMusic = 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            ThePlayer.update(1, 1)
            pygame.Surface.fill(sc, (0, 0, 0))
            pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
        if keys[pygame.K_RIGHT]:
            ThePlayer.update(0, 1)
            pygame.Surface.fill(sc, (0, 0, 0))
            pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
        if keys[pygame.K_UP]:
            ThePlayer.update(2, 1)
            pygame.Surface.fill(sc, (0, 0, 0))
            pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
        if keys[pygame.K_LEFT]:
            ThePlayer.update(3, 1)
            pygame.Surface.fill(sc, (0, 0, 0))
            pygame.draw.rect(sc, (255, 255, 255), TheMenu, 8)
        PlaceOfSans = sans.get_rect(bottomright=(600, 350))
        sc.blit(sans, PlaceOfSans)
        sc.blit(textOfNameFrisk, (150, 920))
        pygame.draw.rect(sc, (255, 255, 255), (650, 920, 200, 30), 3)
        textOfHp2 = size.render(str(ThePlayer.health) + '/50', 0, (0, 0, 255))
        sc.blit(textOfHp2, (800, 960))
        allSprites.draw(sc)
        HealthBar = pygame.Rect((650, 920, 4 * ThePlayer.health, 30))
        pygame.draw.rect(sc, (0, 255, 0), HealthBar)
        sc.blit(ThePacifistText, (600, 100))
        buttons.update()
        buttons.draw(sc)
        pygame.display.flip()
