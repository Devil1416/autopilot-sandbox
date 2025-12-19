import random
def read(state):
    return {"alt": state["alt"] + random.uniform(-2,2),
            "vel": state["vel"] + random.uniform(-0.5,0.5)}
