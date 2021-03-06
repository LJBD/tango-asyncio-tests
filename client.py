import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('192.168.120.168', 8888,
                                                   loop=loop)

    print('Send: %r' % message)
    writer.write(message.encode())

    data = await reader.read(100)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()


message = 'sys/tg_test/1/double_image'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
