
## Ship Sizes ##
#  Frigates
#  Destroyers
#  Cruisers
#  Battlecruisers
#  Battleships
#  Capitals
#    Carriers
#    Dreadnoughts
#    Force Auxillaries
#  Supercapitals
#    Supercarriers
#    Titans

class Ship():
    def __init__(self,):
        Mass        # mass
        Volume      # size
        Capacity    # cargo space
        MaxVelocity # max vel
        InertiaMod  # Inertia modifier
        WarpSpeed   # Speed of warp travel

        # Hitpoints
        ShieldHP
        ArmorHP
        StructuralHP

        # Resists
        EMResist=(0,0.5)    # shield, armor
        ExplosiveResist
        KineticResist
        ThermalResist
        Uniformity          # bleed-through threshold

        # Fitting Stuff
        PowergridOutput     # (ex 950MW)
        CPUOutput           # (ex 550Tf)
        Calibration         # (ex 400points) see EVE Wiki on wtf this is
        CapacitorCapacity   # (ex 2500 GJ)
        CapRechargeTime     # (ex 625k seconds)

        Slots
            High
            Med
            Low

        Hardpoints
            Turrets
            Launchers

        # Targetting and related
        MaxLockedTargets
        MaxTargettingRange
        Sensors
            Radar
            Ladar
            Magnetometric
            Gravimetric
        SignatureRadius
        ScanResolution
        ScanSpeed

        # Drones
        DroneBandwidth
        DroneCapacity

if __name__=="__main__":
        print("Tests completed.")
