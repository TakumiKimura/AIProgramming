#coding: utf-8
import random

START = "★"
NOMARK = "□"
MARKED = "■"
POSITION = "◎"

class Game:
    def __init__(self, X=4, Y=4):
        random.seed()
        self.size = (X, Y)
        self.start = (random.randint(0, X-1), random.randint(0, Y-1))
        self.pos = self.start
        self._init_map()
        self._mark(self.start[0], self.start[1], START)
    
    def get_position(self):
        # 現在のポジションを取得する
        return self.pos

    def move(self, X, Y):
        # 移動する
        # 移動成功の場合はTrue、失敗の場合はFalseが帰る
        if X >= self.size[0] or X < 0:
            return False
        if Y >= self.size[1] or Y < 0:
            return False

        # is point in around current position?
        if not self._can_move(X, Y):
            return False

        # is point NOMARK?
        if self.map[Y][X] != NOMARK:
            return False

        # Set old current position as MARKED
        if self.pos != self.start:
            self._mark(self.pos[0], self.pos[1], MARKED)

        # Set new current position as POSITION
        self.pos = (X, Y)
        self._mark(X, Y, POSITION)
        return True

    def _can_move(self, X, Y):
        if Y == self.pos[1]:
            if X == self.pos[0] + 1:
                return True
            if X == self.pos[0] - 1:
                return True
        if X == self.pos[0]:
            if Y == self.pos[1] + 1:
                return True
            if Y == self.pos[1] - 1:
                return True
        return False
            
    def print(self):
        # 現在の盤面をプリントする
        for line in self.map:
            for bit in line:
                print(bit, end=" ")
            print("", end="\n")

    def is_finished(self):
        # クリアしているかを判定する
        for line in self.map:
            for bit in line:
                if bit == NOMARK:
                    return False
        return True

    def _init_map(self):
        self.map = []
        for _ in range(self.size[0]):
            line = []
            for _ in range(self.size[1]):
                line.append(NOMARK)
            self.map.append(line)


    def _mark(self, X, Y, mark=MARKED):
        self.map[Y][X] = mark
