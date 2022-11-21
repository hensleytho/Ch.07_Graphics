#Sign your name:_Tommy H__

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500, 400, "Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
#Vertical grid lines
for x in range(0, 501, 20):
    arcade.draw_line(x, 0, x, 500, arcade.color.BLACK, 2)
#Horizontal grid lines
for y in range(0, 401, 20):
    arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 2)
#Purple brick
arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX)
#Center circle
radius = 40
arcade.draw_circle_filled(250, 200, radius, arcade.color.WISTERIA)
#Angled brick
arcade.draw_rectangle_filled(180, 260, 40, 20, arcade.color.BLUSH, 315)
#Text
arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20)
#Amber ellipse
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
#Angled line
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
#PacMan
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 30, 330)
#Red dot
arcade.draw_rectangle_filled(460, 10, 5, 5, arcade.color.RED)
arcade.finish_render()
arcade.run()
