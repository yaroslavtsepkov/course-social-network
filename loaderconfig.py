import json
import os

def get_data(path=None):
    """ 
    get config data from file
    Args:
        path(string): path to config file
    Return:
        dict {"login":value", "password":value}
    """

    # use default path 
    if not path:
        path = os.path.relpath("config.json")
    
    try:
        with open(path, mode="r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)

if __name__ == "__main__":
    pass
