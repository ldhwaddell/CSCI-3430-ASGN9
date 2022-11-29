import sys

import pygame

pygame.init()


def draw_window():
    # Colours
    white = (255, 255, 255)
    grey = (169, 169, 169)
    black = (0, 0, 0)

    # Font
    title_font = pygame.font.SysFont("Calibri", 35)
    title = title_font.render("A09 – Lucas Waddell", 1, white)
    quit_font = pygame.font.SysFont("Calibri", 25)
    quit = quit_font.render("Quit", 1, black)

    # Window settings and size
    width, height = 700, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hello World!")
    # Start main loop
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("[+] User has exited game")
                pygame.quit(), sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (
                    width // 2 - 50 <= mouse[0] <= width // 2 + 50
                    and height // 2 + 60 <= mouse[1] <= height // 2 + 110
                ):
                    run = False
                    print("[+] User has exited window")
                    pygame.quit(), sys.exit()

        # Get mouse pos
        mouse = pygame.mouse.get_pos()

        win.fill(black)
        # Draw the main text
        win.blit(
            title,
            (
                width // 2 - title.get_width() // 2,
                height // 2 - title.get_height() // 2,
            ),
        )

        # Draw a rectangle to contain the button, make it slightly darker if hovered over
        if (
            width // 2 - 50 <= mouse[0] <= width // 2 + 50
            and height // 2 + 60 <= mouse[1] <= height // 2 + 110
        ):
            pygame.draw.rect(win, grey, (width // 2 - 50, height // 2 + 60, 100, 50))
        else:
            pygame.draw.rect(win, white, (width // 2 - 50, height // 2 + 60, 100, 50))

        # Draw the words "quit" in the button
        win.blit(
            quit,
            (
                (width // 2 - 50) + (50 - quit.get_width() // 2),
                (height // 2 + 60) + (25 - quit.get_height() // 2),
            ),
        )

        # Refresh display
        pygame.display.update()


if __name__ == "__main__":
    draw_window()
