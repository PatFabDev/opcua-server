import asyncio

from asyncua import Server

from plant.plant import Plant
from plant.mixing_tank.mixing_tank import MixerTank
from simulation.engine import SimulationEngine
from plc.plc import PLC
from plc.io import MixerTankIO


async def main():
    # --------------------------------------------------
    # Create plant and simulation
    # --------------------------------------------------

    plant = Plant()

    mixer = MixerTank(
        "MixerTank01",
        500.0,
    )

    plant.add_machine(mixer)

    # PLC interface
    io = MixerTankIO(mixer)

    # PLC
    plc = PLC(io)

    # Simulation engine
    engine = SimulationEngine(plant)

    # --------------------------------------------------
    # Create OPC UA server
    # --------------------------------------------------

    server = Server()

    await server.init()

    server.set_endpoint(
        "opc.tcp://0.0.0.0:4840/opcua/server/"
    )

    namespace = await server.register_namespace(
        "http://factorytrace.local/opcua"
    )

    # --------------------------------------------------
    # Create OPC UA address space
    # --------------------------------------------------

    objects = server.nodes.objects

    mixer_node = await objects.add_object(
        namespace,
        mixer.get_name(),
    )

    # --------------------------------------------------
    # MixerTank process values
    # --------------------------------------------------

    capacity = await mixer_node.add_variable(
        namespace,
        "Capacity",
        mixer.get_capacity(),
    )

    level = await mixer_node.add_variable(
        namespace,
        "Level",
        mixer.get_level(),
    )

    temperature = await mixer_node.add_variable(
        namespace,
        "Temperature",
        mixer.get_temperature(),
    )

    phase = await mixer_node.add_variable(
        namespace,
        "Phase",
        mixer.get_phase().name,
    )

    # --------------------------------------------------
    # Valves
    # --------------------------------------------------

    valves_node = await mixer_node.add_object(
        namespace,
        "Valves",
    )

    inlet_valve_1_node = await valves_node.add_object(
        namespace,
        "InletValve1",
    )

    inlet_valve_1_state = await inlet_valve_1_node.add_variable(
        namespace,
        "State",
        mixer.get_inlet_valve_1_state().name,
    )

    inlet_valve_2_node = await valves_node.add_object(
        namespace,
        "InletValve2",
    )

    inlet_valve_2_state = await inlet_valve_2_node.add_variable(
        namespace,
        "State",
        mixer.get_inlet_valve_2_state().name,
    )

    outlet_valve_node = await valves_node.add_object(
        namespace,
        "OutletValve",
    )

    outlet_valve_state = await outlet_valve_node.add_variable(
        namespace,
        "State",
        mixer.get_outlet_valve_state().name,
    )

    # --------------------------------------------------
    # Heater
    # --------------------------------------------------

    heater_node = await mixer_node.add_object(
        namespace,
        "Heater",
    )

    heater_state = await heater_node.add_variable(
        namespace,
        "State",
        mixer.get_heater_state().name,
    )

    # --------------------------------------------------
    # Agitator
    # --------------------------------------------------

    agitator_node = await mixer_node.add_object(
        namespace,
        "Agitator",
    )

    agitator_state = await agitator_node.add_variable(
        namespace,
        "State",
        mixer.get_agitator_state().name,
    )

    # --------------------------------------------------
    # Start server
    # --------------------------------------------------

    print("OPC UA Server starting...")
    print("Endpoint: opc.tcp://0.0.0.0:4840/opcua/server/")
    print("MixerTank:", mixer.get_name())

    async with server:
        while True:
            # ------------------------------------------
            # PLC control logic
            # ------------------------------------------

            plc.update()

            # ------------------------------------------
            # Simulation
            # ------------------------------------------

            dt = 1.0

            engine.update(dt)

            # --------------------------------------------------
            # Update OPC UA values
            # --------------------------------------------------

            await level.write_value(
                mixer.get_level()
            )

            await temperature.write_value(
                mixer.get_temperature()
            )

            await phase.write_value(
                mixer.get_phase().name
            )

            await inlet_valve_1_state.write_value(
                mixer.get_inlet_valve_1_state().name
            )

            await inlet_valve_2_state.write_value(
                mixer.get_inlet_valve_2_state().name
            )

            await outlet_valve_state.write_value(
                mixer.get_outlet_valve_state().name
            )

            await heater_state.write_value(
                mixer.get_heater_state().name
            )

            await agitator_state.write_value(
                mixer.get_agitator_state().name
            )

            # ------------------------------------------
            # Wait for next cycle
            # ------------------------------------------

            await asyncio.sleep(dt)


if __name__ == "__main__":
    asyncio.run(main())