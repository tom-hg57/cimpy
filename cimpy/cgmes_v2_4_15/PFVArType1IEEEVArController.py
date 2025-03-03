from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics
from .CGMESProfile import Profile


class PFVArType1IEEEVArController(PFVArControllerType1Dynamics):
    """
    The class represents IEEE VAR Controller Type 1 which operates by moving the voltage reference directly.  Reference: IEEE Standard 421.5-2005 Section 11.3.

    :tvarc: Var controller time delay ().  Typical Value = 5. Default: 0.0
    :vvar: Synchronous machine power factor (). Default: 0.0
    :vvarcbw: Var controller dead band ().  Typical Value = 0.02. Default: 0.0
    :vvarref: Var controller reference (). Default: 0.0
    :vvtmax: Maximum machine terminal voltage needed for pf/var controller to be enabled (). Default: 0.0
    :vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "tvarc": [Profile.DY.value, ],
        "vvar": [Profile.DY.value, ],
        "vvarcbw": [Profile.DY.value, ],
        "vvarref": [Profile.DY.value, ],
        "vvtmax": [Profile.DY.value, ],
        "vvtmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PFVArControllerType1Dynamics:\n" + PFVArControllerType1Dynamics.__doc__

    def __init__(self, tvarc = 0.0, vvar = 0.0, vvarcbw = 0.0, vvarref = 0.0, vvtmax = 0.0, vvtmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.tvarc = tvarc
        self.vvar = vvar
        self.vvarcbw = vvarcbw
        self.vvarref = vvarref
        self.vvtmax = vvtmax
        self.vvtmin = vvtmin

    def __str__(self):
        str = "class=PFVArType1IEEEVArController\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
