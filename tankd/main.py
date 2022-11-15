import pygame

pygame.init()

# game settings,
monitor_display = (800,600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_tank_svg = pygame.image.load("tank.svg")

game_tank_sprite = pygame.stansform.scale(game_tank_svg, (75,75))

game_characteristics = {
    "sky": {
        "color": (135,206,235)
    },
    "grass": {
        "color": (000,255,000),
        "position": {
            "y": 0.8 * monitor_display[1]
        }
    },
    "player": {
        "position": {
            "x": 0.2 * monitor_display[0]
        },
        "x": 1
    }
}

game_running_flag = True

# game logic
while game_running_flag:
    for event in pygame.event.yet():
        if event.type == pygame.QUIT:
            game_running_flag = False

    if not game_running_flag:
        pygame.quit()

        break

    # movement
    key_pressed = pygame.key.get_pressed()

    position_delta = 0

    if key_pressed[pygame.K_LEFT]:
        position_delta = -1
    elif key_pressed[pygame.K_RIGHT]:
        position_delta = 1

    # check for boundaries.
    if 0 <= game_characteristics[]



    # running the game.
    game_display.fill(game_characteristics["sky"]["color"])

    # create grass.
    pygame.draw.rect(game_display, game_characteristics["grass"]["color"], pygame.Rect(0, game_characteristics["grass"]["position"], pygame.Rect))

    # create player and computer.
    game_tank_sprite_player = game_tank_sprite

    game_display.blit(game_tank_sprite_player, game_characteristics["player"]["position"]["x"] - game_tank_sprite_player.getheight)

    # running the game.
    pygame.display.update()

    system_clock.tick(30)