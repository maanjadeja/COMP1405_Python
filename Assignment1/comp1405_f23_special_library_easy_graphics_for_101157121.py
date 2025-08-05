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

# the wrap function from textwrap is used for displaying error messages
from textwrap import wrap

# this 32-colour palette is from the PICO-8 fantasy console (which you
# can learn much more about by visiting www.lexaloffle.com/pico-8.php)
# it has been here implemented as a dictionary of three integer tuples

# please note, however, that only 24 of these colours will actually be
# permitted when completing your assignments, and the only way to know
# which 24 of the 32 colours are "valid" is to read your documentation

# only one of the colours	"storm"	and	"midnight"	will be permitted
# only one of the colours 	"wine"	and	"port"		will be permitted
# only one of the colours 	"moss"	and	"sea"		will be permitted
# only one of the colours 	"tan"	and	"leather"	will be permitted
# only one of the colours 	"slate"	and	"charcoal"	will be permitted
# only one of the colours 	"ember"	and	"crimson"	will be permitted
# only one of the colours 	"lime"	and	"jade"		will be permitted
# only one of the colours 	"dusk"	and	"aubergine"	will be permitted

_showing_errors = True

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

# a palette of 16 colours was defined above, but there are 8 pairs of
# similar colours that will each contribute one additional colour to
# the palette, determined at random using your student id number

POSSIBLE_COLOUR_STORM      = ( 29,  43,  83)
POSSIBLE_COLOUR_MIDNIGHT   = ( 17,  29,  53)
POSSIBLE_COLOUR_WINE       = (126,  37,  83)
POSSIBLE_COLOUR_PORT       = ( 66,  33,  54)
POSSIBLE_COLOUR_MOSS       = (  0, 135,  81)
POSSIBLE_COLOUR_SEA        = ( 18,  83,  89)
POSSIBLE_COLOUR_TAN        = (171,  82,  54)
POSSIBLE_COLOUR_LEATHER    = (116,  47,  41)
POSSIBLE_COLOUR_SLATE      = ( 95,  87,  79)
POSSIBLE_COLOUR_CHARCOAL   = ( 73,  51,  59)
POSSIBLE_COLOUR_EMBER      = (255,   0,  77)
POSSIBLE_COLOUR_CRIMSON    = (190,  18,  80)
POSSIBLE_COLOUR_LIME       = (  0, 228,  54)
POSSIBLE_COLOUR_JADE       = (  0, 181,  67)
POSSIBLE_COLOUR_DUSK       = (131, 118, 156)
POSSIBLE_COLOUR_AUBERGINE  = (117,  70, 101)

# none of the other possible colours is added to the palette until
# the program that generates each unique copy of this library has
# uncommented the corresponding line; to clarify, if a student is
# given access to the colour "storm", the corresponding line will
# be uncommented when that version of the library is generated

# _palette['''storm''']     = POSSIBLE_COLOUR_STORM
_palette['''midnight''']  = POSSIBLE_COLOUR_MIDNIGHT
# _palette['''wine''']      = POSSIBLE_COLOUR_WINE
_palette['''port''']      = POSSIBLE_COLOUR_PORT
_palette['''moss''']      = POSSIBLE_COLOUR_MOSS
# _palette['''sea''']       = POSSIBLE_COLOUR_SEA
# _palette['''tan''']       = POSSIBLE_COLOUR_TAN
_palette['''leather''']   = POSSIBLE_COLOUR_LEATHER
# _palette['''slate''']     = POSSIBLE_COLOUR_SLATE
_palette['''charcoal''']  = POSSIBLE_COLOUR_CHARCOAL
_palette['''ember''']     = POSSIBLE_COLOUR_EMBER
# _palette['''crimson''']   = POSSIBLE_COLOUR_CRIMSON
# _palette['''lime''']      = POSSIBLE_COLOUR_LIME
_palette['''jade''']      = POSSIBLE_COLOUR_JADE
_palette['''dusk''']      = POSSIBLE_COLOUR_DUSK
# _palette['''aubergine'''] = POSSIBLE_COLOUR_AUBERGINE

# this is where the "dictionary" of error codes is populated, and although
# it may appear slightly redundant, it has been implemented in this manner
# because subsequent versions may use more elaborate messages to instruct
# novice users in how to correct these errors; that said, in most cases the
# instructions will be "read the documentation carefully"

_error_codes = {}

_error_codes["INVALID_COLOUR"]                         = '''One of the colours you have used does not appear in the colour palette that was assigned specifically to you. Review your documentation for your list of permitted colours.'''

