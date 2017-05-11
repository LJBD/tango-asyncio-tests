import asyncio
from tango import DevState, GreenMode
from tango.server import Device, command, attribute


class AsyncioDevice(Device):
    green_mode = GreenMode.Asyncio

    async def init_device(self):
        await super().init_device()
        self.set_state(DevState.ON)

    @command
    async def long_running_command(self):
        self.set_state(DevState.INSERT)
        await asyncio.sleep(15)
        self.set_state(DevState.EXTRACT)

    @attribute
    async def test_attribute(self):
        return 42
