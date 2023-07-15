from gl import Renderer, V2,V3, color
import random, shaders
width = 7000
height = 10000

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

rend.glLoadModel("face.obj", translate=(width/6, height/4, 0), scale=(1500,1500,1500))

""" verts = [V3(0,0,0),
        V3(50,0,0),
        V3(25,40,0)]

rend.glAddVertices(verts)
rend.glModelMatrix(translate=(width/2, height/2, 0),
                   scale=(5,3,1)) """
rend.glRender()

rend.glFinish("output.bmp") 