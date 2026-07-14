import json

player_profile = {
    "name": "Abdul",
    "Level": "1",
    "max_hp": "100",
    "inv": ["p", "p", "p", "s"]
    }

with open("save_data.json", "w") as file:
    json.dump(player_profile, file, indent=4)
print("done printing")

print("Restoring data")
with open ("save_data.json", "r") as file:
    loaded_profile = json.load(file)
print(f"Character:{loaded_profile['name']}")
print(f"lavel:{loaded_profile['Level']}")
print(f"inventory:{loaded_profile['inv']}")