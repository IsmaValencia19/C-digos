from tkinter import *
from tkinter import ttk
import requests
import json



if __name__ == '__main__':
    complete_url = 'https://www.dolarsi.com/api/api.php?type=dolar'
    r = requests.get(complete_url)
    #print(r.text)

    text_json = r.json()

    for c in text_json['casa']:
        print(c.get())
        