from .TransformerEnd import TransformerEnd
from .CGMESProfile import Profile


class PowerTransformerEnd(TransformerEnd):
    """
    A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star equivalent as follows 1) for a two Terminal PowerTransformer the high voltage PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage PowerTransformerEnd has zero values for r, r0, x, and x0. 2) for a three Terminal PowerTransformer the three PowerTransformerEnds represents a star equivalent with each leg in the star represented by r, r0, x, and x0 values. 3) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.

    :PowerTransformer: The ends of this power transformer. Default: None
    :b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. Default: 0.0
    :b0: Zero sequence magnetizing branch susceptance. Default: 0.0
    :connectionKind: Kind of connection. Default: None
    :g: Magnetizing branch conductance. Default: 0.0
    :g0: Zero sequence magnetizing branch conductance (star-model). Default: 0.0
    :phaseAngleClock: Terminal voltage phase angle displacement where 360 degrees are represented with clock hours. The valid values are 0 to 11. For example, for the secondary side end of a transformer with vector group code of `Dyn11`, specify the connection kind as wye with neutral and specify the phase angle of the clock as 11.  The clock value of the transformer end number specified as 1, is assumed to be zero.  Note the transformer end number is not assumed to be the same as the terminal sequence number. Default: 0
    :r: Resistance (star-model) of the transformer end. The attribute shall be equal or greater than zero for non-equivalent transformers. Default: 0.0
    :r0: Zero sequence series resistance (star-model) of the transformer end. Default: 0.0
    :ratedS: Normal apparent power rating. The attribute shall be a positive value. For a two-winding transformer the values for the high and low voltage sides shall be identical. Default: 0.0
    :ratedU: Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU that is greater or equal than ratedU for the lower voltage sides. Default: 0.0
    :x: Positive sequence series reactance (star-model) of the transformer end. Default: 0.0
    :x0: Zero sequence series reactance of the transformer end. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "PowerTransformer": [Profile.EQ.value, ],
        "b": [Profile.EQ.value, ],
        "b0": [Profile.EQ.value, ],
        "connectionKind": [Profile.EQ.value, ],
        "g": [Profile.EQ.value, ],
        "g0": [Profile.EQ.value, ],
        "phaseAngleClock": [Profile.EQ.value, ],
        "r": [Profile.EQ.value, ],
        "r0": [Profile.EQ.value, ],
        "ratedS": [Profile.EQ.value, ],
        "ratedU": [Profile.EQ.value, ],
        "x": [Profile.EQ.value, ],
        "x0": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class TransformerEnd:\n" + TransformerEnd.__doc__

    def __init__(self, PowerTransformer = None, b = 0.0, b0 = 0.0, connectionKind = None, g = 0.0, g0 = 0.0, phaseAngleClock = 0, r = 0.0, r0 = 0.0, ratedS = 0.0, ratedU = 0.0, x = 0.0, x0 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.PowerTransformer = PowerTransformer
        self.b = b
        self.b0 = b0
        self.connectionKind = connectionKind
        self.g = g
        self.g0 = g0
        self.phaseAngleClock = phaseAngleClock
        self.r = r
        self.r0 = r0
        self.ratedS = ratedS
        self.ratedU = ratedU
        self.x = x
        self.x0 = x0

    def __str__(self):
        str = "class=PowerTransformerEnd\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
