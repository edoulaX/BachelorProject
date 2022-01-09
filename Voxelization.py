import numpy as np
import open3d as o3d
import os

directory = r"/home/edou/Documents/epfl/ba5/Project/Point_Clouds"

for file in os.listdir(directory): 
    pcd = o3d.io.read_point_cloud(directory + '/' + file)
    max = np.amax(np.asarray(pcd.points))
    scale = 512/max
    pcd.scale(scale, center=pcd.get_center())
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=1)

    path = directory + '/' + file
    o3d.io.write_voxel_grid(path, voxel_grid)
    
