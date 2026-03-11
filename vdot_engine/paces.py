import math

def velocity_from_vo2(vo2):

    # 0.000104v² + 0.182258v - (vo2+4.6) = 0

    a = 0.000104
    b = 0.182258
    c = -(vo2 + 4.60)

    disc = b*b - 4*a*c

    # meters/minute
    v = (-b + math.sqrt(disc)) / (2*a)

    return v

def pace_from_velocity(v):

    # v = meters per minute

    pace_min_per_km = 1000 / v

    minutes = int(pace_min_per_km)

    seconds = int((pace_min_per_km - minutes)*60)

    return f"{minutes}:{seconds:02d} /km"

def training_paces(vdot):

    zones = {

        "easy":(0.65,0.75),

        "marathon":(0.80,0.84),

        "threshold":(0.88,0.92),

        "interval":(0.98,1.02),

        "repetition":(1.05,1.10)
    }

    results = {}

    for zone,(low,high) in zones.items():

        low_vo2 = vdot*low
        high_vo2 = vdot*high

        v_low = velocity_from_vo2(low_vo2)
        v_high = velocity_from_vo2(high_vo2)

        pace_low = pace_from_velocity(v_high)
        pace_high = pace_from_velocity(v_low)

        results[zone]=(pace_low,pace_high)

    return results