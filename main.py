from raylibpy import  *
from classes import *

#COMENTARIO PARA GIT
#COMENTARIO PARA CAMBIO PERMANENTE

w_width, w_height = 800, 640
global_scale = 4.0
global_gravity = 5
player_speed = 3
jump_speed = 50

set_trace_log_level(LOG_NONE)
init_window(w_width, w_height,"Raylib - Test 1.0")

player_texture = ["assets/sprites/player.png", 
                  "assets/sprites/player_attack.png"]
square_texture = ["assets/sprites/square.png"]
enemy_texture = ["assets/sprites/enemy.png"]

control = Controller()


square  = Sprite(square_texture,Vector2(264,256),Vector2(0,0),global_scale)
square2 = Sprite(square_texture,Vector2(380,256),Vector2(0,0),global_scale)
square3 = Sprite(square_texture,Vector2(480,256),Vector2(0,0),global_scale)


player = Sprite(player_texture,Vector2(480,100),Vector2(0,0),global_scale,global_gravity,10,True)
enemy = Sprite(enemy_texture,Vector2(370,100),Vector2(0,0),global_scale,global_gravity, 1)

playergroup = Spritegroup()
squaregroup = Spritegroup()
enemygroup = Spritegroup()

playergroup.add(player)

squaregroup.add(square)
squaregroup.add(square2)
squaregroup.add(square3)

enemygroup.add(enemy)


set_target_fps(60)

while not window_should_close():

    begin_drawing()
    clear_background(BLACK)
    draw_text("Rip Off Knight", 20, 20, 30, Color(255,0,0,255))
    draw_text(f"HP: {player.hp}", 20, 50, 30, Color(255,0,50,255))
    draw_text(f"SP: {player.stamina}", 20, 80, 25, Color(15,150,10,255))
    draw_text(f"floor: {player.onfloor} ", player.position.x, 120, 20, Color(15,150,10,155))
    draw_text(f"player collide: {player.colliding} ", player.position.x, 140, 15, Color(15,150,10,155))

    ypos = 160
    for sq in squaregroup.sprites:
        ypos += 15 
        draw_text(f"square collide: {sq.colliding} ", sq.position.x, ypos, 15, Color(15,150,10,155))
        draw_text(f"square collide: {sq.position.x} ", sq.position.x, ypos+10, 15, Color(15,150,10,155))




    player.velocity = control.input(player.velocity,player_speed,player.onfloor,jump_speed)

    playergroup.update(squaregroup)
    enemygroup.update(playergroup) 
    squaregroup.update(playergroup)

    player.onfloor = player.colliding

    if playergroup.check_collisions(enemygroup) and player.hurt == False:
        if player.hp > 0 and player.state is not "attack":
            player.hp -= 1 
            player.hurt = True

    elif  not playergroup.check_collisions(enemygroup) and player.hurt == True:
        player.hurt = False



    playergroup.draw()
    enemygroup.draw()
    squaregroup.draw() 

    #METER ESTO EN UN OBJETO DE DEBUG
    playergroup.draw_bbox()
    squaregroup.draw_bbox()

    end_drawing()

playergroup.unload()
enemygroup.unload()
squaregroup.unload()
close_window()


