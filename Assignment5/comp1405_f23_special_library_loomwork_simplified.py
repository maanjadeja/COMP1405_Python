
#         d888888o. 8888888 8888888888 ,o888888o.     8 888888888o          # 
#       .`8888:' `88.     8 8888    . 8888     `88.   8 8888    `88.        # 
#       8.`8888.   Y8     8 8888   ,8 8888       `8b  8 8888     `88        # 
#       `8.`8888.         8 8888   88 8888        `8b 8 8888     ,88        #
#        `8.`8888.        8 8888   88 8888         88 8 8888.   ,88'        #
#         `8.`8888.       8 8888   88 8888         88 8 888888888P'         # 
#          `8.`8888.      8 8888   88 8888        ,8P 8 8888                #
#      8b   `8.`8888.     8 8888   `8 8888       ,8P  8 8888                #
#      `8b.  ;8.`8888     8 8888    ` 8888     ,88'   8 8888                #
#       `Y8888P ,88P'     8 8888       `8888888P'     8 8888                #

#  It is important to recognize that you are neither expected nor required  #
#  to "read" the source code that has been provided here. In fact, reading  #
#  this code without first reading the documentation might lead to serious  #
#  errors when submitting your own assignments. Although you are certainly  #
#  welcome to review this code if you wish to (and especially if you would  #
#  like to see how function polymorphism can be implemented in Python with  #
#  structural pattern matching), using this module correctly requires only  #
#  that you read the documentation provided, not the module source itself.  #


# Python "turtle" graphics should be available after a typical install
import turtle as _logo

# this 24-colour palette is from the PICO-8 fantasy console (which you
# can learn much more about by visiting www.lexaloffle.com/pico-8.php)
# it has been here implemented as a dictionary of three integer tuples
# (n.b., each assigned palette is no longer procedurally generated)

_palette = {}
_palette["black"]     = (  0,   0,   0)
_palette["silver"]    = (194, 195, 199)
_palette["white"]     = (255, 241, 232)
_palette["orange"]    = (255, 163,   0)
_palette["lemon"]     = (255, 236,  39)
_palette["sky"]       = ( 41, 173, 255)
_palette["pink"]      = (255, 119, 168)
_palette["peach"]     = (255, 204, 170)
_palette["cocoa"]     = ( 41,  24,  20)
_palette["olive"]     = (162, 136, 121)
_palette["sand"]      = (243, 239, 125)
_palette["carrot"]    = (255, 108,  36)
_palette["tea"]       = (168, 231,  46)
_palette["denim"]     = (  6,  90, 181)
_palette["salmon"]    = (255, 110,  89)
_palette["coral"]     = (255, 157, 129)
_palette["storm"]     = ( 29,  43,  83)
_palette["wine"]      = (126,  37,  83)
_palette["moss"]      = (  0, 135,  81)
_palette["tan"]       = (171,  82,  54)
_palette["slate"]     = ( 95,  87,  79)
_palette["ember"]     = (255,   0,  77)
_palette["lime"]      = (  0, 228,  54)
_palette["dusk"]      = (131, 118, 156)
_palette["leather"]   = (116,  47,  41)


# ------------------------------------------------------------------ #

# this module uses variables that are in global scope in order to
# track the vertical position (i.e., warp thread) and the horizontal
# position (i.e., weft thread) onto which the next bead is placed
global_weft_index = 1
global_warp_index = 1

# this module also uses a global constant for the bead radius (and
# note the use of all caps in the name to emphasize this constancy)
CONST_BEAD_WIDE = 8
CONST_BEAD_HIGH = 30
CONST_WEFT_GAP = 4
CONST_WARP_GAP = 8
# CONST_BEAD_RADIUS = 20

# ------------------------------------------------------------------ #

# this function doesn't do anything at all (and is just a placeholder)
def _pass() -> None:
	pass

# ------------------------------------------------------------------ #

