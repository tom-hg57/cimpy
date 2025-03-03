from .MeasurementValue import MeasurementValue
from .CGMESProfile import Profile


class AccumulatorValue(MeasurementValue):
    """
    AccumulatorValue represents an accumulated (counted) MeasurementValue.

    :Accumulator: The values connected to this measurement. Default: None
    :AccumulatorReset: The command that reset the accumulator value. Default: None
    :value: The value to supervise. The value is positive. Default: 0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Accumulator": [Profile.EQ.value, ],
        "AccumulatorReset": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class MeasurementValue:\n" + MeasurementValue.__doc__

    def __init__(self, Accumulator = None, AccumulatorReset = None, value = 0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Accumulator = Accumulator
        self.AccumulatorReset = AccumulatorReset
        self.value = value

    def __str__(self):
        str = "class=AccumulatorValue\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
