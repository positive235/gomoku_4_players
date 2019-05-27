import pygame

from gomoku_4_players import Gomoku
from gomoku_4_players.palette_wh import COLOR_BLACK, COLOR_RED, COLOR_GRAY, \
    COLOR_GREEN, COLOR_WHITE, COLOR_BLUE, COLOR_PURPLE, W_H, P_WID, P1_HT, \
    P2_HT, P3_HT, P4_HT, DRAW_HT


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    stone = {}
    stone["white"], stone["black"], stone["blue"] = [], [], []
    stone["purple"] = []
    player1_score, player2_score, player3_score, player4_score = 0, 0, 0, 0
    game = Gomoku()
    game.draw_main()
    game.draw_score(player1_score, player2_score, player3_score, player4_score)

    play_order = None

    while True:
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN:

            x_stone, y_stone = game.play_get_pos()

            # New game.
            if (125 + 45 * 16) > x_stone > 45 * 16 and 90 > y_stone > 45:
                stone["white"], stone["black"], stone["blue"] = [], [], []
                stone["purple"] = []
                player1_score, player2_score, player3_score = 0, 0, 0
                player4_score = 0
                game = Gomoku()
                game.draw_main()
                game.draw_score(player1_score, player2_score, player3_score,
                                player4_score)
                game.text_draw("GAME START", W_H // 2, 30, COLOR_GREEN, 35)
                play_order = "K"

            # Next game.
            if (125 + 45 * 16) > x_stone > 45 * 16 and 160 > y_stone > 115:
                stone["white"], stone["black"], stone["blue"] = [], [], []
                stone["purple"] = []
                game = Gomoku()
                game.draw_main()
                game.draw_score(player1_score, player2_score, player3_score,
                                player4_score)
                game.text_draw("NEXT GAME START", W_H // 2, 30, COLOR_GREEN, 35)
                play_order = "K"

            # Draw a white stone (Player 1).
            if play_order is None:
                pass
            elif play_order == "W":
                game.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_RED, 20)
                game.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_BLACK, 20)
                game.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_BLUE, 20)
                game.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_PURPLE, 20)
                if 45 <= x_stone <= W_H and 45 <= y_stone <= W_H:
                    x_stone, y_stone = game.play_draw_stone_pos()
                    stone, play_order = game.play_draw_stone(
                        stone, play_order, "white", COLOR_WHITE,
                        x_stone, y_stone)
                    game.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_GRAY, 20)
                    game.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_BLACK, 20)
                    game.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_BLUE, 20)
                    game.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_RED, 20)
                    player1_score, play_order = game.score(
                        stone, "white", player1_score, play_order)
                    num_stone = len(stone["white"]) + len(stone["black"]) + len(
                        stone["blue"]) + len(stone["purple"])
                    if num_stone == 225:
                        game.text_draw("DRAW", P_WID, DRAW_HT, (200, 0, 0), 45)
                        play_order = None

            # Draw a black stone (Player 2).
            elif play_order == "K":
                game.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_GRAY, 20)
                game.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_RED, 20)
                game.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_BLUE, 20)
                game.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_PURPLE, 20)
                if 45 <= x_stone <= W_H and 45 <= y_stone <= W_H:
                    x_stone, y_stone = game.play_draw_stone_pos()
                    stone, play_order = game.play_draw_stone(
                        stone, play_order, "black", COLOR_BLACK, x_stone, y_stone)
                    game.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_GRAY, 20)
                    game.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_BLACK, 20)
                    game.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_RED, 20)
                    game.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_PURPLE, 20)
                    player2_score, play_order = game.score(
                        stone, "black", player2_score, play_order)
                    num_stone = len(stone["white"]) + len(stone["black"]) + len(
                        stone["blue"]) + len(stone["purple"])
                    if num_stone == 225:
                        game.text_draw("DRAW", P_WID, DRAW_HT, (200, 0, 0), 45)
                        play_order = None

            # Draw a blue stone (Player 3).
            elif play_order == "B":
                game.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_GRAY, 20)
                game.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_BLACK, 20)
                game.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_RED, 20)
                game.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_PURPLE, 20)
                if 45 <= x_stone <= W_H and 45 <= y_stone <= W_H:
                    x_stone, y_stone = game.play_draw_stone_pos()
                    stone, play_order = game.play_draw_stone(
                        stone, play_order, "blue", COLOR_BLUE, x_stone, y_stone)
                    game.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_RED, 20)
                    game.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_BLACK, 20)
                    game.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_BLUE, 20)
                    game.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_PURPLE, 20)
                    player3_score, play_order = game.score(
                        stone, "blue", player3_score, play_order)
                    num_stone = len(stone["white"]) + len(stone["black"]) + len(
                        stone["blue"]) + len(stone["purple"])
                    if num_stone == 225:
                        game.text_draw("DRAW", P_WID, DRAW_HT, (200, 0, 0), 45)
                        play_order = None

            # Draw a blue stone (Player 4).
            elif play_order == "P":
                game.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_GRAY, 20)
                game.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_BLACK, 20)
                game.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_BLUE, 20)
                game.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_RED, 20)
                if 45 <= x_stone <= W_H and 45 <= y_stone <= W_H:
                    x_stone, y_stone = game.play_draw_stone_pos()
                    stone, play_order = game.play_draw_stone(
                        stone, play_order, "purple", COLOR_PURPLE, x_stone, y_stone)
                    game.text_draw("PLAYER 1", P_WID, P1_HT, COLOR_GRAY, 20)
                    game.text_draw("PLAYER 2", P_WID, P2_HT, COLOR_RED, 20)
                    game.text_draw("PLAYER 3", P_WID, P3_HT, COLOR_BLUE, 20)
                    game.text_draw("PLAYER 4", P_WID, P4_HT, COLOR_PURPLE, 20)
                    player4_score, play_order = game.score(
                        stone, "purple", player4_score, play_order)
                    num_stone = len(stone["white"]) + len(stone["black"]) + len(
                        stone["blue"]) + len(stone["purple"])
                    if num_stone == 225:
                        game.text_draw("DRAW", P_WID, DRAW_HT, (200, 0, 0), 45)
                        play_order = None

        game.interactive_button()
        pygame.display.update()
