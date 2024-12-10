from events.eventqueue import EventQueue
from state.state import State
from events.start_event import StartEvent
from events.stop_event import StopEvent
from writer.lawn_mower_writer import LawnWriter

from sim.sim import Sim

# Placeholders. Showing execution flow

#
seed = 42
number_of_mowers = 100
number_of_techs = 10
p_violation = 0.2
c_min = 30 # min time to cut the grass
c_max = 50 # max time to cut the grass
v_min = 1 # min time for violations
v_max = 30 # max time for violations
runtime = 500

# Create the event queue
queue = EventQueue()

# Create the state
state = State(seed, number_of_mowers, number_of_techs, p_violation, c_min, c_max, v_min, v_max, runtime)

# Create start event and end event
start = StartEvent(state, queue)
stop = StopEvent(state, queue, runtime)

# Create output
writer = LawnWriter(state)

# Create the simulation and start the simulation
sim = Sim(state, queue, writer, start, stop)
sim.run()
