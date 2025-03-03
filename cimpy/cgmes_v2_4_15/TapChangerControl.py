from .RegulatingControl import RegulatingControl
from .CGMESProfile import Profile


class TapChangerControl(RegulatingControl):
    """
    Describes behavior specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.

    :TapChanger: The regulating control scheme in which this tap changer participates. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "TapChanger": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class RegulatingControl:\n" + RegulatingControl.__doc__

    def __init__(self, TapChanger = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.TapChanger = TapChanger

    def __str__(self):
        str = "class=TapChangerControl\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
