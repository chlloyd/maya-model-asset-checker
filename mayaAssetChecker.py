import os
import sys
import maya.cmds as cmds

sys.path.append("C:\\Users\\Chris\\Documents\\Programming Projects\\maya-model-asset-checker")

import assetchecks

# current_path = os.path.dirname(os.path.realpath(__builtin__))
height = 800
width = 300


class MayaAssetChecker:
    def __init__(self):
        self.window = "maya_asset_checker"
        self.title = "Model Asset Checker"
        self.size = (height, width)
        self.selected = cmds.ls(selection=True)

    def buildUI(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
            cmds.windowPref(self.window, remove=True)

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.formLayout(numberOfDivisions=100)
        cmds.rowColumnLayout(width=width)
        cmds.text(
            "This tool will check for problems with the following aspects of an \nasset:",
            align='center')
        cmds.text("- Geometry,\n - Images,\n - Shaders", align="left")
        cmds.text("Select the geometry to test and press run below")
        cmds.button(label="Run", command=self.check_all_errors)

        cmds.showWindow()

        def check_all_errors():
            # runs test
            # opens new window with feedback
            pass

class MayaAssetFeedback:
    def __init__(self):
        self.window = "maya_asset_feedback"
        self.title = "Model Asset Feedback"
        self.size = (height, width)

    def buildUI(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
            cmds.windowPref(self.window, remove=True)


    ####################################################################################################################
    # ERROR LIST CONSTRUCTORS
    ####################################################################################################################
    def list_to_bullet_points(self):
        pass

    def build_error_list(self):
        pass

    ####################################################################################################################
    # ERROR CHECKING FUNCTIONS
    ####################################################################################################################
    def check_all_errors(self, *args):
        pass
        # geometryChecks.
        # imageChecks.
        #miscChecks.contents_of_scene()
        #miscChecks.unknown_nodes_check()
        # shaderChecks.
        # uvChecks.


AssetChecker = MayaAssetChecker()
AssetChecker.buildUI()
