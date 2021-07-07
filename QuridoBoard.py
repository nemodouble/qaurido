MAX_BOARD_SIZE = 16
START_WALL_COUNT = 8

class QuridoBoard:
    def __init__(self):
        self.board = [[0] * (MAX_BOARD_SIZE + 1) for i in range(MAX_BOARD_SIZE + 1)]
        self.player_left_wall[1] = START_WALL_COUNT
        self.player_left_wall[2] = START_WALL_COUNT
        self.board[MAX_BOARD_SIZE/2 + 1,2] = 1
        self.board[MAX_BOARD_SIZE/2 + 1,MAX_BOARD_SIZE-2] = 2
        self.player_pos[1] = [MAX_BOARD_SIZE/2 + 1,2]
        self.player_pos[2] = [MAX_BOARD_SIZE/2 + 1,MAX_BOARD_SIZE-2]

    def move_player(self, player_num, direction):
        # 조건 검사
        if self.can_move_player(player_num, direction) == "walk":
            if self.move_player_pos(player_num, direction, 2):
                return True
        return False

    def can_move_player(self, player_num, direction):
        if direction == "up":
            if self.player_pos[player_num][1] + 2 < MAX_BOARD_SIZE:
                if self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1] + 1] == 0:
                    if self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1] + 2] == 0:
                        return "walk"
                    elif self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1] + 2] == 1:
                        if self.player_pos[player_num][1] + 3 < MAX_BOARD_SIZE:
                            if self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1] + 3] == 0:
                                return "jump-forwad"
                            elif self.board[self.player_pos[player_num][0] + 1][self.player_pos[player_num][1] + 2] == 0\
                                and self.board[self.player_pos[player_num][0] - 1][self.player_pos[player_num][1] + 2] == 0:
                                return "jump-both"
                            elif self.board[self.player_pos[player_num][0] + 1][self.player_pos[player_num][1] + 2] == 1:
                                return "jump-left"
                            elif self.board[self.player_pos[player_num][0] - 1][self.player_pos[player_num][1] + 2] == 1:
                                return "jump-right"
            return "none"

        elif direction == "down":
            if self.player_pos[player_num][1] - 2 > 0:
                if self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1] - 1] == 0:
                    if self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1] - 2] == 0:
                        return "walk"
        elif direction == "right":
            if self.player_pos[player_num][0] + 2 < MAX_BOARD_SIZE:
                if self.board[self.player_pos[player_num][0] + 1][self.player_pos[player_num][1]] == 0:
                    if self.board[self.player_pos[player_num][0] + 2][self.player_pos[player_num][1]] == 0:
                        return "walk"
        elif direction == "left":
            if self.player_pos[player_num][1] - 2 < 0:
                if self.board[self.player_pos[player_num][0] - 1][self.player_pos[player_num][1]] == 0:
                    if self.board[self.player_pos[player_num][0] - 2][self.player_pos[player_num][1]] == 0:
                        return "walk"
        return "None"

    def move_player_pos(self, player_num, direction, len):
        self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1]] = 0
        if direction == "up":
            self.player_pos[player_num][1] += len
        elif direction == "down":
            self.player_pos[player_num][1] -= len
        elif direction == "right":
            self.player_pos[player_num][0] += len
        elif direction == "left":
            self.player_pos[player_num][0] -= len
        else:
            return False
        self.board[self.player_pos[player_num][0]][self.player_pos[player_num][1]] = player_num
        return True

    def jump_player(self, player_num, direction):
        None

    def use_wall(self, player_num, x1, y1, x2, y2):
        None
        # 벽 놓을 수 있는지 조건 검사




