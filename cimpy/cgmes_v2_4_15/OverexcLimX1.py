from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics
from .CGMESProfile import Profile


class OverexcLimX1(OverexcitationLimiterDynamics):
    """
    Field voltage over excitation limiter.

    :efd1: Low voltage point on the inverse time characteristic (EFD).  Typical Value = 1.1. Default: 0.0
    :efd2: Mid voltage point on the inverse time characteristic (EFD).  Typical Value = 1.2. Default: 0.0
    :efd3: High voltage point on the inverse time characteristic (EFD).  Typical Value = 1.5. Default: 0.0
    :efddes: Desired field voltage (EFD).  Typical Value = 0.9. Default: 0.0
    :efdrated: Rated field voltage (EFD).  Typical Value = 1.05. Default: 0.0
    :kmx: Gain (K).  Typical Value = 0.01. Default: 0.0
    :t1: Time to trip the exciter at the low voltage point on the inverse time characteristic (TIME).  Typical Value = 120. Default: 0.0
    :t2: Time to trip the exciter at the mid voltage point on the inverse time characteristic (TIME).  Typical Value = 40. Default: 0.0
    :t3: Time to trip the exciter at the high voltage point on the inverse time characteristic (TIME).  Typical Value = 15. Default: 0.0
    :vlow: Low voltage limit (V) (>0). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efd1": [Profile.DY.value, ],
        "efd2": [Profile.DY.value, ],
        "efd3": [Profile.DY.value, ],
        "efddes": [Profile.DY.value, ],
        "efdrated": [Profile.DY.value, ],
        "kmx": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "vlow": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class OverexcitationLimiterDynamics:\n" + OverexcitationLimiterDynamics.__doc__

    def __init__(self, efd1 = 0.0, efd2 = 0.0, efd3 = 0.0, efddes = 0.0, efdrated = 0.0, kmx = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, vlow = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efd1 = efd1
        self.efd2 = efd2
        self.efd3 = efd3
        self.efddes = efddes
        self.efdrated = efdrated
        self.kmx = kmx
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.vlow = vlow

    def __str__(self):
        str = "class=OverexcLimX1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