_error_codes["INVALID_ARGS_FOR_RECT_FUNCTION"]         = '''You are calling your rectangle drawing function with a pattern of arguments (i.e., values appearing in the round brackets) that isn't recognized. Review the documentation assigned specifically to you and ensure that you are providing all of the necessary arguments, listing the arguments in the correct order, and using quotation marks around your selected colour.'''
_error_codes["INVALID_ARGS_FOR_LINE_FUNCTION"]         = '''You are calling your line drawing function with a pattern of arguments (i.e., values appearing in the round brackets) that isn't recognized. Review the documentation assigned specifically to you and ensure that you are providing all of the necessary arguments, listing the arguments in the correct order, and using quotation marks around your selected colour.'''
_error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION"]         = '''You are calling your circle drawing function with a pattern of arguments (i.e., values appearing in the round brackets) that isn't recognized. Review the documentation assigned specifically to you and ensure that you are providing all of the necessary arguments, listing the arguments in the correct order, and using quotation marks around your selected colour.'''
_error_codes["INVALID_ARGS_FOR_POLY_FUNCTION"]         = '''You are calling your poly drawing function with a pattern of arguments (i.e., values appearing in the round brackets) that isn't recognized. Review the documentation assigned specifically to you and ensure that you are providing all of the necessary arguments, listing the arguments in the correct order, and using quotation marks around your selected colour.'''

_error_codes["INVALID_FUNCTION_NAME_DRAW_LINE"]        = '''The "draw_line" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_PLOT_LINE"]        = '''The "plot_line" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''

_error_codes["INVALID_FUNCTION_NAME_DRAW_RECT"]        = '''The "draw_rect" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_DRAW_RECTANGLE"]   = '''The "draw_rectangle" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_PLOT_RECT"]        = '''The "plot_rect" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_PLOT_RECTANGLE"]   = '''The "plot_rectangle" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''

_error_codes["INVALID_FUNCTION_NAME_DRAW_CIRC"]        = '''The "draw_circ" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_DRAW_CIRCLE"]      = '''The "draw_circle" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_PLOT_CIRC"]        = '''The "plot_circ" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_PLOT_CIRCLE"]      = '''The "plot_circle" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''

_error_codes["INVALID_FUNCTION_NAME_DRAW_POLY"]        = '''The "draw_poly" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_DRAW_POLYGON"]     = '''The "draw_polygon" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_PLOT_POLY"]        = '''The "plot_poly" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''
_error_codes["INVALID_FUNCTION_NAME_PLOT_POLYGON"]     = '''The "plot_polygon" function does not appear in your list of permitted functions. Review the documentation assigned to you and ensure that you use the function name exactly as it was specified in the documentation assigned specfically to you.'''

# there are several unique error codes that all map to the same message,
# because some (but not all) errors are procedurally removed from a specific
# instance of the library, and this facilitates that replacement

_error_codes["INVALID_ARGS_FOR_RECT_FUNCTION_STR_TUPLE"]               = _error_codes["INVALID_ARGS_FOR_RECT_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_RECT_FUNCTION_STR_TUPLE_INT_INT"]       = _error_codes["INVALID_ARGS_FOR_RECT_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_RECT_FUNCTION_STR_INT_INT_INT_INT"]     = _error_codes["INVALID_ARGS_FOR_RECT_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_RECT_FUNCTION_TUPLE_STR"]               = _error_codes["INVALID_ARGS_FOR_RECT_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_RECT_FUNCTION_TUPLE_INT_INT_STR"]       = _error_codes["INVALID_ARGS_FOR_RECT_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_RECT_FUNCTION_INT_INT_INT_INT_STR"]     = _error_codes["INVALID_ARGS_FOR_RECT_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_RECT_FUNCTION_UNRECOGNIZED"]            = _error_codes["INVALID_ARGS_FOR_RECT_FUNCTION"]

