import time
from snake import Snake_Game
from turtle import  Screen
from snakeFood import Food
from snakeScore import Score

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake_Game()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
# move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
# detect collision with food    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend() 
        snake.add_segment(snake.segments[-1].position())
        score.increase_score()
        
#detect collision with wall
    if snake.head.xcor()>240 or snake.head.xcor()<-240 or snake.head.ycor()>240 or snake.head.ycor()<-240:
        game_is_on = False
        score.game_over() 
        
#detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
        
        
        

screen.exitonclick()