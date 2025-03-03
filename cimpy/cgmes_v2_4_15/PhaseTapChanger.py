from .TapChanger import TapChanger
from .CGMESProfile import Profile


class PhaseTapChanger(TapChanger):
    """
    A transformer phase shifting tap model that controls the phase angle difference across the power transformer and potentially the active power flow through the power transformer.  This phase tap model may also impact the voltage magnitude.

    :TransformerEnd: Phase tap changer associated with this transformer end. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "TransformerEnd": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class TapChanger:\n" + TapChanger.__doc__

    def __init__(self, TransformerEnd = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.TransformerEnd = TransformerEnd

    def __str__(self):
        str = "class=PhaseTapChanger\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
