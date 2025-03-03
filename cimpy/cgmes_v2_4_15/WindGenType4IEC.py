from .WindTurbineType3or4IEC import WindTurbineType3or4IEC
from .CGMESProfile import Profile


class WindGenType4IEC(WindTurbineType3or4IEC):
    """
    IEC Type 4 generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.4.

    :dipmax: Maximum active current ramp rate (di). It is project dependent parameter. Default: 0.0
    :diqmax: Maximum reactive current ramp rate (di). It is project dependent parameter. Default: 0.0
    :diqmin: Minimum reactive current ramp rate (d). It is case dependent parameter. Default: 0.0
    :tg: Time constant (T). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "dipmax": [Profile.DY.value, ],
        "diqmax": [Profile.DY.value, ],
        "diqmin": [Profile.DY.value, ],
        "tg": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class WindTurbineType3or4IEC:\n" + WindTurbineType3or4IEC.__doc__

    def __init__(self, dipmax = 0.0, diqmax = 0.0, diqmin = 0.0, tg = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.dipmax = dipmax
        self.diqmax = diqmax
        self.diqmin = diqmin
        self.tg = tg

    def __str__(self):
        str = "class=WindGenType4IEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
