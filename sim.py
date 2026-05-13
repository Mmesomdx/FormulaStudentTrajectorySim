import turtle
import random
    
    

class Display():
    def  __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=700, height=700)
        self.screen.bgcolor("green")
        self.screen.tracer(0)
        self.sprites = ["orange_cone.gif", "blue_cone.gif"]
        for sprite in self.sprites:
            self.screen.register_shape(sprite)
    

class Grapher(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.speed(0)
        
    # Function to draw a line between two points
    def draw_line(self,color,pos1,pos2,pensize=1):
        self.color(color)
        self.penup()
        self.pensize(pensize)
        self.goto(pos1[0], pos1[1])
        self.pendown()
        self.goto(pos2[0], pos2[1])
        self.penup()
    
    

class HelperFunctions():
    def __init__(self):
        pass
    #get midpoint between two points 
    def midpoint(self, p1, p2):
        mx = (p1[0] + p2[0]) / 2
        my = (p1[1] + p2[1]) / 2
        return (mx, my)
        
    #laplacian smoothing.
    def flatten(self, points):
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
            


class Simulation():
    def __init__(self):
        self.orange_cones = []
        self.blue_cones = []
        self.track_width = 150
        self.cone_spacing = 25
        self.horizontal_noise = 0
        self.vertical_noise = 0
    
    
    def draw_cone_trajectories(self):
        #draw line between consecutive cones (orange)
        for i in range(len(self.orange_cones)-1):
            cone_current = self.orange_cones[i]
            cone_next = self.orange_cones[i+1]
            Grapher().draw_line("red", cone_current.getPos(), cone_next.getPos())

        #draw line between consecutive cones (blue)
        for i in range(len(self.blue_cones)-1):
            cone_current = self.blue_cones[i]
            cone_next = self.blue_cones[i+1]
            Grapher().draw_line("red", cone_current.getPos(), cone_next.getPos())
    
    
    def draw_middle_trajectory(self):
        #draw average trajectory
        mid_points = []
        for i in range(len(self.orange_cones)):
            mid_points.append(HelperFunctions().midpoint(self.orange_cones[i].getPos(), self.blue_cones[i].getPos()))
            

        for i in range(len(mid_points)-1):
            mid_point_current = mid_points[i]
            mid_point_next = mid_points[i+1]
            Grapher().draw_line("yellow", mid_point_current, mid_point_next)
            

        mid_points = HelperFunctions().flatten(mid_points)

        for i in range(len(mid_points)-1):
            mid_point_current = mid_points[i]
            mid_point_next = mid_points[i+1]
            Grapher().draw_line("magenta", mid_point_current, mid_point_next)



        mid_points = HelperFunctions().flatten(mid_points)

        for i in range(len(mid_points)-1):
            mid_point_current = mid_points[i]
            mid_point_next = mid_points[i+1]
            Grapher().draw_line("cyan", mid_point_current, mid_point_next)
            

        #Ultra smoothed line!

        for i in range(10):
            mid_points = HelperFunctions().flatten(mid_points)

        for i in range(len(mid_points)-1):
            mid_point_current = mid_points[i]
            mid_point_next = mid_points[i+1]
            Grapher().draw_line("white", mid_point_current, mid_point_next,5)

        
    
    def setCones(self):

        for i in range(-10,10,1):
            y = i * self.cone_spacing
            offset = 0.005 * (y**2)  # tweak 0.02 to make the arc more or less curved
            
            self.orange_cones.append(Cone("orange", pos=(self.track_width + offset - 100 + random.uniform(-self.horizontal_noise,self.horizontal_noise),i*self.cone_spacing + random.uniform(-self.vertical_noise,self.vertical_noise))))
            self.blue_cones.append(Cone("blue", pos=(-self.track_width + offset - 100 + random.uniform(-self.horizontal_noise,self.horizontal_noise), i*self.cone_spacing + random.uniform(-self.vertical_noise,self.vertical_noise))))
    
    
    
    def run(self):
        display = Display()
        self.setCones()
        self.draw_cone_trajectories()
        self.draw_middle_trajectory()
        display.screen.update()
        display.screen.mainloop()


s = Simulation()
s.run()


    


    

        
