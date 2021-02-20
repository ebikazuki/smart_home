import json
import requests
from flask import Flask, render_template, request
from flask_assistant import Assistant, ask, tell
from smart_home_temp import temp_result
# from smart_home_eremote import temp_on

app = Flask(__name__)
assist = Assistant(app, '/')

# MESHからのデータ受取り
@app.route("/temp", methods=['POST'])
def temp():
    result = request.data.decode()
    data = {"temp":float(result)}
    file = open("temp.json", "w")
    json.dump(data, file)
    return result

# 起動時の応答
@assist.action('Default Welcome Intent')
def greet_and_start():
    result = blight_result()
    text = "命令をどうぞ。"
    return ask(text)

# 温度の受答え
@assist.action('CheckTemp')
def CheckTemp():
    result = temp_result()
    text = str(result)
    # return ask("現在、" + text + "どです。エアコンをいれますか？")
    return tell("現在、"+ text + "どです。")

# エアコンの起動 
# @assist.action('AirconOn')
# def On():
#    temp_on()
#    return tell("エアコンをいれました。")
#

if __name__ == "__main__":

# エアコンの起動 
# @assist.action('AirconOn')
# def On():
#    temp_on()
#    return tell("エアコンをいれました。")
#

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
