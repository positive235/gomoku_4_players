import pygame

from gomoku_4_players.palette_wh import COLOR_BLACK, COLOR_WHITE, COLOR_BLUE, \
    COLOR_RED, COLOR_GRAY, COLOR_PURPLE, COLOR_BOARD, COLOR_BUTTON, \
    COLOR_AC_BUTTON, W_H, P_WID, C_WID, P1_HT, P2_HT, P3_HT, P4_HT, P1_SC_HT, \
    P2_SC_HT, P3_SC_HT, P4_SC_HT, P1_WIN_HT, P2_WIN_HT, P3_WIN_HT, P4_WIN_HT


class Gomoku:
    def __init__(self):
        self.title = "GOMOKU for 4 players (3-in-a-row)"
        self.screen = pygame.display.set_mode((900, W_H + 45))
        pygame.display.set_caption(self.title)
        self.screen.fill(COLOR_BOARD)

    def draw_main(self, x=45*16, y=45, w=125, h=45,
                  button_color=COLOR_BUTTON, ac_button_color=COLOR_AC_BUTTON):

        # Gomoku board.
        for i in range(1, 16):
            pygame.draw.line(self.screen, COLOR_BLACK,
                             [45 * i, 45], [45 * i, W_H], 2)
            pygame.draw.line(self.screen, COLOR_BLACK,
                             [45, 45 * i], [W_H, 45 * i], 2)
        pygame.draw.circle(self.screen, COLOR_BLACK, [45 * 8, 45 * 8], 8)

    def draw_score(self, player1_score, player2_score, player3_score,
                   player4_score):
        self.player1_score, self.player2_score = player1_score, player2_score
        self.player3_score, self.player4_score = player3_score, player4_score
        # Score.
        self.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_GRAY, 20)
        pygame.draw.circle(self.screen, COLOR_WHITE, (C_WID, P1_HT), 45//5)
        self.text_draw(str(self.player1_score), P_WID, P1_SC_HT, COLOR_GRAY, 35)
        self.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_BLACK, 20)
        pygame.draw.circle(self.screen, COLOR_BLACK, (C_WID, P2_HT), 45 // 5)
        self.text_draw(str(self.player2_score), P_WID, P2_SC_HT, COLOR_BLACK, 35)
        self.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_BLUE, 20)
        pygame.draw.circle(self.screen, COLOR_BLUE, (C_WID, P3_HT), 45 // 5)
        self.text_draw(str(self.player3_score), P_WID, P3_SC_HT, COLOR_BLUE, 35)
        self.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_PURPLE, 20)
        pygame.draw.circle(self.screen, COLOR_PURPLE, (C_WID, P4_HT), 45//5)
        self.text_draw(str(self.player4_score), P_WID, P4_SC_HT, COLOR_PURPLE, 35)

    def interactive_button(self, x=45*16, y=45, w=125, h=45,
                           button_color=COLOR_BUTTON,
                           ac_button_color=COLOR_AC_BUTTON):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.button_color = button_color
        self.ac_button_color = ac_button_color

        # Draw buttons.
        pygame.draw.rect(self.screen, self.button_color, (self.x, self.y,
                                                          self.w, self.h))
        pygame.draw.rect(self.screen, self.button_color, (self.x, self.y + 70,
                                                          self.w, self.h))
        pygame.draw.rect(self.screen, self.button_color, (self.x, W_H - 60,
                                                          self.w, self.h))
        # Draw text on buttons.
        self.text_draw("NEW GAME", self.x + 59, self.y + 25, (200, 0, 0), 20)
        self.text_draw("NEXT GAME", self.x + 62, self.y + 95, (0, 0, 180), 20)
        self.text_draw("QUIT", self.x + 56, W_H - 35, (200, 0, 200), 20)
        # To make interactive buttons.
        mouse = pygame.mouse.get_pos()
        # New game.
        if self.w + self.x > mouse[0] > self.x and \
                self.y + self.h > mouse[1] > self.y:
            pygame.draw.rect(self.screen, self.ac_button_color,
                             (self.x, self.y, self.w, self.h))
            self.text_draw("START", self.x + 59, self.y + 25, COLOR_RED, 20)

        # Next game.
        if self.w + self.x > mouse[0] > self.x and \
                self.y + 70 + self.h > mouse[1] > self.y + 70:
            pygame.draw.rect(self.screen, self.ac_button_color,
                             (self.x, self.y + 70, self.w, self.h))
            self.text_draw("Next game", self.x + 62, self.y + 95, (0, 0, 225), 20)

        # Quit.
        if self.w + self.x > mouse[0] > self.x and \
                W_H - 60 + self.h > mouse[1] > W_H - 60:
            pygame.draw.rect(self.screen, self.ac_button_color,
                             (self.x, W_H - 60, self.w, self.h))
            self.text_draw("Quit", self.x + 56, W_H - 35, (225, 0, 225), 20)
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.quit()
                quit()

    def text_draw(self, text, x_pos, y_pos, font_color, font_size):
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        ff = pygame.font.Font(pygame.font.get_default_font(), self.font_size)
        TextSurf, TextRect = self.text_objects(self.text, ff, self.font_color)
        TextRect.center = (x_pos, y_pos)
        self.screen.blit(TextSurf, TextRect)

    def text_objects(self, text, font, font_color):
        textSurface = font.render(text, True, font_color)
        return textSurface, textSurface.get_rect()

    def play_get_pos(self):
        self.x_stone, self.y_stone = pygame.mouse.get_pos()
        return self.x_stone, self.y_stone

    def play_draw_stone_pos(self):
        if self.x_stone % 45 > 23:
            self.x_stone = (self.x_stone - self.x_stone % 45) + 45
        else:
            self.x_stone -= self.x_stone % 45

        if self.y_stone % 45 > 23:
            self.y_stone = (self.y_stone - self.y_stone % 45) + 45
        else:
            self.y_stone -= self.y_stone % 45

        return self.x_stone, self.y_stone

    def play_draw_stone(self, stone, play_order, color_name, stone_color, x_stone, y_stone):
        self.stone, self.play_order, self.color_name = stone, play_order, color_name
        self.stone_color, self.x_stone, self.y_stone = stone_color, x_stone, y_stone

        if (self.x_stone, self.y_stone) in self.stone["white"]:
            pass
        elif (self.x_stone, self.y_stone) in self.stone["black"]:
            pass
        elif (self.x_stone, self.y_stone) in self.stone["blue"]:
            pass
        elif (self.x_stone, self.y_stone) in self.stone["purple"]:
            pass
        else:
            pygame.draw.circle(self.screen, self.stone_color,
                               (self.x_stone, self.y_stone), 45 // 2)
            self.stone[self.color_name].append((self.x_stone, self.y_stone))
            if self.play_order == "K": self.play_order = "B"
            elif self.play_order == "B": self.play_order = "W"
            elif self.play_order == "W": self.play_order = "P"
            elif self.play_order == "P": self.play_order = "K"

        return self.stone, self.play_order

    def score(self, stone, color_name, player_score, play_order):
        self.stone, self.color_name, self.player_score = stone, color_name, player_score
        self.play_order = play_order
        self.result = None
        if len(self.stone[self.color_name]) >= 3:

            stone_sort = sorted(self.stone[self.color_name])

            for x, y in stone_sort:
                cnt = 0
                for i in range(1, 3):
                    if (x, y + 45 * i) in stone_sort:
                        cnt += 1
                        if cnt == 2:
                            self.player_score += 1
                            self.play_order = None
                            self.result = True
                            break

                    else: break

                cnt = 0
                for i in range(1, 3):
                    if (x + 45 * i, y) in stone_sort:
                        cnt += 1
                        if cnt == 2:
                            self.player_score += 1
                            self.play_order = None
                            self.result = True
                            break
                    else: break

                cnt = 0
                for i in range(1, 3):
                    if (x + 45 * i, y+45 * i) in stone_sort:
                        cnt += 1
                        if cnt == 2:
                            self.player_score += 1
                            self.play_order = None
                            self.result = True
                            break
                cnt = 0
                for i in range(1, 3):
                    if (x + 45 * i, y - 45 * i) in stone_sort:
                        cnt += 1
                        if cnt == 2:
                            self.player_score += 1
                            self.play_order = None
                            self.result = True
                            break

        if self.result:
            if self.color_name == "white":
                self.text_draw("WIN", P_WID, P1_WIN_HT, COLOR_GRAY, 35)

            elif self.color_name == "black":
                self.text_draw("WIN", P_WID, P2_WIN_HT, COLOR_BLACK, 35)

            elif self.color_name == "blue":
                self.text_draw("WIN", P_WID, P3_WIN_HT, COLOR_BLUE, 35)

            elif self.color_name == "purple":
                self.text_draw("WIN", P_WID, P4_WIN_HT, COLOR_PURPLE, 35)

        return self.player_score, self.play_order
