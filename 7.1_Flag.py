'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
A = 260
B = (1.9 * A)
C = (7/13) * A
D = round(0.76 * A)
E = (0.054 * A)
F = (0.054 * A)
G = (0.063 * A)
H = (0.063 * A)
K = (0.0616 * A)
L = round((1/13) * A)
arcade.open_window(B, A, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for y in range(10, A, L*2): #Red lines
    arcade.draw_line(0, y, 2*A, y, (180, 10, 45), L)
arcade.draw_rectangle_filled(D/2, A-(C/2), D, C, (0, 40, 98)) #Blue rectangle

for star in range(round(H*3),D,round(H*2)):arcade.draw_text("*",star-(A/10),D+(A/20),(255,255,255),H*1.5)
for star in range(round(H*3),D,round(H*2)):arcade.draw_text("*",star-(A/10),D-(A/20),(255,255,255),H*1.5)
for star in range(round(H*3),D,round(H*2)):arcade.draw_text("*",star-(A/10),D-3*(A/20),(255,255,255),H*1.5)
for star in range(round(H*3),D,round(H*2)):arcade.draw_text("*",star-(A/10),D-5*(A/20),(255,255,255),H*1.5)

for star in range (round(H/2),D,round(H*2)):arcade.draw_text("*",star,D+(A/10),(255,255,255),H*1.5)
for star in range (round(H/2),D,round(H*2)):arcade.draw_text("*",star,D,(255,255,255),H*1.5)
for star in range (round(H/2),D,round(H*2)):arcade.draw_text("*",star,D-(A/10),(255,255,255),H*1.5)
for star in range (round(H/2),D,round(H*2)):arcade.draw_text("*",star,D-2*(A/10),(255,255,255),H*1.5)
for star in range (round(H/2),D,round(H*2)):arcade.draw_text("*",star,D-3*(A/10),(255,255,255),H*1.5)







# for s in range(round(H), D, round(H*2)):
#     arcade.draw_text("*", s, D+(A/12), (255, 255, 255), H*1.5)
#     arcade.draw_text("*", s, D, (255, 255, 255), H * 1.5)
#     arcade.draw_text("*", s, D - (A / 10), (255, 255, 255), H * 1.5)
#     arcade.draw_text("*", s, D - 2 * (A / 10), (255, 255, 255), H * 1.5)
#     arcade.draw_text("*", s, D - 3 * (A / 10), (255, 255, 255), H * 1.5)
# for s in range(round(H), D, round(H*2)):
#     arcade.draw_text("*", s - (A/10), D + (A/20), (255, 255, 255), H*1.5)
#     arcade.draw_text("*", s - (A/10), D - (A/20), (255, 255, 255), H*1.5)
#     arcade.draw_text("*", s - (A/10), D - 3 * (A / 20), (255, 255, 255), H * 1.5)
#     arcade.draw_text("*", s - (A/15), D - 5 * (A / 20), (255, 255, 255), H * 1.5)
# arcade.finish_render()
arcade.run()
# for s in range(round(H), D, round(H*2)):
#     arcade.draw_text("*", s, D+(A/10), (255, 255, 255), H*1.5)
#     arcade.draw_text("*", s, D, (255, 255, 255), H * 1.5)
#     arcade.draw_text("*", s, D - (A / 10), (255, 255, 255), H * 1.5)
#     arcade.draw_text("*", s, D - 2 * (A / 10), (255, 255, 255), H * 1.5)
#     arcade.draw_text("*", s, D - 3 * (A / 10), (255, 255, 255), H * 1.5)
# for s in range(round(H), D, round(H*2)):
#     arcade.draw_text("*", s - (A/10), D + (A/20), (255, 255, 255), H*1.5)
#     arcade.draw_text("*", s - (A/10), D - (A/20), (255, 255, 255), H*1.5)
#     arcade.draw_text("*", s - (A/10), D - 3 * (A / 20), (255, 255, 255), H * 1.5)
#     arcade.draw_text("*", s - (A/15), D - 5 * (A / 20), (255, 255, 255), H * 1.5)


# x = D/5 + A
# while x >= D-5*(A/20):
#     for s in range(round(H/2), D, round(H*2)):
#         arcade.draw_text("*", s, x, (255, 255, 255), H*1.5)
#         x -= (A/20)
#     for s in range(round(H*3), D, round(H*2)):
#         arcade.draw_text("*", s - (A/10), x, (255, 255, 255), H*1.5)
#         x -= (A/20)
#     for s in range(round(H/2), D, round(H*2)):
#         arcade.draw_text("*", s, x, (255, 255, 255), H*1.5)