from .Base import Base
from .CGMESProfile import Profile


class SvPowerFlow(Base):
    """
    State variable for power flow. Load convention is used for flow direction. This means flow out from the TopologicalNode into the equipment is positive.

    :Terminal: The terminal associated with the power flow state variable. Default: None
    :p: The active power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. Default: 0.0
    :q: The reactive power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.SV.value, ],
        "Terminal": [Profile.SV.value, ],
        "p": [Profile.SV.value, ],
        "q": [Profile.SV.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SV.value


    def __init__(self, Terminal = None, p = 0.0, q = 0.0):

        self.Terminal = Terminal
        self.p = p
        self.q = q

    def __str__(self):
        str = "class=SvPowerFlow\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
