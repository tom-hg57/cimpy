from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class BusNameMarker(IdentifiedObject):
    """
    Used to apply user standard names to topology buses. Typically used for "bus/branch" case generation. Associated with one or more terminals that are normally connected with the bus name.    The associated terminals are normally connected by non-retained switches. For a ring bus station configuration, all busbar terminals in the ring are typically associated.   For a breaker and a half scheme, both busbars would normally be associated.  For a ring bus, all busbars would normally be associated.  For a "straight" busbar configuration, normally only the main terminal at the busbar would be associated.

    :ReportingGroup: The bus name markers that belong to this reporting group. Default: None
    :Terminal: The terminals associated with this bus name marker. Default: "list"
    :priority: Priority of bus name marker for use as topology bus name.  Use 0 for don t care.  Use 1 for highest priority.  Use 2 as priority is less than 1 and so on. Default: 0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "ReportingGroup": [Profile.EQ.value, ],
        "Terminal": [Profile.EQ.value, ],
        "priority": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, ReportingGroup = None, Terminal = "list", priority = 0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ReportingGroup = ReportingGroup
        self.Terminal = Terminal
        self.priority = priority

    def __str__(self):
        str = "class=BusNameMarker\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
