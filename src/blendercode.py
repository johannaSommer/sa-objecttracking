# CODE COLLECTION TO LATER MIX TOGETHER FOR ACTUAL WORKING BLENDER CODE

# snippet to move existing object in a few frames
import bpy
positions = (0,3,1),(0,5,2),(0,6,1)
start_pos = (0,0,0)

ob = bpy.data.objects["Sphere"]

frame_num = 0

for position in positions:
    bpy.context.scene.frame_set(frame_num)
    ob.location = position
    ob.keyframe_insert(data_path="location", index=-1)
    frame_num =+ 20


# snippet to create a sphere
import bpy
import bmesh

bpyscene = bpy.context.scene

mesh = bpy.data.meshes.new('Basic_Sphere')
basic_sphere = bpy.data.objects.new("Basic_Sphere", mesh)

bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True

bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()

# snippet to completely delete a sphere
import bpy

bpy.ops.object.select_all(action='DESELECT')

bpy.data.objects['Camera'].select_set(True)

bpy.ops.object.delete()
