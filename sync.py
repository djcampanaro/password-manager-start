import json

def sync_data():

    try:
        with open("data_laptop.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data_laptop.json", "w") as data_file:
            json.dump({}, data_file, indent=4)

    try:
        with open("data_desktop.json", "r") as data_file_2:
            data_2 = json.load(data_file_2)
    except FileNotFoundError:
        with open("data_desktop.json", "w") as data_file_2:
            json.dump({}, data_file_2, indent=4)

    data_sync = {**data, **data_2}
    data_sync_sorted = {key: value for key, value in sorted(data_sync.items())}

    with open("data_desktop.json", "w") as data_file:
        json.dump(data_sync_sorted, data_file, indent=4)
