import turtle
import random

sc = turtle.Screen()
sc.setup(width=700, height=700)
sc.bgcolor("green")
sc.tracer(0)
sprites = ["orange_cone.gif", "blue_cone.gif"]
for sprite in sprites:
    sc.register_shape(sprite)
    
    
    
    
grapher = turtle.Turtle()
grapher.hideturtle()
grapher.speed(0)

# Function to draw a line between two points
def draw_line(color,pos1,pos2):
    grapher.color(color)
    grapher.penup()
    grapher.goto(pos1[0], pos1[1])
    grapher.pendown()
    grapher.goto(pos2[0], pos2[1])
    grapher.penup()
    
    
def midpoint(p1, p2):
    mx = (p1[0] + p2[0]) / 2
    my = (p1[1] + p2[1]) / 2
    return (mx, my)
    
#laplacian smoothing.
def flatten(points):
    new_points = []
    # Add the first point as is
    new_points.append(points[0])
    
    # Average every middle point with the one before it and after it
    for i in range(1, len(points) - 1):
        x = (points[i-1][0] + points[i][0] + points[i+1][0]) / 3
        y = (points[i-1][1] + points[i][1] + points[i+1][1]) / 3
        new_points.append((x, y))
        
    # Add the last point as is
    new_points.append(points[-1])
    return new_points
    
    
    


class Cone(turtle.Turtle):
    def __init__(self, cone_type="orange", pos=(0,0)):
        turtle.Turtle.__init__(self)
        self.cone_type = cone_type
        self.penup()
        self.setpos(pos[0], pos[1])
        if cone_type == "orange":
            self.shape("orange_cone.gif")
        elif cone_type == "blue":
            self.shape("blue_cone.gif")
        else:
            self.shape("circle")
            self.color("red")
    
    def getPos(self):
        return (self.xcor(), self.ycor())
            


class Car(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("#00ddff")
        self.shape("turtle")

orange_cones = []
blue_cones = []
track_width = 150
cone_spacing = 25

horizontal_noise = 0
vertical_noise = 0




for i in range(-10,10,1):
    y = i * cone_spacing
    offset = 0.005 * (y**2)  # tweak 0.02 to make the arc more or less curved
    
    
    orange_cones.append(Cone("orange", pos=(track_width + offset - 100 + random.uniform(-horizontal_noise,horizontal_noise),i*cone_spacing + random.uniform(-vertical_noise,vertical_noise))))
    blue_cones.append(Cone("blue", pos=(-track_width + offset - 100 + random.uniform(-horizontal_noise,horizontal_noise), i*cone_spacing + random.uniform(-vertical_noise,vertical_noise))))
    

blue_cones[3].setx(-1000)
    
#print orange cones
print("ORANGE CONE COORDS:")
for cone in orange_cones:
    print(cone.getPos())

#print blue cones
print("BLUE CONE COORDS:")
for cone in blue_cones:
    print(cone.getPos())
    

orange_positions = []
blue_positions = []

#draw line between consecutive cones (orange)
for i in range(len(orange_cones)-1):
    cone_current = orange_cones[i]
    cone_next = orange_cones[i+1]
    draw_line("red", cone_current.getPos(), cone_next.getPos())

#draw line between consecutive cones (blue)
for i in range(len(blue_cones)-1):
    cone_current = blue_cones[i]
    cone_next = blue_cones[i+1]
    draw_line("red", cone_current.getPos(), cone_next.getPos())


#draw average trajectory
mid_points = []
for i in range(len(orange_cones)):
    mid_points.append(midpoint(orange_cones[i].getPos(), blue_cones[i].getPos()))
    

for i in range(len(mid_points)-1):
    mid_point_current = mid_points[i]
    mid_point_next = mid_points[i+1]
    draw_line("yellow", mid_point_current, mid_point_next)
    

mid_points = flatten(mid_points)

for i in range(len(mid_points)-1):
    mid_point_current = mid_points[i]
    mid_point_next = mid_points[i+1]
    draw_line("magenta", mid_point_current, mid_point_next)



mid_points = flatten(mid_points)

for i in range(len(mid_points)-1):
    mid_point_current = mid_points[i]
    mid_point_next = mid_points[i+1]
    draw_line("cyan", mid_point_current, mid_point_next)
    

#Ultra smoothed line!

for i in range(10):
    mid_points = flatten(mid_points)

for i in range(len(mid_points)-1):
    mid_point_current = mid_points[i]
    mid_point_next = mid_points[i+1]
    draw_line("white", mid_point_current, mid_point_next)



    

sc.update()
sc.mainloop()
        
        
