
TITLE = "My Game"

WIDTH = 1024
HEIGHT = 768


player = Actor("dragon_awake", (320, 240))


def draw():
    screen.fill("white")
    player.draw()


def update():
    if keyboard.left:
        player.x -= 4

    if keyboard.right:
        player.x += 4

    if keyboard.up:
        player.y -= 4

    if keyboard.down:
        player.y += 4
