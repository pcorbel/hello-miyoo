from pygame import DOUBLEBUF, Color, display, event, init, quit
from pygame.font import SysFont
from pygame.locals import *
from time import sleep

# declare vars
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
is_running = True

# init screen
init()
display.set_caption("Hello Miyoo")
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF)
fonts = SysFont(None, 48)


# declare functions
def pprint(text):
    screen.fill(BLACK)
    surface = fonts.render(text, False, WHITE, BLACK)
    rect = surface.get_rect()
    rect.centerx = screen.get_rect().centerx
    rect.centery = screen.get_rect().centery
    screen.blit(surface, rect)
    display.flip()


# run the app
pprint("Hello Miyoo")
while is_running:
    # print key pressed
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_UP:
                pprint("Up")

            elif e.key == K_DOWN:
                pprint("Down")

            elif e.key == K_LEFT:
                pprint("Left")

            elif e.key == K_RIGHT:
                pprint("Right")

            elif e.key == K_SPACE:
                pprint("A")

            elif e.key == K_LCTRL:
                pprint("B")

            elif e.key == K_LSHIFT:
                pprint("X")

            elif e.key == K_LALT:
                pprint("Y")

            elif e.key == K_e:
                pprint("L1")

            elif e.key == K_TAB:
                pprint("L2")

            elif e.key == K_t:
                pprint("R1")

            elif e.key == K_BACKSPACE:
                pprint("R2")

            elif e.key == K_RETURN:
                pprint("Start")

            elif e.key == K_RCTRL:
                pprint("Select")

            elif e.key == K_ESCAPE:
                pprint("Menu")
                sleep(1)
                is_running = False

        elif e.type == QUIT:
            is_running = False

# quit the app
pprint("Bye Miyoo")
sleep(1)
quit()
