import json
import requests


def lambda_handler(event, context):
    #DrawGameId = 15, Name = MEGA Millions

    url = "https://www.calottery.com/api/DrawGameApi/DrawGamePastDrawResults/15/1/20"

    response = requests.get(url)
    data = response.json()
    game_name = data['Name']
    next_draw = data['NextDraw']['DrawNumber']
    next_draw_date = data['NextDraw']['DrawDate']
    next_draw_jackpot = data['NextDraw']['JackpotAmount']
    most_recent_draw_number = data['MostRecentDraw']['DrawNumber']
    most_recent_draw_date = data['MostRecentDraw']['DrawDate']
    number0 = data['MostRecentDraw']['WinningNumbers']['0']['Number']
    number1 = data['MostRecentDraw']['WinningNumbers']['1']['Number']
    number2 = data['MostRecentDraw']['WinningNumbers']['2']['Number']
    number3 = data['MostRecentDraw']['WinningNumbers']['3']['Number']
    number4 = data['MostRecentDraw']['WinningNumbers']['4']['Number']
    number5 = data['MostRecentDraw']['WinningNumbers']['5']['Number']
    api_response = {
        "frames": [
            {
                "text": str(game_name) + " - Next Draw: " + str(next_draw) + " will be played on, " + str(next_draw_date)[:10] + " for $" + str(next_draw_jackpot)[:-8] + " MILLION*",
                "icon": 46733,
                "index": 0
            },
            {
                "text": str(game_name) + " - Last Draw: " + str(most_recent_draw_number) + " was played on, " + str(most_recent_draw_date)[:10],
                "icon": 3273,
                "index": 1
            },
            {
                "text": str(game_name) + " - Last Draw Winning Numbers: " + str(number0) + " " + str(number1) + " " + str(number2) + " " + str(number3) + " " + str(number4) + " " + str(number5),
                "icon": 46733,
                "index": 2
            }
            ]
    }
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(api_response)

    return response_object
