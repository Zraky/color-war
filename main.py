import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
clock = pygame.time.Clock()
run = True
FPS = 60
case = 5
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_turn = 2
play_move = 0

pygame.display.set_caption("Color War")
#icon = pygame.image.load('color_war.png')
#pygame.display.set_icon(icon)

def reset():
    map_game = []
    global case
    for i in range(case):
        map_game.append([])
        for y in range(case):
            map_game[i].append([0, 0])
    return map_game

Map_game = reset()

def click(x, y, player_turn):
    global play_move
    if Map_game[x][y][0] == player_turn:
        Map_game[x][y][0] = player_turn
        Map_game[x][y][1] += 1
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1
        play_move += 1
    if play_move < 2:
        if Map_game[x][y][0] == 0:
            Map_game[x][y][0] = player_turn
            Map_game[x][y][1] = 3
            if player_turn == 1:
                player_turn = 2
            else:
                player_turn = 1
            play_move += 1
    return Map_game, player_turn

cd = 0

def draw(map):
    global case, player_turn, cd, dt
    cd += dt
    width = height = SCREEN_HEIGHT / case
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_HEIGHT, SCREEN_WIDTH))
    for y in range(len(map)):
        for x in range(len(map[0])):
            if pygame.draw.rect(screen, (255, 255, 255), (y * width, x * height, width, height), 100000, 20).collidepoint(pygame.mouse.get_pos()):
                if player_turn == 1:
                    pygame.draw.rect(screen, (0, 0, 255), (y * width, x * height, width, height), 100000, 20)
                    if pygame.mouse.get_pressed()[0] and cd >= 0.1:
                        map, player_turn = click(y, x, player_turn)
                        cd = 0
                else:
                    pygame.draw.rect(screen, (255, 0, 0), (y * width, x * height, width, height), 100000, 20)
                    if pygame.mouse.get_pressed()[0] and cd >= 0.1:
                        map ,player_turn = click(y, x, player_turn)
                        cd = 0


            else:
                pygame.draw.rect(screen, (255, 255, 255), (y * width, x * height, width, height), 100000, 20)

            if map[y][x][0] == 0:
                pygame.draw.circle(screen, (200, 200, 200), (y * width + width / 2, x * height + height / 2), 45)
            elif map[y][x][0] == 1:
                pygame.draw.circle(screen, (0, 0, 255), (y * width + width / 2, x * height + height / 2), 45)
                if map[y][x][1] == 1:
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2, x * height + height / 2), 10)
                elif map[y][x][1] == 2:
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 + 15, x * height + height / 2), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 - 15, x * height + height / 2), 10)
                elif map[y][x][1] == 3:
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 + 15, x * height + height / 2 - 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 - 15, x * height + height / 2 - 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2, x * height + height / 2 + 15), 10)
                elif map[y][x][1] == 4:
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 + 15, x * height + height / 2 - 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 - 15, x * height + height / 2 - 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 + 15, x * height + height / 2 + 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 - 15, x * height + height / 2 + 15),10)

            elif map[y][x][0] == 2:
                pygame.draw.circle(screen, (255, 0, 0), (y * width + width / 2, x * height + height / 2), 45)
                if map[y][x][1] == 1:
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2, x * height + height / 2), 10)
                elif map[y][x][1] == 2:
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 + 15, x * height + height / 2), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 - 15, x * height + height / 2), 10)
                elif map[y][x][1] == 3:
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 + 15, x * height + height / 2 - 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 - 15, x * height + height / 2 - 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2, x * height + height / 2 + 15), 10)
                elif map[y][x][1] == 4:
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 + 15, x * height + height / 2 - 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 - 15, x * height + height / 2 - 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 + 15, x * height + height / 2 + 15), 10)
                    pygame.draw.circle(screen, (255, 255, 255), (y * width + width / 2 - 15, x * height + height / 2 + 15),10)
            pygame.draw.rect(screen, (0, 0, 0), (y * width, x * height, width, height), 5, 20)

def explosion(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x][1] >= 4:
                if y + 1 < len(map):
                    map[y + 1][x][0] = map[y][x][0]
                    map[y + 1][x][1] += 1
                if y - 1 >= 0:
                    map[y - 1][x][0] = map[y][x][0]
                    map[y - 1][x][1] += 1
                if x + 1 < len(map[y]):
                    map[y][x + 1][0] = map[y][x][0]
                    map[y][x + 1][1] += 1
                if x - 1 >= 0:
                    map[y][x - 1][0] = map[y][x][0]
                    map[y][x - 1][1] += 1
                map[y][x][1] -= 4
            if map[y][x][1] == 0:
                map[y][x][0] = 0


