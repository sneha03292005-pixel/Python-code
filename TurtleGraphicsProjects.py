
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.speed('fastest')
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


#useful for random colours and random directions for the below codes
# tim=Turtle()
# colours=['blue','green','purple','orange','pink','brown','grey']
# directions=[0,90,180,270]

#its drawing random lines in random directions and random colours 
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.pensize(15)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.speed('fastest')
    
    

#different type of shapes drawn in random colours
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         tim.forward(70)
#         tim.right(angle)     
# for shape_size_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_size_n)         
                                                                                                  