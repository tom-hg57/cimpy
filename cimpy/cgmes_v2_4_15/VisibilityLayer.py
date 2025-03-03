from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class VisibilityLayer(IdentifiedObject):
    """
    Layers are typically used for grouping diagram objects according to themes and scales. Themes are used to display or hide certain information (e.g., lakes, borders), while scales are used for hiding or displaying information depending on the current zoom level (hide text when it is too small to be read, or when it exceeds the screen size). This is also called de-cluttering.  CIM based graphics exchange will support an m:n relationship between diagram objects and layers. It will be the task of the importing system to convert an m:n case into an appropriate 1:n representation if the importing system does not support m:n.

    :VisibleObjects: A visibility layer can contain one or more diagram objects. Default: "list"
    :drawingOrder: The drawing order for this layer.  The higher the number, the later the layer and the objects within it are rendered. Default: 0
    """

    possibleProfileList = {
        "class": [Profile.DL.value, ],
        "VisibleObjects": [Profile.DL.value, ],
        "drawingOrder": [Profile.DL.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DL.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, VisibleObjects = "list", drawingOrder = 0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.VisibleObjects = VisibleObjects
        self.drawingOrder = drawingOrder

    def __str__(self):
        str = "class=VisibilityLayer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