class Menu():
    def __init__(self, color_1=(200, 200, 200), color_2=(255, 255, 255)):
        self.screen_size_w = round(SCREEN_WIDTH * 1 / 4)
        self.screen_size_h = SCREEN_HEIGHT
        self.color = color_1
        self.police = pygame.font.SysFont(str(None), 30)
        self.police_win = pygame.font.SysFont(str(None), 160)

        self.game = 1
        self.blue_win = 0
        self.red_win = 0
        self.game_point = 1

        self.button_re_start = pygame.Rect(self.screen_size_w * 3.1, self.screen_size_h * 10 / 15, self.screen_size_w * 0.8, self.screen_size_h * 1/10)
        self.button_re_start_color = color_1
        self.button_quit = pygame.Rect(self.screen_size_w * 3.1, self.screen_size_h * 10 / 12, self.screen_size_w * 0.8, self.screen_size_h * 1 / 10)
        self.button_quit_color = color_1
        self.button_color_1 = color_1
        self.button_color_2 = color_2
        self.police_button = pygame.font.SysFont(str(None), 50)

        self.continue_run = True

    def button_click(self, mouse_1, mouse_pos):
        if self.button_re_start.collidepoint(mouse_pos):
            self.button_re_start_color = self.button_color_2
            if mouse_1:
                global Map_game, play_move
                Map_game = reset()
                play_move = 0
                self.game += 1
                self.game_point = 1
        else:
            self.button_re_start_color = self.button_color_1

        if self.button_quit.collidepoint(mouse_pos):
            self.button_quit_color = self.button_color_2
            if mouse_1:
                global run
                run = False
        else:
            self.button_quit_color = self.button_color_1

    def check_win(self, map):
        red_win = True
        blue_win = True
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x][0] == 1:
                    red_win = False
                if map[y][x][0] == 2:
                    blue_win = False
        if play_move > 2:
            if red_win == True:
                if self.game_point == 1:
                    self.red_win += 1
                    self.game_point -=1
                pygame.draw.rect(screen, (255, 150, 150), (0, SCREEN_HEIGHT / 4, SCREEN_HEIGHT, SCREEN_WIDTH / 3))
                screen.blit((self.police_win.render("RED WIN", 1, (0, 0, 0))), (0, SCREEN_HEIGHT / 2.5))


            if blue_win == True:
                if self.game_point == 1:
                    self.blue_win += 1
                    self.game_point -=1
                pygame.draw.rect(screen, (150, 150, 255), (0, SCREEN_HEIGHT / 4, SCREEN_HEIGHT, SCREEN_WIDTH / 3))
                screen.blit((self.police_win.render("BLUE WIN", 1, (0, 0, 0))), (0, SCREEN_HEIGHT / 3))

    def draw(self, turn):
        dt = clock.tick(60) / 1000

        pygame.draw.rect(screen, (self.color), (self.screen_size_w * 3, 0, SCREEN_WIDTH, self.screen_size_h), 5, 0)

        screen.blit((self.police.render(f"Game n°{self.game}", 1, self.color)),(self.screen_size_w * 3.1, self.screen_size_h * 1/98))
        screen.blit((self.police.render(f"Blue win : {self.blue_win}", 1, (0, 0, 255))), (self.screen_size_w * 3.1, self.screen_size_h * 1/20))
        screen.blit((self.police.render(f"Red win : {self.red_win}", 1, (255, 0, 0))), (self.screen_size_w * 3.1, self.screen_size_h * 1 / 12))
        screen.blit((self.police.render(f"Time : {int(round(pygame.time.get_ticks() / 1000, 0))}s", 1, self.color)), (self.screen_size_w * 3.1, self.screen_size_h * 1 / 8))
        screen.blit((self.police.render(f"FPS : {round(1 / dt, 2)}", 1, self.color)), (self.screen_size_w * 3.1, self.screen_size_h * 1 / 6))
        if turn == 1:
            screen.blit((self.police.render(f"Blue turn", 1, (0, 0, 255))),
                        (self.screen_size_w * 3.1, self.screen_size_h * 1 / 5))
        else:
            screen.blit((self.police.render(f"Red turn", 1, (255, 0, 0))),
                        (self.screen_size_w * 3.1, self.screen_size_h * 1 / 5))

        pygame.draw.rect(screen, self.button_re_start_color, self.button_re_start, 10, 4)
        screen.blit((self.police_button.render("restart", 1, self.button_re_start_color)),(self.button_re_start.x * 1.045, self.button_re_start.y * 1.028))

        pygame.draw.rect(screen, self.button_quit_color, self.button_quit, 10, 4)
        screen.blit((self.police_button.render("exit", 1, self.button_quit_color)), (self.button_quit.x * 1.08, self.button_quit.y * 1.025))

menu = Menu()

while run:
    screen.fill("#000000")
    dt = clock.tick(60) / 1000
    mouse_pos = pygame.mouse.get_pos()
    mouse_clic_0 = pygame.mouse.get_pressed()[0]

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    menu.button_click(mouse_clic_0, mouse_pos)
    menu.draw(player_turn)
    explosion(Map_game)
    draw(Map_game)
    menu.check_win(Map_game)


    pygame.display.flip()
    clock.tick(FPS)
    dt = clock.tick(60) / 1000
pygame.quit()
sys.exit()