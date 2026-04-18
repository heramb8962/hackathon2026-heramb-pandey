import json
import asyncio
from agent.agent import process_ticket

async def run_ticket(ticket):
    return process_ticket(ticket)

async def main():
    with open("data/tickets.json") as f:
        tickets = json.load(f)

    tasks = [run_ticket(ticket) for ticket in tickets]

    results = await asyncio.gather(*tasks)

    print("\nFINAL RESULTS:")
    for res in results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())