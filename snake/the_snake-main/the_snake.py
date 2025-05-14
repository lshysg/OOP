from random import choice
import pygame

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SPEED = 15

ALL_CELLS = {(x * GRID_SIZE, y * GRID_SIZE) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)}

# Инициализация
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

class GameObject:
    def __init__(self):
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

    def draw(self):
        raise NotImplementedError

class Apple(GameObject):
    def __init__(self, snake_positions):
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position(snake_positions)

    def randomize_position(self, snake_positions):
        free_cells = ALL_CELLS - set(snake_positions)
        if free_cells:
            self.position = choice(list(free_cells))

    def draw(self):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

class Snake(GameObject):
    def __init__(self):
        super().__init__()
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        self.last = None
        self.just_ate = False  # Флаг, указывающий, что змейка только что съела яблоко

    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = (
            (head_x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT
        )

        if new_head in self.positions[1:]:
            self.reset()
            return True

        self.positions.insert(0, new_head)

        if not self.just_ate and len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None
            self.just_ate = False
        
        return False

    def draw(self):
        for position in self.positions:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        return self.positions[0]

    def reset(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None
        self.just_ate = False

def handle_keys(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.next_direction = RIGHT

def main():
    snake = Snake()
    apple = Apple(snake.positions)

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()

        # Проверка на съедание яблока
        if snake.get_head_position() == apple.position:
            snake.length += 1
            snake.just_ate = True  # Устанавливаем флаг
            apple.randomize_position(snake.positions)
            # Сразу перерисовываем сцену без задержки
            screen.fill(BOARD_BACKGROUND_COLOR)
            snake.draw()
            apple.draw()
            pygame.display.update()
            continue  # Пропускаем обычное движение в этом кадре

        reset_occurred = snake.move()
        if reset_occurred:
            apple.randomize_position(snake.positions)

        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw()
        apple.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()