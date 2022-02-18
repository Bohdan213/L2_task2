import argparse
import requests
import sys
import json

# a = requests.get("https://api.twitter.com/2/users/44196397/following?user.fields=created_at", headers={'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAI7vZAEAAAAAWxLmcJ3L6Qn49oId3kUP5CZijmk%3DLDuIqIpBahgDanLhSxqwl7A2ueKRfXsFK4ll4zCgatORTveens'})
# a = a.json()

key_value = []

def recursive(data, users_key):
    global key_value
    if type(data) == dict:
        for key in data.keys():
            if key == users_key:
                key_value.append(data[key])
            else:
                if type(data[key]) == dict:
                    recursive(data[key], users_key)
    else:
        return


def main():
    users_key = input()
    with open('twitter.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    API_list = data['data']
    for dictionary in API_list:
        for key in dictionary.keys():
            if key == users_key:
                key_value.append(dictionary[key])
            else:
                if type(dictionary[key]) == dict:
                    recursive(dictionary[key], users_key)
    return key_value

if __name__ == '__main__':
    print(main())