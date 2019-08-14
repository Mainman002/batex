import bpy
from . bex_utils import *

class BatEx_Export:

  def __init__(self, context):
    self.__context = context
    self.__export_folder = context.scene.export_folder
    self.__export_applyTransform = context.scene.apply_transform
    self.__export_applyModifiers = context.scene.apply_modifiers
    #self.__export_includeTextures = context.scene.include_textures     ### Doesn't seem to do anything ###
    self.__export_exportScale = context.scene.export_scale
    self.__center_transform = context.scene.center_transform
    self.__export_objects = context.selected_objects
  
  def do_center(self, obj):
    if self.__center_transform:
      loc = get_object_loc(obj)
      set_object_to_loc(obj, (0,0,0))
      return loc

    return None

  def do_export(self):

    bpy.ops.object.mode_set(mode='OBJECT')

    for obj in self.__export_objects:
      bpy.ops.object.select_all(action='DESELECT') 
      obj.select_set(state=True)

      # Center selected object
      old_pos = self.do_center(obj)

      # Select children if exist
      for child in get_children(obj):
        child.select_set(state=True)

      # Export the selected object as fbx
      # TODO: Expose mode properties
      bpy.ops.export_scene.fbx(check_existing=False,
      filepath=self.__export_folder + "/" + obj.name + ".fbx",
      filter_glob="*.fbx",
      use_selection=True,
      use_armature_deform_only=True,
      mesh_smooth_type=self.__context.scene.export_smoothing,
      add_leaf_bones=False,
      global_scale=self.__export_exportScale,
      bake_space_transform=self.__export_applyTransform,
      use_mesh_modifiers=self.__export_applyModifiers,
      #embed_textures=self.__export_includeTextures,    ### Doesn't seem to do anything ###
      path_mode='ABSOLUTE')

      if old_pos is not None:
        set_object_to_loc(obj, old_pos)