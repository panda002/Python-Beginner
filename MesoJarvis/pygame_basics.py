import pygame  # this is needed to access the PyGame framework

pygame.init()  # this initializes all the modules of PyGame
screen = pygame.display.set_mode((400, 300))  # this will display a window of the desired size
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if is_blue:
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.QUIT:  # When we click on the close button, this is fired
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    # Add this somewhere after the event pumping and before the display.flip()
    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
    clock.tick(60)
