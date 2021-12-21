from turtle import Turtle
UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.turtlesize(stretch_wid=0.8, stretch_len=6)
        self.left(UP)
        self.color("white")

    def down(self):
        self.setheading(DOWN)

    def up(self):
        self.setheading(UP)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def auto_move(self):
        self.move()
        out = self.ycor() < 240 and self.ycor() > -240
        if not out:
            self.left(180)
            self.move()


    #
    #
    #
    #
    #     self.snake_list= []
    #     self.create_snake()
    #     self.head = self.snake_list[0]
    #
    #
    # def create_snake(self):
    #     for position in STARTING_POSITIONS:
    #         self.add_segment(position)
    #
    # def add_segment(self,position):
    #     new_block = Turtle(shape="square")
    #     new_block.penup()
    #     new_block.color("white")
    #     new_block.goto(position)
    #     self.snake_list.append(new_block)
    #
    # def extend(self):
    #     self.add_segment(self.snake_list[-1].position())
    #

    #









# from turtle import Turtle
# UP = 90
# DOWN = 270
# MOVE_DISTANCE = 20
#
#
# class Paddle(Turtle):
#     def __init__(self, position):  # What happened when initiate)
#         self.paddle_list = []
#
#         for i in position:
#             new_block = Turtle(shape="square")
#             new_block.penup()
#             new_block.left(90)
#             new_block.color("white")
#             new_block.goto(i)
#             self.paddle_list.append(new_block)
#         self.head = self.paddle_list[0]
#
#     def down(self):
#         self.head.setheading(DOWN)
#
#     def up(self):
#         self.head.setheading(UP)
#
#     def move(self):
#         for seg_num in range(len(self.paddle_list) - 1, 0, -1):
#             new_x = self.paddle_list[seg_num - 1].xcor()
#             new_y = self.paddle_list[seg_num - 1].ycor()
#             self.paddle_list[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#
#     def auto_move(self):
#         self.move()
#         out = self.head.ycor() < 240 and self.head.ycor() > -240
#         if not out:
#             self.head.left(180)
#             self.move()
#
#
#     #
#     #
#     #
#     #
#     #     self.snake_list= []
#     #     self.create_snake()
#     #     self.head = self.snake_list[0]
#     #
#     #
#     # def create_snake(self):
#     #     for position in STARTING_POSITIONS:
#     #         self.add_segment(position)
#     #
#     # def add_segment(self,position):
#     #     new_block = Turtle(shape="square")
#     #     new_block.penup()
#     #     new_block.color("white")
#     #     new_block.goto(position)
#     #     self.snake_list.append(new_block)
#     #
#     # def extend(self):
#     #     self.add_segment(self.snake_list[-1].position())
#     #
#
#     #
#
#
