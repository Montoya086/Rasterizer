from gl import Renderer, V2,V3, color
import random, shaders
width = 1920
height = 1080

rend = Renderer(width, height)

# for x in range(width):
#     for y in range(height):
#         rend.glPoint(x,y, color(random.random(),random.random(),random.random()))


""" for x in range(width):
    for y in range(height):
        if random.random()>0.995:
            size = random.randrange(0,3)
            brightness = random.random()/2+0.5

            starColor = color(brightness,brightness,brightness)

            if(size==0):
                rend.glPoint(x,y,starColor)
            if size ==1: 
                rend.glPoint(x,y,starColor)
                rend.glPoint(x+1,y,starColor)
                rend.glPoint(x,y+1,starColor)
                rend.glPoint(x+1,y+1,starColor)
            elif size ==2:
                rend.glPoint(x,y,starColor)
                rend.glPoint(x,y+1,starColor)
                rend.glPoint(x,y-1,starColor)
                rend.glPoint(x+1,y,starColor)
                rend.glPoint(x-1,y,starColor)
"""

rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.fragmentShader

#Right: -90,0,90
#Front: -90,0,0
#Left: -90,0,-90
rend.glLoadModel("skull.obj", translate=(width/2, height/8, 0), scale=(30,30,30), rotate=(-90,0,90))

""" verts = [V3(0,0,0),
        V3(50,0,0),
        V3(25,40,0)]

rend.glAddVertices(verts)
rend.glModelMatrix(translate=(width/2, height/2, 0),
                   scale=(5,3,1)) """
rend.glRender()

rend.glFinish("Right.bmp") 