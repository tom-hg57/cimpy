from .EquipmentContainer import EquipmentContainer
from .CGMESProfile import Profile


class Bay(EquipmentContainer):
    """
    A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.  A bay typically represents a physical grouping related to modularization of equipment.

    :VoltageLevel: The voltage level containing this bay. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "VoltageLevel": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EquipmentContainer:\n" + EquipmentContainer.__doc__

    def __init__(self, VoltageLevel = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.VoltageLevel = VoltageLevel

    def __str__(self):
        str = "class=Bay\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
