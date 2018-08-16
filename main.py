# This main file will traverse the heroes table and send the information to be gathered.
# Afterwards it will write them into the database

import requests
import pandas as pandas
import mysql.connector
import hero
from bs4 import BeautifulSoup


def main():
    # choice = 1

    # Url that holds the hero table
    table_url = "https://feheroes.gamepedia.com/Hero_list"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(table_url, headers=headers)

    # Grab the html from the url
    soup = BeautifulSoup(r.text, "lxml")
    # Grab the table with the heroes from the soup
    table = soup.find("table")
    # Grab all the rows to read in the table
    rows = table.findAll("tr")
    # Use this count to skip first row(header) and count heroes read
    hero_count = 0

    # Iterate through all the rows
    for row in rows:
        if hero_count == 0:
            hero_count += 1
            continue
        data = row.find("td")
        link = data.find("a")
        print(link["title"])
        print("https://feheroes.gamepedia.com/" + link["href"])
        image = link.find("img")
        print(image["src"])
        hero_count += 1
        if hero_count == 3:
            break


    # while loop for user choice
    # count = 1
    # while True:
    #     print("Count at: " + str(count))
    #     try:
    #         hero_choice = int(input("Enter 1 next hero, 2 to skip next hero or 0 to end: "))
    #         if hero_choice == 1:
    #             print("Hero")
    #             pass
    #         elif hero_choice == 2:
    #             print("Skip")
    #             continue
    #         elif hero_choice == 0:
    #             print("End")
    #             break
    #         else:
    #             print("Not a known command!")
    #             break
    #     except:
    #         print("Please type an integer!")
    #         continue
    #     count += 1


    # program ends when user types in 0
    # while choice != 0:
        #ask for the urls for the hero in the database
        # url = input("Enter hero url or press 0 to exit: ")
        # image_url = input("Enter hero image url: ")

        #connect to the url with the correct headers
        # headers = {"User-Agent": "Mozilla/5.0"}
        # r = requests.get(url, headers=headers)

        #get the tables/dataframe from the website
        # df = pandas.read_html(r.text)
        # no_of_table = len(df)

        #print the urls as confirmation
        # print("Hero url: " + url)
        # print("Image url: " + image_url)
        # print()

        #get the stats and weapon from website
        # if no_of_table == 14:
        #     print("LEVEL 1 STATS")
        #     print("HP: " + df[3][1][len(df[3][1]) - 1])
        #     print("ATK: " + df[3][2][len(df[3][2]) - 1])
        #     print("SPD: " + df[3][3][len(df[3][3]) - 1])
        #     print("DEF: " + df[3][4][len(df[3][4]) - 1])
        #     print("RES: " + df[3][5][len(df[3][5]) - 1])
        #     print("BST: " + df[3][6][len(df[3][6]) - 1])
        #     print()
        #     print("Level 40 STATS")
        #     print("HP: " + df[4][1][len(df[4][1]) - 1])
        #     print("ATK: " + df[4][2][len(df[4][2]) - 1])
        #     print("SPD: " + df[4][3][len(df[4][3]) - 1])
        #     print("DEF: " + df[4][4][len(df[4][4]) - 1])
        #     print("RES: " + df[4][5][len(df[4][5]) - 1])
        #     print("BST: " + df[4][6][len(df[4][6]) - 1])
        #     print()
        #     print("WEAPONS")
        #     print("Weapon at 5: " + df[6][0][len(df[6][0]) - 1])
        # if no_of_table == 15:
        #     print("LEVEL 1 STATS")
        #     print("HP: " + df[4][1][len(df[4][1]) - 1])
        #     print("ATK: " + df[4][2][len(df[4][2]) - 1])
        #     print("SPD: " + df[4][3][len(df[4][3]) - 1])
        #     print("DEF: " + df[4][4][len(df[4][4]) - 1])
        #     print("RES: " + df[4][5][len(df[4][5]) - 1])
        #     print("BST: " + df[4][6][len(df[4][6]) - 1])
        #     print()
        #     print("Level 40 STATS")
        #     print("HP: " + df[5][1][len(df[5][1]) - 1])
        #     print("ATK: " + df[5][2][len(df[5][2]) - 1])
        #     print("SPD: " + df[5][3][len(df[5][3]) - 1])
        #     print("DEF: " + df[5][4][len(df[5][4]) - 1])
        #     print("RES: " + df[5][5][len(df[5][5]) - 1])
        #     print("BST: " + df[5][6][len(df[5][6]) - 1])
        #     print()
        #     print("WEAPONS")
        #     print("Weapon at 5: " + df[7][0][len(df[7][0]) - 1])

    return 0

def connect_to_db():
    return

def disconnect_to_db():
    return

def add_to_db(Hero):
    return

if __name__ == "__main__":
    main()
