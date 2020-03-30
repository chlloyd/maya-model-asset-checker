# Misc Node Checks
import maya.cmds as cmds


def contents_of_scene():  # checks for any addition nodes within the scene that shouldn't be there. e.g. lighting
    basic_nodes = []
    all_in_scene = cmds.ls()
    for node in all_in_scene:
        # check if its in basic nodes, if it is, move on
        # check if its within self.selected
        # return all that should be in the scene
        pass


def unknown_nodes_check():
    unknown_nodes_list = []
    for nodes in cmds.ls(selection=True):
        if cmds.objectType == "unknown":
            unknown_nodes_list.append(nodes)
    return unknown_nodes_list
