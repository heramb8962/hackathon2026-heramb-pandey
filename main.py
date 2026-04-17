import json
from agent.agent import process_ticket

def main():
    with open("data/tickets.json") as f:
        tickets = json.load(f)

    for ticket in tickets:
        process_ticket(ticket)

if __name__ == "__main__":
    main()