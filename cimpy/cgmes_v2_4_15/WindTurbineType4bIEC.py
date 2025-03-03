from .WindGenType4IEC import WindGenType4IEC
from .CGMESProfile import Profile


class WindTurbineType4bIEC(WindGenType4IEC):
    """
    Wind turbine IEC Type 4A.  Reference: IEC Standard 61400-27-1, section 6.5.5.3.

    :WindContPType4bIEC: Wind control P type 4B model associated with this wind turbine type 4B model. Default: None
    :WindMechIEC: Wind mechanical model associated with this wind turbine Type 4B model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindContPType4bIEC": [Profile.DY.value, ],
        "WindMechIEC": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class WindGenType4IEC:\n" + WindGenType4IEC.__doc__

    def __init__(self, WindContPType4bIEC = None, WindMechIEC = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindContPType4bIEC = WindContPType4bIEC
        self.WindMechIEC = WindMechIEC

    def __str__(self):
        str = "class=WindTurbineType4bIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