_error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION_STR_TUPLE"]               = _error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION_STR_TUPLE_INT''')"]       = _error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION_STR_INT_INT_INT''')"]     = _error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION_TUPLE_STR''')"]           = _error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION_TUPLE_INT_STR''')"]       = _error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION_INT_INT_INT_STR''')"]     = _error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION_UNRECOGNIZED"]            = _error_codes["INVALID_ARGS_FOR_CIRC_FUNCTION"]

_error_codes["INVALID_ARGS_FOR_LINE_FUNCTION_STR_TUPLE_TUPLE"]         = _error_codes["INVALID_ARGS_FOR_LINE_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_LINE_FUNCTION_TUPLE_TUPLE_STR"]         = _error_codes["INVALID_ARGS_FOR_LINE_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_LINE_FUNCTION_STR_INT_INT_INT_INT"]     = _error_codes["INVALID_ARGS_FOR_LINE_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_LINE_FUNCTION_INT_INT_INT_INT_STR"]     = _error_codes["INVALID_ARGS_FOR_LINE_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_LINE_FUNCTION_UNRECOGNIZED"]            = _error_codes["INVALID_ARGS_FOR_LINE_FUNCTION"]

_error_codes["INVALID_ARGS_FOR_POLY_FUNCTION_STR_LIST"]                = _error_codes["INVALID_ARGS_FOR_POLY_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_POLY_FUNCTION_STR_LIST_LIST"]           = _error_codes["INVALID_ARGS_FOR_POLY_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_POLY_FUNCTION_LIST_STR"]                = _error_codes["INVALID_ARGS_FOR_POLY_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_POLY_FUNCTION_LIST_LIST_STR"]           = _error_codes["INVALID_ARGS_FOR_POLY_FUNCTION"]
_error_codes["INVALID_ARGS_FOR_POLY_FUNCTION_UNRECOGNIZED"]            = _error_codes["INVALID_ARGS_FOR_POLY_FUNCTION"]

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

	if clr not in _palette.keys():
		raise_error('''INVALID_COLOUR''')	
		_turtle.color(_palette["black"])		
	else:
		_turtle.color(_palette[clr])

	_goto(x, y)
	_turtle.setheading(0)
	_turtle.begin_fill()
	_turtle.pendown()

# ...and so is this one
def _term() -> None:
	_turtle.setheading(0)
	_turtle.penup()
	_turtle.end_fill()

# ------------------------------------------------------------------ #

# this is the function for drawing rectangles, but like many functions
# in this module it must be emphasized that using an underscore at the
# start of a function name indicates that the function was created for
# internal use only, so unless you are adding to this specific module,
# you should never be calling this function directly
def _main_rect(*args):

	# you might have also noticed that this function (and several more
	# included below) has no type-hints and begins with a "match case"
	# statement; this is what allows this function to actually produce
	# the desired result (albeit with a warning) even if the arguments
	# have been configured incorrectly
	match args:
	
		# this case, for instance, is "matched" only when the unpacked
		# argument collection (i.e., *args) starts with a string first
		# and then a tuple of four integers next
		case str(), (int(), int(), int(), int()):
			raise_error('''INVALID_ARGS_FOR_RECT_FUNCTION_STR_TUPLE''')
			x, y, wid, hgt, clr = args[1][0], args[1][1], args[1][2], args[1][3], args[0]
			pass
		case str(), (int(), int()), int(), int():
			raise_error('''INVALID_ARGS_FOR_RECT_FUNCTION_STR_TUPLE_INT_INT''')
			x, y, wid, hgt, clr = args[1][0], args[1][1], args[2], args[3], args[0]
			pass
		case str(), int(), int(), int(), int():
			raise_error('''INVALID_ARGS_FOR_RECT_FUNCTION_STR_INT_INT_INT_INT''')
			x, y, wid, hgt, clr = args[1], args[2], args[3], args[4], args[0]
			pass
		case (int(), int(), int(), int()), str():
			raise_error('''INVALID_ARGS_FOR_RECT_FUNCTION_TUPLE_STR''')
			x, y, wid, hgt, clr = args[0][0], args[0][1], args[0][2], args[0][3], args[1]
			pass
		case (int(), int()), int(), int(), str():
			raise_error('''INVALID_ARGS_FOR_RECT_FUNCTION_TUPLE_INT_INT_STR''')
			x, y, wid, hgt, clr = args[0][0], args[0][1], args[1], args[2], args[3]
			pass
		case int(), int(), int(), int(), str():
			# raise_error('''INVALID_ARGS_FOR_RECT_FUNCTION_INT_INT_INT_INT_STR''')
			x, y, wid, hgt, clr = args[0], args[1], args[2], args[3], args[4]
			pass	
		case _:
			raise_error('''INVALID_ARGS_FOR_RECT_FUNCTION_UNRECOGNIZED''')
			exit()

	# this is where the actual turtle drawing takes place
	_init(x, y, clr)
	_goto(x + wid, y)
	_goto(x + wid, y + hgt)
	_goto(x, y + hgt)
	_goto(x, y)
	_term()

# this is the function for drawing circles
def _main_circ(*args):
	match args:
		case str(), (int(), int(), int()):
			raise_error('''INVALID_ARGS_FOR_CIRC_FUNCTION_STR_TUPLE''')
			x, y, rad, clr = args[1][0], args[1][1], args[1][2], args[0]
			pass
		case str(), (int(), int()), int():
			raise_error('''INVALID_ARGS_FOR_CIRC_FUNCTION_STR_TUPLE_INT''')
			x, y, rad, clr = args[1][0], args[1][1], args[2], args[0]
			pass
		case str(), int(), int(), int():
			raise_error('''INVALID_ARGS_FOR_CIRC_FUNCTION_STR_INT_INT_INT''')
			x, y, rad, clr = args[1], args[2], args[3], args[0]
			pass
		case (int(), int(), int()), str():
			raise_error('''INVALID_ARGS_FOR_CIRC_FUNCTION_TUPLE_STR''')
			x, y, rad, clr = args[0][0], args[0][1], args[0][2], args[1]
			pass
		case (int(), int()), int(), str():
			# raise_error('''INVALID_ARGS_FOR_CIRC_FUNCTION_TUPLE_INT_STR''')
			x, y, rad, clr = args[0][0], args[0][1], args[1], args[2]
			pass
		case int(), int(), int(), str():
			raise_error('''INVALID_ARGS_FOR_CIRC_FUNCTION_INT_INT_INT_STR''')
			x, y, rad, clr = args[0], args[1], args[2], args[3]
			pass	
		case _:
			exit()

	_init(x, y, clr)
	_turtle.forward(rad)
	_turtle.left(90)
	_turtle.circle(rad)
	_term()

# this is the function for drawing lines
def _main_line(*args):
	match args:
		case str(), (int(), int()), (int(), int()):
			# raise_error('''INVALID_ARGS_FOR_LINE_FUNCTION_STR_TUPLE_TUPLE''')
			x1, y1, x2, y2, clr = args[1][0], args[1][1], args[2][0], args[2][1], args[0]
			pass
		case (int(), int()), (int(), int()), str():
			raise_error('''INVALID_ARGS_FOR_LINE_FUNCTION_TUPLE_TUPLE_STR''')
			x1, y1, x2, y2, clr = args[0][0], args[0][1], args[1][0], args[1][1], args[2]
			pass
		case str(), int(), int(), int(), int():
			raise_error('''INVALID_ARGS_FOR_LINE_FUNCTION_STR_INT_INT_INT_INT''')
			x1, y1, x2, y2, clr = args[1], args[2], args[3], args[4], args[0]
			pass
		case int(), int(), int(), int(), str():
			raise_error('''INVALID_ARGS_FOR_LINE_FUNCTION_INT_INT_INT_INT_STR''')
			x1, y1, x2, y2, clr = args[0], args[1], args[2], args[3], args[4]
			pass
		case _:
			exit()

	_init(x1, y1, clr)
	_goto(x2, y2)
	_term()

# this is the function for drawing polygons
def _main_poly(*args):
	match args:
		case str(), list():
			raise_error('''INVALID_ARGS_FOR_POLY_FUNCTION_STR_LIST''')
			xs, ys, clr = [e[0] for e in args[1]], [e[1] for e in args[1]], args[0]
		case str(), list(), list():
			raise_error('''INVALID_ARGS_FOR_POLY_FUNCTION_STR_LIST_LIST''')
			xs, ys, clr = args[1], args[2], args[0]
		case list(), str():
			raise_error('''INVALID_ARGS_FOR_POLY_FUNCTION_LIST_STR''')
			xs, ys, clr = [e[0] for e in args[0]], [e[1] for e in args[0]], args[1]
		case list(), list(), str():
			# raise_error('''INVALID_ARGS_FOR_POLY_FUNCTION_LIST_LIST_STR''')
			xs, ys, clr = args[0], args[1], args[2]
		case _:
			exit()
		
	_init(xs[0], ys[0], clr)
	for i in range(1, len(xs)):
		_goto(xs[i], ys[i])
	_term()

# ------------------------------------------------------------------ #

# starting with this function, the remaining functions provided do not
# have names that start with an underscore and are thus not restricted
# to internal use; nevertheless, you must consult the documentation to
# see what functions are actually permitted for use in your assignment

def open_window(wid: int = 640, hgt: int = 480) -> None:
	global _window, _turtle
	_window = _logo.Screen()
	_window.setup(wid, hgt)
	_window.colormode(255)
	_window.tracer(0)
	_window.bgcolor(_palette["black"])	
	_turtle = _logo.Turtle()
	_turtle.penup()
	_turtle.hideturtle()
	_turtle.speed(0)
	_turtle.width(0)

def fill_window(clr: str) -> None:
	_window.bgcolor(_palette[clr])

def save_window() -> None:
	#_logo.getcanvas().winfo_toplevel().attributes("-zoom", 1)
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

# ------------------------------------------------------------------ #

# this is a function used in the live-coding demonstrations for drawing sectors
def demo_sector(pos: tuple[int, int], rad: int, sta: int, end: int, clr: str) -> None:
	x, y = pos[0], pos[1]
	_init(x, y, clr)
	_turtle.left(sta)
	_turtle.forward(rad)
	_turtle.left(90)
	if sta <= end:
		_turtle.circle(rad, end - sta)
	else:
		_turtle.circle(rad, 360 + end - sta)
	_goto(x, y)
	_term()

# this is a function used in the live-coding demonstrations for drawing five-pointed stars
def demo_pentalpha(pos: tuple[int, int], clr: str) -> None:
	x, y = pos[0], pos[1]
	_init(x, y, clr)
	# a few additional steps are needed to horizontally center a pentalpha...
	_turtle.setheading(90)
	_turtle.forward(0.325 * 20) # n.b., 0.3525 is approximately tan 18 degrees...
	_turtle.setheading(180)
	_turtle.forward(10)
	_turtle.setheading(0)
	for _ in range(5):
		_turtle.forward(20)
		_turtle.right(144)
	_turtle.forward(10)
	_term()

# ------------------------------------------------------------------ #

# this function prints the relevant error message on the terminal and displays something
# in the drawing window, but does not actually prevent the program from continuing
def raise_error(code: str) -> None:

	# there is a global variable that can be used to turn off error messages, but setting
	# that variable to false does *not* mean that your assignment submission won't be 
	# treated as having errors... this variable just allows instructors to conduct their
	# live coding demonstrations more easily
	if _showing_errors and code in _error_codes:
	
		# the message appears on the terminal...
		print('\n' + ('*' * 50).center(60))
		for line in wrap(_error_codes[code], 44):
			print(("* " + line.center(46) + " *").center(60))
		print(('*' * 50).center(60) + '\n')
		
		# ...and a red strikethrough line appears on the drawing
		w = _logo.window_width() - 10
		h = _logo.window_height() - 10
		_goto(4, 4)
		_turtle.color((255, 0, 0))
		_turtle.pensize(8)
		_turtle.pendown()
		_goto(w, 4)
		_goto(w, h)
		_goto(4, h)
		_goto(4, 4)
		_goto(w, h)
		_turtle.penup()
		_turtle.pensize(1)
		_term()
	
	
# ------------------------------------------------------------------ #

# these are all the function aliases, which unfortunately should be handled separately to
# facilitate error messaging to a programmer calling the wrong one	
def draw_line(*args):
	raise_error('''INVALID_FUNCTION_NAME_DRAW_LINE''')
	_main_line(*args)

def plot_line(*args):
	# raise_error('''INVALID_FUNCTION_NAME_PLOT_LINE''')
	_main_line(*args)
 
def draw_rect(*args):
	raise_error('''INVALID_FUNCTION_NAME_DRAW_RECT''')
	_main_rect(*args)

def plot_rect(*args):
	raise_error('''INVALID_FUNCTION_NAME_PLOT_RECT''')
	_main_rect(*args)
 
def draw_rectangle(*args):
	raise_error('''INVALID_FUNCTION_NAME_DRAW_RECTANGLE''')
	_main_rect(*args)

def plot_rectangle(*args):
	# raise_error('''INVALID_FUNCTION_NAME_PLOT_RECTANGLE''')
	_main_rect(*args)
 
def draw_circ(*args):
	raise_error('''INVALID_FUNCTION_NAME_DRAW_CIRC''')
	_main_circ(*args)

def plot_circ(*args):
	raise_error('''INVALID_FUNCTION_NAME_PLOT_CIRC''')
	_main_circ(*args)
 
def draw_circle(*args):
	raise_error('''INVALID_FUNCTION_NAME_DRAW_CIRCLE''')
	_main_circ(*args)

def plot_circle(*args):
	# raise_error('''INVALID_FUNCTION_NAME_PLOT_CIRCLE''')
	_main_circ(*args)
 
def draw_poly(*args):
	raise_error('''INVALID_FUNCTION_NAME_DRAW_POLY''')
	_main_poly(*args)

def plot_poly(*args):
	raise_error('''INVALID_FUNCTION_NAME_PLOT_POLY''')
	_main_poly(*args)
 
def draw_polygon(*args):
	raise_error('''INVALID_FUNCTION_NAME_DRAW_POLYGON''')
	_main_poly(*args)

def plot_polygon(*args):
	# raise_error('''INVALID_FUNCTION_NAME_PLOT_POLYGON''')
	_main_poly(*args)