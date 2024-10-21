from raylibpy import *

class Sprite:

    def __init__(self, texture, position, speed, global_scale = 1, global_gravity = 0):

        self.texture = load_texture(texture)
        self.position = position
        self.speed = speed
        self.bbox = Rectangle(position.x, position.y, self.texture.width*global_scale, self.texture.height*global_scale)
        self.colliding = False
        self.gravity = global_gravity
        self.scale = global_scale
        self.bbox_color = Color(255,255,255,0)

    def update(self):

        self.bbox.x = self.position.x
        self.bbox.y = self.position.y

        self.position += self.speed

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

    def __init__(self):

        self.sprites = []  # List to store sprite instances

    def add(self,sprite):

        self.sprites.append(sprite)


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
                else:
                    sprite.colliding, othersprite.colliding = False, False
