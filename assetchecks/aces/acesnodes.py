import maya.cmds as cmds


def list_all_file_nodes_in_scene():
    """Lists all file nodes within the scene.

    Returns: A list of all file nodes in the scene

    """
    return cmds.ls(type="file")


def colour_space_check():  # check for correct colour space on file nodes

    for filenode in list_all_file_nodes_in_scene():
        if cmds.getAttr(filenode + ".colorSpace") != "" or cmds.getAttr(filenode + ".colorSpace") != "":
            pass
            # add to list


def alpha_is_luminance_check():  # check for alpha is luminance on metalness/metallic and roughness
    for file in list_all_file_nodes_in_scene():
        #if cmds.getAttr(filenode + "")
        pass