bl_info = {
    "name" : "Batex",
    "author" : "jayanam",
    "descrtion" : "Batch export as Fbx",
    "blender" : (2, 80, 0),
    "version" : (0, 3, 1, 1),
    "location" : "Batex panel",
    "warning" : "",
    "category" : "Import-Export"
}

import bpy
from bpy.props import *

from . bex_panel import *
from . bex_op import *
from . bex_folder_op import *

bpy.types.Scene.export_folder = StringProperty(name="Export folder", 
               subtype="DIR_PATH", 
               description="Directory to export the fbx files into")

bpy.types.Scene.center_transform = BoolProperty(name="Center transform",
                default=True,
                description="Set the pivot point of the object to the center")

bpy.types.Scene.apply_transform = BoolProperty(name="Apply transform",
                default=True,
                description="Applies experimental scale and transforms")

bpy.types.Scene.apply_modifiers = BoolProperty(name="Apply modifiers",
                default=True,
                description="Applies modifiers")

#bpy.types.Scene.include_textures = BoolProperty(name="Include textures",     ### Doesn't seem to do anything ###
                #default=False,
                #description="Inludes textures into the fbx file")

bpy.types.Scene.export_scale = FloatProperty(name="Export scale",
                default=1.0,
                min=0.01,
                max=10.0,
                description="Sets the exported model scale")

bpy.types.Scene.export_smoothing = EnumProperty(
    name="Smoothing",
    description="Defines the export smoothing information",
    items=(
        ('EDGE', 'Edge', 'Write edge smoothing',0),
        ('FACE', 'Face', 'Write face smoothing',1),
        ('OFF', 'Normals Only', 'Write normals only',2)
        ),
    default='OFF'
    )

classes = ( BatEx_PT_Panel, BatEx_OT_Operator, BatEx_OT_OpenFolder )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
