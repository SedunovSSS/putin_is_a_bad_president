import pygame
from random import randrange
from tkinter import messagebox
pygame.init()

width, height = 800, 640
widthBtn, heightBtn = 75, 30
lang = 'ru'
russian = ["Путин плохой президент?", "Да", "Нет", "Спасибо", "Спасибо за отзыв! Мы в вас не сомневались"]
english = ["Putin is a bad president?", "Yes", "No", "Thanks", "Thanks for the feedback! We didn't doubt you"]
if lang == 'ru':
    array = russian
else:
    array = english
fps = 60
sc = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
x, y = 200, 100
x1, y1 = 530, 100
text = pygame.font.SysFont("Arial", 20, bold=True).render(array[0], False, (255, 255, 255))
btnYes = pygame.Rect(x, y, widthBtn, heightBtn)
textYes = pygame.font.SysFont("Arial", 15, bold=True).render(array[1], False, (0, 0, 0))
btnNo = pygame.Rect(x1, y1, widthBtn, heightBtn)
textNo = pygame.font.SysFont("Arial", 15, bold=True).render(array[2], False, (0, 0, 0))
bySSS = pygame.font.SysFont("Arial", 15, bold=True).render("By SSS", False, (255, 255, 255))
pygame.display.set_caption(array[0])

while True:
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif x < mouse_pos_x < x+widthBtn and y < mouse_pos_y < y+heightBtn:
            x, y = randrange(0, width-widthBtn), randrange(0, height-heightBtn)
            btnYes = pygame.Rect(x, y, widthBtn, heightBtn)
            textYes = pygame.font.SysFont("Arial", 15, bold=True).render(array[1], False, (0, 0, 0))
        elif x1 < mouse_pos_x < x1+widthBtn and y1 < mouse_pos_y < y1+heightBtn:
            if i.type == pygame.MOUSEBUTTONDOWN:
                messagebox.showinfo(array[3], array[4])
                exit()

    sc.fill("black")
    sc.blit(text, (width//2-100, 50))
    pygame.draw.rect(sc, (255, 255, 255), btnYes)
    sc.blit(textYes, (x+30, y+5))
    pygame.draw.rect(sc, (255, 255, 255), btnNo)
    sc.blit(textNo, (x1+20, y1+5))
    sc.blit(bySSS, (2, height-20))
    pygame.display.flip()
    clock.tick(fps)
