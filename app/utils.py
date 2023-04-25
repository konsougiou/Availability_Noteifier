import json


def get_items():
    with open( "database.json", "r") as read_file:
        json_data = json.load(read_file)

    return json_data["items"]
 

def add_item(item_name: str, price: str):

    with open( "database.json", "r") as read_file:
        json_data = json.load(read_file)
        try:
            json_data["items"][item_name] = float(price)
        except:
            json_data["items"][item_name] = 0.00

    with open( "database.json", "w") as write_file:
        json.dump(json_data, write_file)


def remove_item(item_name: str):

    with open( "database.json", "r") as read_file:
        json_data = json.load(read_file)
        try:
            json_data["items"].pop(item_name)
        except:
            pass

    with open( "database.json", "w") as write_file:
        json.dump(json_data, write_file)


