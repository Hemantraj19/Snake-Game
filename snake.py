from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_objects = []
        self.create_snake()
        self.head = self.turtle_objects[0]

    def create_snake(self):
        for i in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=i * -20, y=0)
            self.turtle_objects.append(turtle)

    def reset(self):
        for object in self.turtle_objects:
            object.goto(1000, 1000)
        self.turtle_objects.clear()
        self.create_snake()
        self.head = self.turtle_objects[0]

    def grow_snake(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        x_cor = self.turtle_objects[-1].xcor()
        turtle.goto(x=x_cor - 20, y=0)
        self.turtle_objects.append(turtle)

    def move(self):
        for i in range(len(self.turtle_objects) - 1, 0, -1):
            self.turtle_objects[i].goto(
                self.turtle_objects[i - 1].xcor(), self.turtle_objects[i - 1].ycor()
            )
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
