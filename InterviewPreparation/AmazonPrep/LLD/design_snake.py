from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food_map = food
        self.direction_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        self.food_index = 0
        self.snake = deque([(0,0)])
        self.snake_set = {(0,0): 1}

    def move(self, direction: str) -> int:
        move = self.direction_map.get(direction)
        x_curr, y_curr = self.snake[0]
        x_new, y_new = x_curr + move[0], y_curr + move[1]
        if x_new >= self.width or x_new < 0 or y_new < 0 or y_new >= self.height:
            return -1
        if self.food_index >= len(self.food_map):
            return -1
        if (x_new, y_new) in self.snake_set or (x_new, y_new) == self.snake[-1]:
            return -1
        
        if self.food_index < len(self.food_map) \
           and self.food_map[self.food_index][0] == x_new \
           and self.food_map[self.food_index][1] == y_new:
            self.food_index += 1
        else:
            tail = self.snake.pop()
            del self.snake_set[tail]
        
        self.snake.appendleft((x_new, y_new))
        self.snake_set[(x_new, y_new)] = 1
        return len(self.snake) - 1


        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)