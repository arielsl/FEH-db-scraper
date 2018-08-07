import requests
import pandas as pandas
import mysql.connector


def main():
    #int to maintain program running
    choice = 0

    #program ends when user types in 0
    while choice != 0:
        #ask for the urls for the hero in the database
        url = input("Enter hero url or press 0 to exit: ")
        # image_url = input("Enter hero image url: ")

        #connect to the url with the correct headers
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)

        #get the tables/dataframe from the website
        df = pandas.read_html(r.text)
        no_of_table = len(df)

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

if __name__ == "__main__":
    main()