# this function moves the turtle to the co-ordinates provided (and was
# included because turtle graphics uses the center of the screen as an
# origin, instead of using the much more common top-left corner pixel)
# n.b., the type hints indicate there are two integer arguments (i.e., 
# the x and y co-ordinate values, in that order) but no return value.
def _goto(x: int, y: int) -> None:
	_turtle.setpos(x - _logo.window_width() // 2, _logo.window_height() // 2 - y)

# ------------------------------------------------------------------ #

# this function is simply used to "bookend" any drawing routines...
def _init(x: int, y: int, clr: str) -> None:
	_goto(x, y)
	_turtle.setheading(0)
	if clr not in _palette.keys():
		raise_error('''INVALID_COLOUR''')	
		_turtle.color(_palette["black"])		
	else:
		_turtle.color(_palette[clr])
	_turtle.begin_fill()
	_turtle.pendown()

# ...and so is this one
def _term() -> None:
	_turtle.setheading(0)
	_turtle.penup()
	_turtle.end_fill()

# ------------------------------------------------------------------ #

# this function draws a bead of the colour provided onto the current
# weft thread, then (just as one would do if creating actual beadwork)
# moves *down* to the next position on the current weft thread (i.e.,
# change the warp thread without changing the weft thread)
def add_bead(arg_bead_colour: str) -> None:
	global global_warp_index
	x = global_weft_index * (CONST_BEAD_WIDE + CONST_WEFT_GAP)
	y = global_warp_index * (CONST_BEAD_HIGH + CONST_WARP_GAP)
	_goto(x, y)
	_turtle.begin_fill()
	_turtle.pendown()
	_turtle.color(_palette[arg_bead_colour])
	_goto(x + CONST_BEAD_WIDE, y)
	_goto(x + CONST_BEAD_WIDE, y + CONST_BEAD_HIGH)
	_goto(x, y + CONST_BEAD_HIGH)
	_goto(x, y)
	_turtle.penup()
	_turtle.end_fill()
	# _init(global_weft_index * CONST_BEAD_RADIUS * 2, global_warp_index * CONST_BEAD_RADIUS * 2, arg_bead_colour)
	# _turtle.forward(CONST_BEAD_RADIUS)
	# _turtle.left(90)
	# _turtle.circle(CONST_BEAD_RADIUS)
	# _term()
	global_warp_index += 1

# this function must be called manually once a column of beads has
# been completed, in order to move *right* to the next weft thread
# it also resets the warp thread as well (i.e., resets to the top)
# n.b., this function does nothing if there are no beads on the
# current weft thread (i.e., column)
def next_thread() -> None:
	global global_warp_index
	if global_warp_index > 1:
		global_warp_index = 1
		global global_weft_index
		global_weft_index += 1

# ------------------------------------------------------------------ #

# this function is used to create the initial drawing window, but,
# unlike its counterpart in "Easy Graphics", the parameters in this
# function are the number of threads (and thus the window dimensions
# are the product of these values and the contstant bead diameter)
def open_window(number_weft_threads: int = 36, number_warp_threads: int = 7) -> None:
	global _window, _turtle, global_weft_index, global_warp_index
	global_weft_index = 1
	global_warp_index = 1
	screen_wide = (number_weft_threads + 2) * (CONST_BEAD_WIDE + CONST_WEFT_GAP) + 3
	screen_high = (number_warp_threads + 2) * (CONST_BEAD_HIGH + CONST_WARP_GAP) + 1
	_window = _logo.Screen()
	_window.cv._rootwindow.resizable(False, False)
	print(screen_wide, screen_high)
	_window.setup(screen_wide, screen_high)
	_window.colormode(255)
	_window.tracer(0)
	_window.bgcolor(_palette["black"])	
	_turtle = _logo.Turtle()

	_turtle.width(3)
	# _turtle.color(_palette["tan"])
	
	# for i in range(number_warp_threads + 1):
	# 	y = (i + 1) * (CONST_BEAD_HIGH + CONST_WARP_GAP) - 4
	# 	_turtle.penup()
	# 	_goto(0, y)
	# 	_turtle.pendown()
	# 	_goto(screen_wide, y)
	# 	_turtle.penup()

	# _turtle.width(1)
	
	# for i in range(number_weft_threads):
	# 	x = (i + 1) * (CONST_BEAD_WIDE + CONST_WEFT_GAP) + 4
	# 	_turtle.penup()
	# 	_goto(x, CONST_BEAD_HIGH + 2)
	# 	_turtle.pendown()
	# 	_goto(x, screen_high - CONST_BEAD_HIGH - 10)
	# 	_turtle.penup()

	# _turtle.hideturtle()
	# _turtle.speed(0)
	# _turtle.width(0)
	

def fill_window(clr: str) -> None:
	_window.bgcolor(_palette[clr])

def save_window() -> None:
	_logo.getcanvas().postscript(file = "postscript_image_generated_by_easy_graphics.eps")

def keep_window() -> None:
	_logo.exitonclick()

def insert_grid(dim: int) -> None:
	wid = _window.window_width()
	hgt = _window.window_height()
	for x in range(0, wid, dim):
		_main_line((x, 0), (x, hgt), "charcoal")
	for y in range(0, hgt, dim):
		_main_line((0, y), (wid, y), "charcoal")