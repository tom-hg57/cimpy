from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindContCurrLimIEC(IdentifiedObject):
    """
    Current limitation model.  The current limitation model combines the physical limits.  Reference: IEC Standard 61400-27-1 Section 6.6.5.7.

    :WindDynamicsLookupTable: The current control limitation model with which this wind dynamics lookup table is associated. Default: "list"
    :WindTurbineType3or4IEC: Wind turbine type 3 or 4 model with which this wind control current limitation model is associated. Default: None
    :imax: Maximum continuous current at the wind turbine terminals (). It is type dependent parameter. Default: 0.0
    :imaxdip: Maximum current during voltage dip at the wind turbine terminals (). It is project dependent parameter. Default: 0.0
    :mdfslim: Limitation of type 3 stator current  ():  - false=0: total current limitation,  - true=1: stator current limitation).  It is type dependent parameter. Default: False
    :mqpri: Prioritisation of q control during LVRT (): - true = 1: reactive power priority, - false = 0: active power priority.  It is project dependent parameter. Default: False
    :tufilt: Voltage measurement filter time constant (). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindDynamicsLookupTable": [Profile.DY.value, ],
        "WindTurbineType3or4IEC": [Profile.DY.value, ],
        "imax": [Profile.DY.value, ],
        "imaxdip": [Profile.DY.value, ],
        "mdfslim": [Profile.DY.value, ],
        "mqpri": [Profile.DY.value, ],
        "tufilt": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindDynamicsLookupTable = "list", WindTurbineType3or4IEC = None, imax = 0.0, imaxdip = 0.0, mdfslim = False, mqpri = False, tufilt = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindDynamicsLookupTable = WindDynamicsLookupTable
        self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
        self.imax = imax
        self.imaxdip = imaxdip
        self.mdfslim = mdfslim
        self.mqpri = mqpri
        self.tufilt = tufilt

    def __str__(self):
        str = "class=WindContCurrLimIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
