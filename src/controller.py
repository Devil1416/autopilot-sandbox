TARGET = 100
def control(sensor, prev=[0]):
    e = TARGET - sensor['alt']
    d = e - prev[0]
    thrust = 0.1*e + 0.05*d
    prev[0] = e
    return max(min(thrust, 20), -20)
