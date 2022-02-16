import arcade


def main():
    #syntax error - forgot colon
    #create a new window to draw on
    arcade.open_window(1000, 1000, "picture")
    #set background color
    arcade.set_background_color(arcade.color.ASH_GREY)

    #creating the shapes
    body = []
    sponge = body.append(arcade.create_rectangle(500, 500, 250, 300, arcade.color.YELLOW))



    #draw the shapes
    arcade.start_render()
   #draw everything in body
    for _whole_picture in body:
        _whole_picture.draw()

    arcade.finish_render()




    #error-wasn't staying open
    arcade.run()


main()