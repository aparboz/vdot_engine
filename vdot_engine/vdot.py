import math

def velocity(distance_m, time_s):
    return distance_m / time_s


def vo2_from_velocity(v):
    v*=60
    return -4.60 + 0.182258 * v + 0.000104 * v * v


def percent_vo2max(time_min):
    return 0.8 + 0.1894393 * math.exp(-0.012778 * time_min) + 0.2989558 * math.exp(-0.1932605 * time_min)


def vdot(distance_m, time_s):

    v = velocity(distance_m, time_s)

    vo2 = vo2_from_velocity(v)

    pct = percent_vo2max(time_s/60)

    return vo2 / pct