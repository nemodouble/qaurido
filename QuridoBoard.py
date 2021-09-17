import random

MAX_BOARD_SIZE = 17
STARTING_PLAYER_POS_X = int((MAX_BOARD_SIZE+2)/2)
STARTING_WALLS_NUMBER = 10
BOARD_AIR = 0
BOARD_PLAYER1 = 1
BOARD_PLAYER2 = 2
BOARD_WALL = 3


def get_opponent_player(player_num):
    if player_num == BOARD_PLAYER1:
        return BOARD_PLAYER2
    elif player_num == BOARD_PLAYER2:
        return BOARD_PLAYER1
    else:
        return -1


class QuridoBoard:
    def __init__(self):
        self.board = [[BOARD_AIR] * (MAX_BOARD_SIZE + 2) for i in range(MAX_BOARD_SIZE + 2)]
        for i in range(MAX_BOARD_SIZE + 1):
            self.board[i][0] = BOARD_WALL
            self.board[i][MAX_BOARD_SIZE + 1] = BOARD_WALL
            self.board[0][i] = BOARD_WALL
            self.board[MAX_BOARD_SIZE + 1][i] = BOARD_WALL
        self.left_wall = [-1, STARTING_WALLS_NUMBER, STARTING_WALLS_NUMBER]
        self.board[STARTING_PLAYER_POS_X][1] = BOARD_PLAYER1
        self.board[STARTING_PLAYER_POS_X][MAX_BOARD_SIZE] = BOARD_PLAYER2
        self.player_pos = [[-1, -1], [STARTING_PLAYER_POS_X, 1], [STARTING_PLAYER_POS_X, MAX_BOARD_SIZE]]

    def move_player(self, player_num, direction):
        if self.can_move(player_num, self.player_pos[player_num][0], self.player_pos[player_num][1], direction) == "walk":
            if self.move_player_pos(player_num, direction):
                return True
        return False

    def jump_player(self, player_num, direction, jump_way):
        if self.can_move(player_num, self.player_pos[player_num][0], self.player_pos[player_num][1], direction) == jump_way:
            if self.jump_player_pos(player_num, direction, jump_way):
                return True
        return False

    def use_wall(self, player_num, str_x2, str_y2, dir):
        x2 = int(str_x2)
        y2 = int(str_y2)
        if dir == "vertical":
            x1 = x2
            x3 = x2
            y1 = y2 - 1
            y3 = y2 + 1
        elif dir == "horizon":
            x1 = x2 - 1
            x3 = x2 + 1
            y1 = y2
            y3 = y2
        else:
            return False
        if self.can_use_wall(player_num, x2, y2, dir):
            self.board[x1][y1] = BOARD_WALL
            self.board[x2][y2] = BOARD_WALL
            self.board[x3][y3] = BOARD_WALL
            self.left_wall[player_num] -= 1
            return True
        else:
            return False

    def get_possible_moves(self, player_num):
        possible_moves = ["error"]
        x = self.player_pos[player_num][0]
        y = self.player_pos[player_num][1]
        if self.can_move(player_num, x, y, "up") != "none":
            possible_moves.append(self.can_move(player_num, x, y, "up") + "/up")
        if self.can_move(player_num, x, y, "down") != "none":
            possible_moves.append(self.can_move(player_num, x, y, "down") + "/down")
        if self.can_move(player_num, x, y, "left") != "none":
            possible_moves.append(self.can_move(player_num, x, y, "left") + "/left")
        if self.can_move(player_num, x, y, "right") != "none":
            possible_moves.append(self.can_move(player_num, x, y, "right") + "/right")
        for i in range(8):
            for j in range(8):
                if self.can_use_wall(player_num, 2*i+2, 2*j+2, "horizon"):
                    possible_moves.append("use-wall/" + str(2*i+2) + "/" + str(2*j+2) + "/horizon")
                if self.can_use_wall(player_num, 2*i+2, 2*j+2, "vertical"):
                    possible_moves.append("use-wall/" + str(2*i+2) + "/" + str(2*j+2) + "/vertical")
        #random.shuffle(possible_moves)
        return possible_moves

    def unmake_move(self, nplayer, move):
        if move.find("walk") != -1:
            if move.split('/')[1] == "up":
                self.move_player(nplayer, "down")
            elif move.split('/')[1] == "down":
                self.move_player(nplayer, "up")
            elif move.split('/')[1] == "left":
                self.move_player(nplayer, "right")
            elif move.split('/')[1] == "right":
                self.move_player(nplayer, "left")
        elif move.find("jump") != -1:
            if move.split('/')[1] == "up":
                if move.split('/')[0] == "jump-forward":
                    self.jump_player(nplayer, "down", move.split('/')[0])
                elif move.split('/')[0] == "jump-right":
                    self.jump_player(nplayer, "left", "jump-left")
                elif move.split('/')[0] == "jump-left":
                    self.jump_player(nplayer, "right", "jump-right")
            elif move.split('/')[1] == "down":
                if move.split('/')[0] == "jump-forward":
                    self.jump_player(nplayer, "up", move.split('/')[0])
                elif move.split('/')[0] == "jump-right":
                    self.jump_player(nplayer, "right", "jump-left")
                elif move.split('/')[0] == "jump-left":
                    self.jump_player(nplayer, "left", "jump-right")
            elif move.split('/')[1] == "left":
                if move.split('/')[0] == "jump-forward":
                    self.jump_player(nplayer, "right", move.split('/')[0])
                elif move.split('/')[0] == "jump-right":
                    self.jump_player(nplayer, "up", "jump-left")
                elif move.split('/')[0] == "jump-left":
                    self.jump_player(nplayer, "down", "jump-right")
            elif move.split('/')[1] == "right":
                if move.split('/')[0] == "jump-forward":
                    self.jump_player(nplayer, "left", move.split('/')[0])
                elif move.split('/')[0] == "jump-right":
                    self.jump_player(nplayer, "down", "jump-left")
                elif move.split('/')[0] == "jump-left":
                    self.jump_player(nplayer, "up", "jump-right")
        elif move.find("wall") != -1:
            self.unuse_wall(nplayer, move.split('/')[1], move.split('/')[2], move.split('/')[3])

    def print_board(self):
        print("  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7")
        for i in range(MAX_BOARD_SIZE, 0, -1):
            print(str(i % 10) + " ", end='')
            for j in range(1, MAX_BOARD_SIZE+1, 1):
                if self.board[j][i] == BOARD_AIR:
                    if i % 2 == 0 and j % 2 == 0:
                        print(". ", end='')
                    elif i * j % 2 == 1:
                        print("□ ", end='')
                    else:
                        print("  ", end='')
                elif self.board[j][i] == BOARD_WALL:
                    print("■ ", end='')
                elif self.board[j][i] == BOARD_PLAYER1:
                    print("◎ ", end='')
                elif self.board[j][i] == BOARD_PLAYER2:
                    print("● ", end='')
            print()

        print("# 아래 칸수 : " + str(self.calculate_need_turn(1)) + " / 위 칸수 : " + str(self.calculate_need_turn(2)), end=' ')
        print("# 아래 벽수 : " + str(self.left_wall[1]) + " / 위 벽수 : " + str(self.left_wall[2]))
        print("# 아래 스코어보드")
        self.calculate_need_turn(1, True)
        print("# 위 스코어보드")
        self.calculate_need_turn(2, True)

    def can_move(self, player_num, x, y, direction):
        opp_player_num = get_opponent_player(player_num)
        if direction == "up":
            # if not overBoard
            if y + 2 <= MAX_BOARD_SIZE:
                # if wall
                if self.board[x][y + 1] == BOARD_WALL:
                    return "none"
                # if not wall
                elif self.board[x][y + 1] == BOARD_AIR:
                    # if not wall and nothing
                    if self.board[x][y + 2] == BOARD_AIR:
                        return "walk"
                    # if not wall but opponent player
                    elif self.board[x][y + 2] == opp_player_num:
                        # if not over board (jump)
                        if y + 3 <= MAX_BOARD_SIZE:
                            if self.board[x][y + 3] == BOARD_AIR:
                                return "jump-forward"
                        elif y + 2 <= MAX_BOARD_SIZE:
                            if self.board[x + 1][y + 2] == BOARD_AIR and self.board[x - 1][y + 2] == BOARD_AIR:
                                return "jump-both"
                            elif self.board[x + 1][y + 2] == opp_player_num:
                                return "jump-left"
                            elif self.board[x - 1][y + 2] == opp_player_num:
                                return "jump-right"
            return "none"
        elif direction == "down":
            if y - 2 >= 0:
                if self.board[x][y - 1] == BOARD_AIR:
                    if self.board[x][y - 2] == BOARD_AIR:
                        return "walk"
                    elif self.board[x][y - 2] == opp_player_num:
                        if y - 3 >= 0:
                            if self.board[x][y - 3] == BOARD_AIR:
                                return "jump-forward"
                            elif self.board[x + 1][y - 2] == BOARD_AIR and self.board[x - 1][y - 2] == BOARD_AIR:
                                return "jump-both"
                            elif self.board[x - 1][y - 2] == opp_player_num:
                                return "jump-left"
                            elif self.board[x + 1][y - 2] == opp_player_num:
                                return "jump-right"
            return "none"
        elif direction == "right":
            if x + 2 <= MAX_BOARD_SIZE:
                if self.board[x + 1][y] == BOARD_AIR:
                    if self.board[x + 2][y] == BOARD_AIR:
                        return "walk"
                    elif self.board[x + 2][y] == opp_player_num:
                        if x + 3 <= MAX_BOARD_SIZE:
                            if self.board[x + 3][y] == BOARD_AIR:
                                return "jump-forward"
                        elif x + 2 <= MAX_BOARD_SIZE:
                            if self.board[x + 2][y + 1] == BOARD_AIR\
                                and self.board[x + 2][y - 1] == BOARD_AIR:
                                return "jump-both"
                            elif self.board[x + 2][y + 1] == opp_player_num:
                                return "jump-left"
                            elif self.board[x + 2][y - 1] == opp_player_num:
                                return "jump-right"
            return "none"
        elif direction == "left":
            if x - 2 >= 0:
                if self.board[x - 1][y] == BOARD_AIR:
                    if self.board[x - 2][y] == BOARD_AIR:
                        return "walk"
                    elif self.board[x - 2][y] == opp_player_num:
                        if x - 3 >= 0:
                            if self.board[x - 3][y] == BOARD_AIR:
                                return "jump-forward"
                            elif self.board[x - 2][y + 1] == BOARD_AIR and self.board[x - 2][y - 1] == BOARD_AIR:
                                return "jump-both"
                            elif self.board[x - 2][y - 1] == opp_player_num:
                                return "jump-left"
                            elif self.board[x - 2][y + 1] == opp_player_num:
                                return "jump-right"
            return "none"
        return "none"

    def can_use_wall(self, player_num, x2, y2, dir):
        if dir == "vertical":
            x1 = x2
            x3 = x2
            y1 = y2 - 1
            y3 = y2 + 1
        elif dir == "horizon":
            x1 = x2 - 1
            x3 = x2 + 1
            y1 = y2
            y3 = y2
        else:
            return False
        # if player's wall remain and valid wall
        if self.board[x1][y1] == BOARD_AIR and self.board[x2][y2] == BOARD_AIR and self.board[x3][y3] == BOARD_AIR\
                and x2 % 2 == 0 and y2 % 2 == 0 and self.left_wall[player_num] > 0:
            self.board[x1][y1] = BOARD_WALL
            self.board[x2][y2] = BOARD_WALL
            self.board[x3][y3] = BOARD_WALL
            if self.calculate_need_turn(player_num) != -1 and self.calculate_need_turn(get_opponent_player(player_num)) != -1:
                self.board[x1][y1] = BOARD_AIR
                self.board[x2][y2] = BOARD_AIR
                self.board[x3][y3] = BOARD_AIR
                return True
            else:
                self.board[x1][y1] = BOARD_AIR
                self.board[x2][y2] = BOARD_AIR
                self.board[x3][y3] = BOARD_AIR
                return False
        else:
            return False

    def move_player_pos(self, player_num, direction):
        self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1]] = BOARD_AIR
        if direction == "up":
            self.player_pos[player_num][1] += 2
        elif direction == "down":
            self.player_pos[player_num][1] -= 2
        elif direction == "right":
            self.player_pos[player_num][0] += 2
        elif direction == "left":
            self.player_pos[player_num][0] -= 2
        else:
            return False
        self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1]] = player_num
        return True

    def jump_player_pos(self, player_num, direction, jump_way):
        self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1]] = BOARD_AIR
        if direction == "up":
            if jump_way == "jump-forward":
                self.player_pos[player_num][1] += 4
            elif jump_way == "jump-left":
                self.player_pos[player_num][0] -= 2
                self.player_pos[player_num][1] += 2
            elif jump_way == "jump-right":
                self.player_pos[player_num][0] += 2
                self.player_pos[player_num][1] += 2
            else:
                return False
        elif direction == "down":
            if jump_way == "jump-forward":
                self.player_pos[player_num][1] -= 4
            elif jump_way == "jump-left":
                self.player_pos[player_num][0] += 2
                self.player_pos[player_num][1] -= 2
            elif jump_way == "jump-right":
                self.player_pos[player_num][0] -= 2
                self.player_pos[player_num][1] -= 2
            else:
                return False
        elif direction == "right":
            if jump_way == "jump-forward":
                self.player_pos[player_num][0] += 4
            elif jump_way == "jump-left":
                self.player_pos[player_num][0] += 2
                self.player_pos[player_num][1] += 2
            elif jump_way == "jump-right":
                self.player_pos[player_num][0] += 2
                self.player_pos[player_num][1] -= 2
            else:
                return False
        elif direction == "left":
            if jump_way == "jump-forward":
                self.player_pos[player_num][0] -= 4
            elif jump_way == "jump-left":
                self.player_pos[player_num][0] -= 2
                self.player_pos[player_num][1] -= 2
            elif jump_way == "jump-right":
                self.player_pos[player_num][0] -= 2
                self.player_pos[player_num][1] += 2
            else:
                return False
        else:
            return False
        self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1]] = player_num

    def unuse_wall(self, player_num, str_x2, str_y2, dir):
        x2 = int(str_x2)
        y2 = int(str_y2)
        if dir == "vertical":
            x1 = x2
            x3 = x2
            y1 = y2 - 1
            y3 = y2 + 1
        elif dir == "horizon":
            x1 = x2 - 1
            x3 = x2 + 1
            y1 = y2
            y3 = y2
        else:
            return False
        self.board[x1][y1] = BOARD_AIR
        self.board[x2][y2] = BOARD_AIR
        self.board[x3][y3] = BOARD_AIR
        self.left_wall[player_num] += 1
        return True

    def calculate_need_turn(self, player_num: int, print_scoreboard=False):
        if player_num == 1:
            end_line = MAX_BOARD_SIZE
        elif player_num == 2:
            end_line = 1
        # 2차원 보드랑 똑같은 크기
        score_board = [[-1] * (MAX_BOARD_SIZE + 2) for i in range(MAX_BOARD_SIZE + 2)]
        count = 0
        # 2차원좌표 배열
        root_stack = [[self.player_pos[player_num][0], self.player_pos[player_num][1]]]
        score_board[self.player_pos[player_num][0]][self.player_pos[player_num][1]] = 0

        def set_root(pos, x, y, count):
            if score_board[pos[0] + x][pos[1] + y] == -1:
                score_board[pos[0] + x][pos[1] + y] = count
                root_stack.append([pos[0] + x, pos[1] + y])

        while True:
            count += 1
            tmp_stack = []
            tmp_stack.extend(root_stack)
            # root_stack 의 각 좌표마다 실행
            for pos in tmp_stack:
                # 위
                can_move_up = self.can_move(player_num, pos[0], pos[1], "up")
                if can_move_up != "none":
                    # 방문하지 않은곳이면
                    set_root(pos, 0, 2, count)
                # 아래
                can_move_down = self.can_move(player_num, pos[0], pos[1], "down")
                if can_move_down != "none":
                    set_root(pos, 0, -2, count)
                # 오른쪽
                can_move_right = self.can_move(player_num, pos[0], pos[1], "right")
                if can_move_right != "none":
                    set_root(pos, 2, 0, count)
                # 왼쪽
                can_move_left = self.can_move(player_num, pos[0], pos[1], "left")
                if can_move_left != "none":
                    set_root(pos, -2, 0, count)
                root_stack.remove(pos)
            if not root_stack:
                # for i in score_board:
                #     for j in i:
                #         print(str(j) + "\t", end='')
                #     print()
                return -1
            game_end = False
            score = MAX_BOARD_SIZE * MAX_BOARD_SIZE
            for i in range(MAX_BOARD_SIZE):
                if score_board[i][end_line] != -1:
                    game_end = True
                    if score_board[i][end_line] < score:
                        score = score_board[i][end_line]
            if game_end:
                if print_scoreboard:
                    for i in range(MAX_BOARD_SIZE, 0, -2):
                        for j in range(1, MAX_BOARD_SIZE + 1, 2):
                            print(str(score_board[j][i]) + "\t", end='')
                        print()
                return score



