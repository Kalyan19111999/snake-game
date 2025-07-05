from turtle import Turtle

STARTING_SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # Managing snake's body
        self.snakes_body = []
        self.create_snake()
        self.head = self.snakes_body[0]

    def create_snake(self):
        for _ in range(3):
            self.create_piece(STARTING_SNAKE_POSITIONS[_])

    def create_piece(self, position):
        snake_piece = Turtle(shape="square")
        snake_piece.color("white")
        snake_piece.up()

        snake_piece.goto(position)
        self.snakes_body.append(snake_piece)

    def move(self) -> None:
        for snake_piece in range(len(self.snakes_body) - 1, 0, -1):
            changed_x, changed_y = self.snakes_body[snake_piece - 1].xcor(), self.snakes_body[snake_piece - 1].ycor()
            self.snakes_body[snake_piece].goto((changed_x, changed_y))
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow_snake(self):
        self.create_piece(self.snakes_body[-1].position())

    def tail_collision(self) -> bool:
        for snake_piece in self.snakes_body[1:]:
            if self.head.distance(snake_piece) < 10:
                return True
        return False