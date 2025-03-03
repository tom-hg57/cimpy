from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant including their control models.

    :EnergySource: Energy Source (current source) with which this wind Type 3 or 4 dynamics model is asoociated. Default: None
    :RemoteInputSignal: Wind turbine Type 3 or 4 models using this remote input signal. Default: None
    :WindPlantDynamics: The wind plant with which the wind turbines type 3 or 4 are associated. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "EnergySource": [Profile.DY.value, ],
        "RemoteInputSignal": [Profile.DY.value, ],
        "WindPlantDynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, EnergySource = None, RemoteInputSignal = None, WindPlantDynamics = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.EnergySource = EnergySource
        self.RemoteInputSignal = RemoteInputSignal
        self.WindPlantDynamics = WindPlantDynamics

    def __str__(self):
        str = "class=WindTurbineType3or4Dynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
