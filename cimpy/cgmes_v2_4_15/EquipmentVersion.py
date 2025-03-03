from .Base import Base
from .CGMESProfile import Profile


class EquipmentVersion(Base):
    """
    Version details.

    :baseUML: Base UML provided by CIM model manager. Default: ''
    :baseURIcore: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: ''
    :baseURIoperation: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: ''
    :baseURIshortCircuit: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: ''
    :date: Profile creation date Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. Default: ''
    :differenceModelURI: Difference model URI defined by IEC 61970-552. Default: ''
    :entsoeUML: UML provided by ENTSO-E. Default: ''
    :entsoeURIcore: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/EquipmentCore/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: ''
    :entsoeURIoperation: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/EquipmentOperation/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: ''
    :entsoeURIshortCircuit: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/EquipmentShortCircuit/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: ''
    :modelDescriptionURI: Model Description URI defined by IEC 61970-552. Default: ''
    :namespaceRDF: RDF namespace. Default: ''
    :namespaceUML: CIM UML namespace. Default: ''
    :shortName: The short name of the profile used in profile documentation. Default: ''
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "baseUML": [Profile.EQ.value, ],
        "baseURIcore": [Profile.EQ.value, ],
        "baseURIoperation": [Profile.EQ.value, ],
        "baseURIshortCircuit": [Profile.EQ.value, ],
        "date": [Profile.EQ.value, ],
        "differenceModelURI": [Profile.EQ.value, ],
        "entsoeUML": [Profile.EQ.value, ],
        "entsoeURIcore": [Profile.EQ.value, ],
        "entsoeURIoperation": [Profile.EQ.value, ],
        "entsoeURIshortCircuit": [Profile.EQ.value, ],
        "modelDescriptionURI": [Profile.EQ.value, ],
        "namespaceRDF": [Profile.EQ.value, ],
        "namespaceUML": [Profile.EQ.value, ],
        "shortName": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, baseUML = '', baseURIcore = '', baseURIoperation = '', baseURIshortCircuit = '', date = '', differenceModelURI = '', entsoeUML = '', entsoeURIcore = '', entsoeURIoperation = '', entsoeURIshortCircuit = '', modelDescriptionURI = '', namespaceRDF = '', namespaceUML = '', shortName = ''):

        self.baseUML = baseUML
        self.baseURIcore = baseURIcore
        self.baseURIoperation = baseURIoperation
        self.baseURIshortCircuit = baseURIshortCircuit
        self.date = date
        self.differenceModelURI = differenceModelURI
        self.entsoeUML = entsoeUML
        self.entsoeURIcore = entsoeURIcore
        self.entsoeURIoperation = entsoeURIoperation
        self.entsoeURIshortCircuit = entsoeURIshortCircuit
        self.modelDescriptionURI = modelDescriptionURI
        self.namespaceRDF = namespaceRDF
        self.namespaceUML = namespaceUML
        self.shortName = shortName

    def __str__(self):
        str = "class=EquipmentVersion\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
