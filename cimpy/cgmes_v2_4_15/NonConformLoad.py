from .EnergyConsumer import EnergyConsumer
from .CGMESProfile import Profile


class NonConformLoad(EnergyConsumer):
    """
    NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.

    :LoadGroup: Conform loads assigned to this ConformLoadGroup. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "LoadGroup": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EnergyConsumer:\n" + EnergyConsumer.__doc__

    def __init__(self, LoadGroup = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LoadGroup = LoadGroup

    def __str__(self):
        str = "class=NonConformLoad\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
