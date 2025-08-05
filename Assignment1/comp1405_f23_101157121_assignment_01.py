#Name: Maansinh Jadeja
#Student Number: 101157121
import comp1405_f23_special_library_easy_graphics_for_101157121

def main():
    #open the 500x500 window
    comp1405_f23_special_library_easy_graphics_for_101157121.open_window(600,600)
    #background colour of window
    comp1405_f23_special_library_easy_graphics_for_101157121.fill_window("white")
    # comp1405_f23_special_library_easy_graphics_for_101157121.insert_grid(50)

    #draw the circle
    comp1405_f23_special_library_easy_graphics_for_101157121.plot_circle(300,300,300,"moss")

    #draw the rectangle section
    comp1405_f23_special_library_easy_graphics_for_101157121.plot_rectangle(180,75,120,75,"port")
    #draw the triangle section
    comp1405_f23_special_library_easy_graphics_for_101157121.plot_polygon([300,360,300],[75,75,150],"port")

    #draw the rectangle section
    comp1405_f23_special_library_easy_graphics_for_101157121.plot_rectangle(240,450,120,75,"midnight")
    comp1405_f23_special_library_easy_graphics_for_101157121.plot_rectangle(360,375,60,75,"midnight")
    #draw the triangle section
    comp1405_f23_special_library_easy_graphics_for_101157121.plot_polygon([360,420,360],[450,450,525],"midnight")


	#keep window open
    comp1405_f23_special_library_easy_graphics_for_101157121.keep_window()


main()