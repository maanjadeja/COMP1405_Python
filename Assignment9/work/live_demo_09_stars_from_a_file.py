import special_library_easy_graphics
import random

def main():

	# open a window 500 pixels high and 500 pixels wide and fill with the colour midnight
	special_library_easy_graphics.open_window(500, 500)
	special_library_easy_graphics.fill_window("midnight")

	# open a file "handle" in r+ mode (allowing for both reading and appending)
	file_hndl = open("live_demo_09_sample_file.txt", "r+")
	
	# use a postcondition loop (implemented with a break) to read the file, one line at a time,
	# "until" the line that was most recently read ends up being empty
	while True:
	
		file_data = file_hndl.readline()
		
		if file_data == "":
			break
		
		# this method will split the comma-separated string into two strings...
		file_data = file_data.split(",")

		# ...which can then be converted to integers and used as x and y co-ordinates
		special_library_easy_graphics.demo_pentalpha((int(file_data[0]), int(file_data[1])), "orange")

	# I can also write a new pair of x and y co-ordinates to the open file handle, so that there
	# will be a new (randomly positioned) star appearing every time the program is executed
	file_hndl.write(f"\n{random.randint(0, 500)},{random.randint(0, 500)}")
	
	# it is always good practice to close your file handles when they are no longer needed
	file_hndl.close()
	
	# the window will close when the program ends, so we need to call a
	# function to keep the window open until the close button is clicked
	special_library_easy_graphics.keep_window()


main()