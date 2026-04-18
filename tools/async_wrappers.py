import asyncio
from services.registry import SERVICES

async def call_tool(name, *args):
    return await asyncio.to_thread(SERVICES[name], *args)