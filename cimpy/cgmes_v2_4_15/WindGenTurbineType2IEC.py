from .WindTurbineType1or2IEC import WindTurbineType1or2IEC
from .CGMESProfile import Profile


class WindGenTurbineType2IEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC Type 2.  Reference: IEC Standard 61400-27-1, section 6.5.3.

    :WindContRotorRIEC: Wind control rotor resistance model associated with wind turbine type 2 model. Default: None
    :WindPitchContEmulIEC: Pitch control emulator model associated with this wind turbine type 2 model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindContRotorRIEC": [Profile.DY.value, ],
        "WindPitchContEmulIEC": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class WindTurbineType1or2IEC:\n" + WindTurbineType1or2IEC.__doc__

    def __init__(self, WindContRotorRIEC = None, WindPitchContEmulIEC = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindContRotorRIEC = WindContRotorRIEC
        self.WindPitchContEmulIEC = WindPitchContEmulIEC

    def __str__(self):
        str = "class=WindGenTurbineType2IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
