TARGET = 100
def control(sensor, prev=[0]):
    error = TARGET - sensor["alt"]
    d = error - prev[0]
    thrust = 0.12*error + 0.05*d
    prev[0] = error
    return max(min(thrust, 20), -20)
