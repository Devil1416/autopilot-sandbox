def update(state, thrust):
    g = -9.8
    acc = thrust + g
    state['vel'] += acc * 0.1
    state['alt'] += state['vel'] * 0.1
    return state
