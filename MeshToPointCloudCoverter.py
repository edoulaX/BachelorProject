import pymeshlab
import os
ms = pymeshlab.MeshSet()
sampleNum = 1000000
directory = r"C:\Users\edoul\Documents\ba5\Project\Meshes"
resultPath = r"C:\Users\edoul\Documents\ba5\Project\result"
meshes = []

for file in os.listdir(directory): #peut etre un bug avec le b
    if not '.html' in file and '.obj' in file:
        meshes.append(file)

for name in meshes:
    ms.load_new_mesh(directory + '\\' + name)
    ms.point_cloud_simplification(samplenum = sampleNum)   #convert the mesh in a point cloud
    ms.save_current_mesh(resultPath + '\\' + name + '.ply')
