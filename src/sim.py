import random
from .physics import update
from .controller import control

def run():
    state = {'alt': 0, 'vel': 0}
    for _ in range(200):
        sensor = {'alt': state['alt'] + random.uniform(-2, 2)}
        thrust = control(sensor)
        state = update(state, thrust)
        print(state)
