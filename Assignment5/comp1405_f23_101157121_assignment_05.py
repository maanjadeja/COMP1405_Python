#Name: Maansinh Jadeja
#Student Number: 101157121 
#Assignment 5

from comp1405_f23_special_library_loomwork_simplified import *

# def main():
patternWide = 16
nPatterns = 12
wide = patternWide*nPatterns
high = 13
height=16


open_window(wide,height)

for patternRepetition in range(12):

    for n in range(6):
        if(n%2==1):
            for i in range(height):
                add_bead("moss")
            next_thread()
            
        else:
            for j in range(height):
                add_bead("black")
            next_thread()

    for o in range(11):
        if(o<5):
            for k in range(height):
                # if(k%3==0 and k>(o*k)):#when the next increment of o happens it goes from the beginning and does all of row%3, we just want
                if(k==(o+1)*3):
                    add_bead("sky")#it to do 1 time instead of all, so lets keep a counter and multiply it to point the row
                else:
                    add_bead("lime")           
            
            next_thread()
        else:
            for l in range(height):
                if(l==5 or l==height-1):
                    add_bead("lemon")
                else:
                    add_bead("leather")

            next_thread()

keep_window()

# main()


# import turtle

# screen = turtle.Screen()
# screen.setup(200, 200)
# screen.bgcolor('lightgreen')

# bob = turtle.Turtle()
# bob.shape('turtle')
# bob.pensize(3)
# bob.circle(50)

# screen.exitonclick()
