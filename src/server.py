import asyncio

from asyncua import Server


async def main():
    server = Server()

    await server.init()

    server.set_endpoint(
        "opc.tcp://0.0.0.0:4840/opcua/server/"
    )

    namespace = await server.register_namespace(
        "http://factorytrace.local/opcua"
    )

    objects = server.nodes.objects

    test_object = await objects.add_object(
        namespace,
        "Test"
    )

    temperature = await test_object.add_variable(
        namespace,
        "Temperature",
        25.0
    )

    print("OPC UA Server starting...")
    print("Endpoint: opc.tcp://0.0.0.0:4840/opcua/server/")
    print("Temperature:", await temperature.read_value())

    async with server:
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())