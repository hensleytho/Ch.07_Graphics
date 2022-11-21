import arcade
arcade.open_window(600,600,"My Drawing")
arcade.set_background_color(arcade.color.CAMBRIDGE_BLUE)

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(200,300,200,0,arcade.color.AIR_FORCE_BLUE)
arcade.draw_rectangle_filled(300,300,400,400,(60,60,60,100),45)
arcade.draw_rectangle_outline(300,300,400,400,(0,0,0),3,45)
#drawing stuff

#points/lines
arcade.draw_point(300,300,arcade.color.BLACK,3)
arcade.draw_line(100,100,500,500,(255,0,0),4)

#circles/ellipses
arcade.draw_circle_filled(300,300,50,(255,255,255),200)
arcade.draw_circle_outline(300,300,50,(0,0,0),3)
arcade.draw_ellipse_filled(400,400,100,50,arcade.color.BLUE,45)

point_list=((100,100),(120,400),(200,400),(300,150))
arcade.draw_polygon_filled(point_list,arcade.color.BRASS)

#text
arcade.draw_text("PyCasso",100,550,arcade.color.CADMIUM_RED,20)

# mypic = arcade.load_texture("python.png")
# arcade.draw_texture_rectangle(500,100,mypic.width,mypic.height,mypic,45,200)

#fence posts
for i in range(0,610,20):
    arcade.draw_rectangle_filled(i,60,10,30,arcade.color.WHITE)

#fence rails
arcade.draw_rectangle_filled(300,67,600,5,(255,255,255))
arcade.draw_rectangle_filled(300,52,600,5,(255,255,255))


radius=70
y=50
for i in range(3):
    arcade.draw_circle_filled(100,y,radius,(255,255,255))
    y=y+1.4*radius
    radius=radius*.8


arcade.finish_render()


arcade.run()