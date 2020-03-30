# UV Maps Checks
def uv_zero_map_check(self):  # Faces with zero Map Area
    # get list of all uv faces in scene
    # for loop
    # cmds.polyUVCoverage()
    # find if any are 0
    pass


def uv_space_percentage(self):  # returns percentage of uv space used. More is best
    shader_dict = {}
    geo_list = []

    for shader in cmds.ls(type="aiStandardSurface"):
        for shaderGroup in cmds.listConnections(shader):
            if cmds.objectType(ShaderGroup) == "shadingEngine":
                for connectedNode in cmds.listConnections(y):
                    if cmds.objectType(connectedNode) == "transform":
                        geo = connectedNode
                        geo_list.append(geo)
        shader_dict[shader] = geo_list

        print(cmds.polyUVCoverage(cmds.ls(selection=True)))
    return cmds.polyLayoutUV(self.selected, percentageSpace=True)