'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
arcade.open_window(600, 400, "Tommy Hensley, Pycasso")
arcade.set_background_color(arcade.color.LIGHT_PINK)
arcade.start_render()
for y in range(0, 900, 50):
    arcade.draw_line(0, y, 800, y, arcade.color.LIGHT_BLUE, 15)
for x in range(0, 800, 20):
    arcade.draw_line(x, 0, x, 800, arcade.color.LIGHT_GREEN, 10)
arcade.draw_circle_filled(150, 200, 165, (255, 255, 255))
arcade.draw_circle_filled(450, 200, 165, (255, 255, 255))
arcade.draw_circle_outline(150, 200, 175, (0, 0, 0), 10)
arcade.draw_circle_outline(450, 200, 175, (0, 0, 0), 10)
arcade.draw_circle_filled(80, 290, 60, (0, 0, 0,))
arcade.draw_circle_filled(525, 115, 60, (0, 0, 0,))

x=0
while x <= 650:
    arcade.draw_line(x+120, 363, x+95, 460, arcade.color.BLACK, 15,)
    arcade.draw_line(x+150, 365, x+150, 420, arcade.color.BLACK, 15,)
    arcade.draw_line(x+180, 363, x+215, 460, arcade.color.BLACK, 15,)
    x += 300

for x in range(0, 800, 5):
    arcade.draw_line(x, 0, x, 800, arcade.color.LIGHT_PINK, 2)
arcade.finish_render()
arcade.run()

# arcade.draw_circle_outline(0, 200, 150, (0, 0, 0), 10)
# arcade.draw_circle_outline(0, 200, 125, (0, 0, 0), 10)
# arcade.draw_circle_outline(150, 200, 200, (0, 0, 0), 10)
# arcade.draw_circle_outline(150, 200, 175, (0, 0, 0), 10)
# arcade.draw_circle_outline(450, 200, 200, (0, 0, 0), 10)
# arcade.draw_circle_outline(450, 200, 175, (0, 0, 0), 10)
# arcade.draw_circle_outline(600, 200, 150, (0, 0, 0), 10)
# arcade.draw_circle_outline(600, 200, 125, (0, 0, 0), 10)