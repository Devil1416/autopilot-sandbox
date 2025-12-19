import matplotlib.pyplot as plt
from .physics import update
from .sensors import read
from .controller import control

def run():
    state = {"alt":0,"vel":0}
    data = []
    for _ in range(300):
        s = read(state)
        thrust = control(s)
        state = update(state, thrust)
        data.append(state["alt"])
    plt.plot(data)
    plt.title("autopilot stabilization")
    plt.show()
