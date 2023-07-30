from gl import Renderer, V2,V3, color
import random, shaders
width = 1500
height = 1500

rend = Renderer(width, height)

rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.fragmentShader

#Right: -90,0,90
#Back: -90,0,0
#Front: -90,0,-180
#Left: -90,0,-90
rend.glLoadModel(filename="skull.obj", 
                 textureName="Texture.bmp", 
                 translate=(width/4, height/2, 0), 
                 scale=(23,23,23), 
                 rotate=(-90,0,-180))

rend.glLoadModel(filename="skull.obj", 
                 textureName="Texture.bmp", 
                 translate=(width-(width/4), height/2, 0), 
                 scale=(23,23,23), 
                 rotate=(-90,0,0))

rend.glLoadModel(filename="skull.obj", 
                 textureName="Texture.bmp", 
                 translate=(width/4, height/32, 0), 
                 scale=(23,23,23), 
                 rotate=(-90,0,-90))

rend.glLoadModel(filename="skull.obj", 
                 textureName="Texture.bmp", 
                 translate=(width-(width/4), height/32, 0), 
                 scale=(23,23,23), 
                 rotate=(-90,0,90))

rend.glRender() 

rend.glFinish("Test.bmp") 