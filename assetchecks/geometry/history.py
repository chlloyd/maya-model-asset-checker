import maya.cmds as cmds


def construction_history_check():
    """ Checks to see if there is construction history on the selected object.

    Returns: True if construction history exists, or False if not.

    """
    if len(cmds.listhistory(cmds.ls(selection=True))) > 2:
        return True
    else:
        return False
