from raylibpy import  *
from classes import *

w_width, w_height = 800, 640
global_scale = 4.0
global_gravity = 0.9

init_window(w_width, w_height,"Raylib - Test 1.0")

player_texture = "assets/sprites/player.png"
square_texture = "assets/sprites/square.png"


player = Sprite(player_texture,Vector2(264,100),Vector2(0,0),global_scale,global_gravity)
square = Sprite(square_texture,Vector2(264,256),Vector2(0,0),global_scale)

playergroup = Spritegroup()
squaregroup = Spritegroup()

playergroup.add(player)
squaregroup.add(square)

set_target_fps(60)

while not window_should_close():

    begin_drawing()
    clear_background(BLACK)
    draw_text("Rip Off Knight", 20, 20, 30, Color(255,0,0,255))

    
    squaregroup.draw()
    playergroup.draw()

    playergroup.update()
    playergroup.check_collisions(squaregroup)

    #playergroup.draw_bbox()
    #squaregroup.draw_bbox()

    end_drawing()

playergroup.unload()
close_window()


