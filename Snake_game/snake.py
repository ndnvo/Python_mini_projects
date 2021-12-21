import time
from turtle import Screen, Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):# What happened when initiate)
        self.snake_list= []
        self.create_snake()
        self.head = self.snake_list[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_block = Turtle(shape="square")
        new_block.penup()
        new_block.color("white")
        new_block.goto(position)
        self.snake_list.append(new_block)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
             self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def reset(self):
        for seg in self.snake_list:
            seg.goto(1000,1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]