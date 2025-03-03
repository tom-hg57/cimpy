from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovHydro4(TurbineGovernorDynamics):
    """
    Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors of traditional 'dashpot' type.  This model can be used to represent simple, Francis, Pelton or Kaplan turbines.

    :at: Turbine gain (At).  Typical Value = 1.2. Default: 0.0
    :bgv0: Kaplan blade servo point 0 (Bgv0).  Typical Value = 0. Default: 0.0
    :bgv1: Kaplan blade servo point 1 (Bgv1).  Typical Value = 0. Default: 0.0
    :bgv2: Kaplan blade servo point 2 (Bgv2). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1. Default: 0.0
    :bgv3: Kaplan blade servo point 3 (Bgv3). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667. Default: 0.0
    :bgv4: Kaplan blade servo point 4 (Bgv4).  Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9. Default: 0.0
    :bgv5: Kaplan blade servo point 5 (Bgv5). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1. Default: 0.0
    :bmax: Maximum blade adjustment factor (Bmax). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276. Default: 0.0
    :db1: Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0
    :dturb: Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1. Default: 0.0
    :eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0
    :gmax: Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1. Default: 0.0
    :gmin: Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0. Default: 0.0
    :gv0: Nonlinear gain point 0, PU gv (Gv0). Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1. Default: 0.0
    :gv1: Nonlinear gain point 1, PU gv (Gv1). Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4. Default: 0.0
    :gv2: Nonlinear gain point 2, PU gv (Gv2). Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5. Default: 0.0
    :gv3: Nonlinear gain point 3, PU gv (Gv3). Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7. Default: 0.0
    :gv4: Nonlinear gain point 4, PU gv (Gv4). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8. Default: 0.0
    :gv5: Nonlinear gain point 5, PU gv (Gv5). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9. Default: 0.0
    :hdam: Head available at dam (hdam).  Typical Value = 1. Default: 0.0
    :mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    :pgv0: Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0. Default: 0.0
    :pgv1: Nonlinear gain point 1, PU power (Pgv1). Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35. Default: 0.0
    :pgv2: Nonlinear gain point 2, PU power (Pgv2). Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468. Default: 0.0
    :pgv3: Nonlinear gain point 3, PU power (Pgv3). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796. Default: 0.0
    :pgv4: Nonlinear gain point 4, PU power (Pgv4). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917. Default: 0.0
    :pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99. Default: 0.0
    :qn1: No-load flow at nominal head (Qnl). Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0. Default: 0.0
    :rperm: Permanent droop (Rperm).  Typical Value = 0.05. Default: 0.0
    :rtemp: Temporary droop (Rtemp).  Typical Value = 0.3. Default: 0.0
    :tblade: Blade servo time constant (Tblade).  Typical Value = 100. Default: 0.0
    :tg: Gate servo time constant (Tg) (>0).  Typical Value = 0.5. Default: 0.0
    :tp: Pilot servo time constant (Tp).  Typical Value = 0.1. Default: 0.0
    :tr: Dashpot time constant (Tr) (>0).  Typical Value = 5. Default: 0.0
    :tw: Water inertia time constant (Tw) (>0).  Typical Value = 1. Default: 0.0
    :uc: Max gate closing velocity (Uc).  Typical Value = 0.2. Default: 0.0
    :uo: Max gate opening velocity (Uo).  Typical Vlaue = 0.2. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "at": [Profile.DY.value, ],
        "bgv0": [Profile.DY.value, ],
        "bgv1": [Profile.DY.value, ],
        "bgv2": [Profile.DY.value, ],
        "bgv3": [Profile.DY.value, ],
        "bgv4": [Profile.DY.value, ],
        "bgv5": [Profile.DY.value, ],
        "bmax": [Profile.DY.value, ],
        "db1": [Profile.DY.value, ],
        "db2": [Profile.DY.value, ],
        "dturb": [Profile.DY.value, ],
        "eps": [Profile.DY.value, ],
        "gmax": [Profile.DY.value, ],
        "gmin": [Profile.DY.value, ],
        "gv0": [Profile.DY.value, ],
        "gv1": [Profile.DY.value, ],
        "gv2": [Profile.DY.value, ],
        "gv3": [Profile.DY.value, ],
        "gv4": [Profile.DY.value, ],
        "gv5": [Profile.DY.value, ],
        "hdam": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pgv0": [Profile.DY.value, ],
        "pgv1": [Profile.DY.value, ],
        "pgv2": [Profile.DY.value, ],
        "pgv3": [Profile.DY.value, ],
        "pgv4": [Profile.DY.value, ],
        "pgv5": [Profile.DY.value, ],
        "qn1": [Profile.DY.value, ],
        "rperm": [Profile.DY.value, ],
        "rtemp": [Profile.DY.value, ],
        "tblade": [Profile.DY.value, ],
        "tg": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
        "tr": [Profile.DY.value, ],
        "tw": [Profile.DY.value, ],
        "uc": [Profile.DY.value, ],
        "uo": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, at = 0.0, bgv0 = 0.0, bgv1 = 0.0, bgv2 = 0.0, bgv3 = 0.0, bgv4 = 0.0, bgv5 = 0.0, bmax = 0.0, db1 = 0.0, db2 = 0.0, dturb = 0.0, eps = 0.0, gmax = 0.0, gmin = 0.0, gv0 = 0.0, gv1 = 0.0, gv2 = 0.0, gv3 = 0.0, gv4 = 0.0, gv5 = 0.0, hdam = 0.0, mwbase = 0.0, pgv0 = 0.0, pgv1 = 0.0, pgv2 = 0.0, pgv3 = 0.0, pgv4 = 0.0, pgv5 = 0.0, qn1 = 0.0, rperm = 0.0, rtemp = 0.0, tblade = 0.0, tg = 0.0, tp = 0.0, tr = 0.0, tw = 0.0, uc = 0.0, uo = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.at = at
        self.bgv0 = bgv0
        self.bgv1 = bgv1
        self.bgv2 = bgv2
        self.bgv3 = bgv3
        self.bgv4 = bgv4
        self.bgv5 = bgv5
        self.bmax = bmax
        self.db1 = db1
        self.db2 = db2
        self.dturb = dturb
        self.eps = eps
        self.gmax = gmax
        self.gmin = gmin
        self.gv0 = gv0
        self.gv1 = gv1
        self.gv2 = gv2
        self.gv3 = gv3
        self.gv4 = gv4
        self.gv5 = gv5
        self.hdam = hdam
        self.mwbase = mwbase
        self.pgv0 = pgv0
        self.pgv1 = pgv1
        self.pgv2 = pgv2
        self.pgv3 = pgv3
        self.pgv4 = pgv4
        self.pgv5 = pgv5
        self.qn1 = qn1
        self.rperm = rperm
        self.rtemp = rtemp
        self.tblade = tblade
        self.tg = tg
        self.tp = tp
        self.tr = tr
        self.tw = tw
        self.uc = uc
        self.uo = uo

    def __str__(self):
        str = "class=GovHydro4\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
