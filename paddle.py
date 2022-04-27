from turtle import Turtle, shape

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.pu()
        self.goto(position)
    def go_up(self):
    # move paddle using coordinates: because "setheading" will turn the paddle
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(x=new_x, y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(x=new_x, y=new_y)
