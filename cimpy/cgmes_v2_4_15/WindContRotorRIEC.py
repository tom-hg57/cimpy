from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class WindContRotorRIEC(IdentifiedObject):
    """
    Rotor resistance control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.2.

    :WindDynamicsLookupTable: The wind dynamics lookup table associated with this rotor resistance control model. Default: "list"
    :WindGenTurbineType2IEC: Wind turbine type 2 model with whitch this wind control rotor resistance model is associated. Default: None
    :kirr: Integral gain in rotor resistance PI controller (). It is type dependent parameter. Default: 0.0
    :komegafilt: Filter gain for generator speed measurement (K). It is type dependent parameter. Default: 0.0
    :kpfilt: Filter gain for power measurement (). It is type dependent parameter. Default: 0.0
    :kprr: Proportional gain in rotor resistance PI controller (). It is type dependent parameter. Default: 0.0
    :rmax: Maximum rotor resistance (). It is type dependent parameter. Default: 0.0
    :rmin: Minimum rotor resistance (). It is type dependent parameter. Default: 0.0
    :tomegafilt: Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0.0
    :tpfilt: Filter time constant for power measurement (). It is type dependent parameter. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "WindDynamicsLookupTable": [Profile.DY.value, ],
        "WindGenTurbineType2IEC": [Profile.DY.value, ],
        "kirr": [Profile.DY.value, ],
        "komegafilt": [Profile.DY.value, ],
        "kpfilt": [Profile.DY.value, ],
        "kprr": [Profile.DY.value, ],
        "rmax": [Profile.DY.value, ],
        "rmin": [Profile.DY.value, ],
        "tomegafilt": [Profile.DY.value, ],
        "tpfilt": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, WindDynamicsLookupTable = "list", WindGenTurbineType2IEC = None, kirr = 0.0, komegafilt = 0.0, kpfilt = 0.0, kprr = 0.0, rmax = 0.0, rmin = 0.0, tomegafilt = 0.0, tpfilt = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.WindDynamicsLookupTable = WindDynamicsLookupTable
        self.WindGenTurbineType2IEC = WindGenTurbineType2IEC
        self.kirr = kirr
        self.komegafilt = komegafilt
        self.kpfilt = kpfilt
        self.kprr = kprr
        self.rmax = rmax
        self.rmin = rmin
        self.tomegafilt = tomegafilt
        self.tpfilt = tpfilt

    def __str__(self):
        str = "class=WindContRotorRIEC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
