import asyncio

from asyncua import Server

from mixing_tank.mixing_tank import MixerTank


async def main():
    # Create MixerTank process model
    mixer = MixerTank("MixerTank01", 2000)

    # Create OPC UA server
    server = Server()

    await server.init()

    server.set_endpoint(
        "opc.tcp://0.0.0.0:4840/opcua/server/"
    )

    # Register application namespace
    namespace = await server.register_namespace(
        "http://factorytrace.local/opcua"
    )

    # Get Objects folder
    objects = server.nodes.objects

    # Create MixerTank object
    mixer_node = await objects.add_object(
        namespace,
        mixer.get_name()
    )

    # Create OPC UA variables
    capacity = await mixer_node.add_variable(
        namespace,
        "Capacity",
        mixer.get_capacity()
    )

    level = await mixer_node.add_variable(
        namespace,
        "Level",
        mixer.get_level()
    )

    temperature = await mixer_node.add_variable(
        namespace,
        "Temperature",
        mixer.get_temperature()
    )

    print("OPC UA Server starting...")
    print("Endpoint: opc.tcp://0.0.0.0:4840/opcua/server/")
    print("Capacity:", await capacity.read_value())
    print("Level:", await level.read_value())
    print("Temperature:", await temperature.read_value())

    async with server:
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())