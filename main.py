# Placeholders. Showing execution flow

# Create the event queue
queue = EventQueue(args..)

# Create the state
state = LawnMowerState(args..)

# Create start event and end event
start = StartEvent(args..)
end = EndEvent(args..)

# Create output
writer = LawnMowerWriter(state)

# Create the simulation and start the simulation
sim = simulator(state, queue, writer, start, stop)
sim.execute()
