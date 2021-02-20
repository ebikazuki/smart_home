import json

def temp_result():
    file = open("temp.json", "r")
    json_dict = json.load(file)
    result = json_dict["temp"]
    return result

if __name__ == '__main__':
    temp_result()

