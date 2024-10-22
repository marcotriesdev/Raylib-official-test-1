from raylibpy import *

class Sprite:

    def __init__(self, textures, position, velocity, global_scale = 1, global_gravity = 0, hp = 0, isplayer = False):

        self.textures = textures
        self.texture = load_texture(textures[0])
        self.position = position
        self.velocity = velocity
        self.normalvelocity = self.velocity
        self.bbox = Rectangle(position.x, position.y, self.texture.width*global_scale, self.texture.height*global_scale)
        
        self.isplayer = isplayer
        self.colliding = False
        self.onfloor = False
        self.gravity = global_gravity
        self.scale = global_scale
        self.bbox_color = Color(255,255,255,0)
        self.hp = hp
        self.hurt = False

        self.state = "idle"
        self.stamina = 50


    def update_state(self):

        match self.state:
            case "idle":
                self.velocity = self.normalvelocity
                self.texture = load_texture(self.textures[0])
            case "attack":
                self.velocity *= 0.6
                self.texture = load_texture(self.textures[1])


    def actions(self):

        if self.isplayer:
            if is_key_down(KEY_SPACE) and self.stamina > 0:
                self.state = "attack"
                self.stamina -= 2
            else:
                self.state = "idle"


    def update_bbox(self):

        self.bbox = Rectangle(self.position.x, self.position.y,
                        self.texture.width*self.scale, 
                        self.texture.height*self.scale)


    def stamina_limit(self):

        if self.stamina < 0:
            self.stamina = 0


    def update(self):

        self.actions()
        self.update_state()
        self.update_bbox()
        self.stamina_limit()

        self.position += self.velocity

        if not self.colliding:
            self.position.y += self.gravity


    def draw(self):

        if self.colliding:
            self.bbox_color = Color(255,0,0,100) #transparent red
        else:
            self.bbox_color = Color(255,255,255,100) #transparent white

        draw_texture_ex(self.texture,self.position,0,self.scale,WHITE)

    def unload(self):

        unload_texture(self.texture)

class Spritegroup:

    def __init__(self, type = 0):

        self.sprites = []  # List to store sprite instances
        self.type = type

    def add(self,elements):

        for element in elements:
            self.sprites.append(element)


    def update(self):

        for sprite in self.sprites:
            sprite.update()
        

    def draw(self):

        for sprite in self.sprites:
            sprite.draw()

    def draw_bbox(self):

        for sprite in self.sprites:
            draw_rectangle_rec(sprite.bbox,sprite.bbox_color)

    def unload(self):

        for sprite in self.sprites:
            sprite.unload()

    def check_collisions(self,other_group):

        for sprite in self.sprites:
            for othersprite in other_group.sprites:
                if check_collision_recs(sprite.bbox,othersprite.bbox):
                    sprite.colliding, othersprite.colliding = True, True
                    return True
                else:
                    sprite.colliding, othersprite.colliding = False, False
                    return False

class Controller:

    def __init__(self):

        self.active = True
    
    def input(self,velocity,player_speed,onfloor,jump_speed):

        velocity.x, velocity.y = 0, 0
        if is_key_down(KEY_W):
            if onfloor:
                velocity.y = -jump_speed  # Mover hacia arriba
        if is_key_down(KEY_S):
            if not onfloor:
                velocity.y += player_speed  # Mover hacia abajo
        if is_key_down(KEY_A):
            velocity.x = -player_speed  # Mover hacia la izquierda
        if is_key_down(KEY_D):
            velocity.x = player_speed
        


        print(velocity)
        return velocity