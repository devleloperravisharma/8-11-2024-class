import pgzrun
import random

WIDTH = 800
HEIGHT = 600
center_x = WIDTH//2
center_y = HEIGHT//2
center = (center_x, center_y)
final_level = 5
start_speed = 10
ITEMS = ["bag", "battery", "bottle", "chips"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global game_over, game_complete, current_level, items

    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("Game Over!!!!!", "that sucks to be you.")
    elif game_complete:
        display_message("Game Won!!!!!", "dang. heres a cookie 🍪🍪🍪🍪🍪🍪🍪")

    else:
        for item in items:
            item.draw()


def display_message(heading, subheading):
    screen.draw.text(heading, (center_x, (center_y-15)), font = ("Georgia", 50, "bold"), color = ("white"))
    screen.draw.text(subheading, (center_x, (center_y +15)), font = ("Georgia", 30), color = ("white"))


def update():
    pass







pgzrun.go()