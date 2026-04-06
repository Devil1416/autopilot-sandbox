"""Simple enum-based flight state machine."""
from enum import Enum, auto
from typing import Optional, Callable

class FlightState(Enum):
    PREFLIGHT  = auto()
    TAKEOFF    = auto()
    CLIMB      = auto()
    CRUISE     = auto()
    DESCEND    = auto()
    LANDING    = auto()
    LANDED     = auto()
    ABORT      = auto()

# Valid transitions: state -> set of allowed next states
TRANSITIONS: dict[FlightState, set[FlightState]] = {
    FlightState.PREFLIGHT: {FlightState.TAKEOFF, FlightState.ABORT},
    FlightState.TAKEOFF:  {FlightState.CLIMB,   FlightState.ABORT},
    FlightState.CLIMB:    {FlightState.CRUISE,  FlightState.ABORT},
    FlightState.CRUISE:   {FlightState.DESCEND, FlightState.ABORT},
    FlightState.DESCEND:  {FlightState.LANDING, FlightState.ABORT},
    FlightState.LANDING:  {FlightState.LANDED,  FlightState.ABORT},
    FlightState.LANDED:   set(),
    FlightState.ABORT:    set(),
}

class FlightStateMachine:
    def __init__(self):
        self.state = FlightState.PREFLIGHT
        self._on_enter: dict[FlightState, Callable] = {}

    def on_enter(self, state: FlightState, cb: Callable):
        self._on_enter[state] = cb

    def transition(self, target: FlightState) -> bool:
        if target not in TRANSITIONS.get(self.state, set()):
            return False
        self.state = target
        if target in self._on_enter:
            self._on_enter[target]()
        return True
