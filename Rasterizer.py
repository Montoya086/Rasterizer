from gl import Renderer, V2,V3, color
import random, shaders
width = 1920
height = 1080

rend = Renderer(width, height)

rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.fragmentShader

#Right: -90,0,90
#Front: -90,0,0
#Left: -90,0,-90
rend.glLoadModel("skull.obj", translate=(width/2, height/8, 0), scale=(30,30,30), rotate=(-90,0,90))

rend.glRender()

rend.glFinish("Right.bmp") 