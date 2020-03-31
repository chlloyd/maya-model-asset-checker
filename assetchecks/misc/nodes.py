# Misc Node Checks
import os
import maya.cmds as cmds
from assetchecks.aces.acesnodes import list_all_file_nodes_in_scene


def contents_of_scene():  # checks for any addition nodes within the scene that shouldn't be there. e.g. lighting
    basic_nodes = []
    all_in_scene = cmds.ls()
    for node in all_in_scene:
        # check if its in basic nodes, if it is, move on
        # check if its within self.selected
        # return all that should be in the scene
        pass


def unknown_nodes_check():
    """ Checks for unknown nodes within the scene.

    Returns: A list of unknown nodes in the scene.

    """
    unknown_nodes_list = []
    for nodes in cmds.ls(selection=True):
        if cmds.objectType == "unknown":
            unknown_nodes_list.append(nodes)
    return unknown_nodes_list


def relative_paths_check():
    """Checks the file nodes within the scenes texture paths

    Returns: a list of all file nodes without relative paths

    """
    textures_with_wrong_path = []
    maya_project_folder = cmds.workspace(q=True, dir=True)
    for filenode in list_all_file_nodes_in_scene():
        texture_path = cmds.getAttr(filenode+".FileTextureName")
        if texture_path.startwith(maya_project_folder) is False:
            textures_with_wrong_path.append(filenode)
    return textures_with_wrong_path


def broken_path_check():
    """ Checks the file nodes within the scene paths are not broken.

    Returns: A list of file nodes with broken texture paths.

    """
    broken_path_list = []
    for filenode in list_all_file_nodes_in_scene():
        texture_path = cmds.getAttr(filenode + ".FileTextureName")
        if not os.path.exists(texture_path):
            broken_path_list.append(filenode)
    return broken_path_check()
