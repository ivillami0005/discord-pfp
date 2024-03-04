from discordrp import Presence
import time

client_id = "1214032046498779136"  # Replace this with your own client id

with Presence(client_id) as presence:
    print("Connected")
    presence.set(
        {
            "state": "In Game",
            "details": "Summoner's Rift",
            "timestamps": {"start": int(time.time())},
        }
    )
    print("Presence updated")

    while True:
        time.sleep(15)
