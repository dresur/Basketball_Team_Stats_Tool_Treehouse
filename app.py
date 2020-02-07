from constants import *
from sys import exit
import random


def number_players(players):
    if len(players) % 3 == 0:
        return True


def menu_initial():
    menu = ("\n BASKETBALL TEAMS STATS TOOLS \n \n"
            "---- MENU ---- \n\n"
            "1. Display Teams Stats \n"
            "2. Quit \n")
    print(menu)


def warning_principal():
    print("That option is not in the MENU\n")


def val_err():
    print("Use only numbers to choose from the MENU\n")


def print_teams(TEAMS):
    i = 1
    teams = []
    for team in TEAMS:
        teams.append(str(i) + ". " + team)
        i += 1
    for team in teams:
        print(team, sep ="\n")


def define_team(player, teams):
    no_experience = [players for players in player if players["experience"] == "NO"]
    experience = [players for players in player if players["experience"] == "YES"]
    final_teams = {}
    for team in teams:
        final_teams[team] = random.sample(no_experience, int(len(player) / len(teams) / 2)) + random.sample(experience, int(len(player) / len(teams) / 2))
        for players in final_teams[team]:
            if players in no_experience:
                no_experience.remove(players)
            else:
                experience.remove(players)
    return final_teams


def team_stats(final_teams, choice):
    ind = int(choice - 1)
    names = []
    experience = []
    guardians = []
    height = []
    team_name = TEAMS[ind]
    height_final = 0
    total_team_players = len(final_teams[TEAMS[ind]])
    for team in final_teams[TEAMS[ind]]:
        names.append(team["name"])
        experience.append(team["experience"])
        guardians.append(", ".join(team["guardians"].split("and")))
        height.append(team["height"].split())
    for a in height:
        height = int(a[0])
        height_final += height
    height_final = round(height_final / len(names), 2)
    experienced = experience.count("NO")
    no_experience = len(experience) - experienced
    return names, experienced, no_experience, guardians, height_final, team_name, total_team_players


if __name__ == "__main__":

    if number_players(PLAYERS) is False:
        print("Call more friend to play! You do not have enough players!")
        exit(0)
    else:
        while True:
            menu_initial()
            try:
                choice = int(input("Select you option: \n"))
            except ValueError:
                val_err()
                input("Press ENTER to try again")
                continue
            if choice == 1:
                while True:
                    print("\nChoose the team: \n")
                    print_teams(TEAMS)
                    print(str(int(len(TEAMS)) + 1) + ". Go to the previous MENU\n")
                    try:
                        choice = int(input("Select you option: \n"))
                    except ValueError:
                        val_err()
                        input("Press ENTER to try again")
                        continue
                    if choice <= 0 or choice > (len(TEAMS) + 1):
                        warning_principal()
                        input("Press ENTER to try again")
                    elif choice == (len(TEAMS) + 1):
                        break
                    else:
                        names, experienced, no_experience, guardians, height_final, team_name, total_team_players = \
                            team_stats(define_team(PLAYERS, TEAMS), choice)
                        print("\nInformation about {}\n"
                              "------------------\n"
                              "TOTAL NUMBER OF PLAYERS: {}\n".format(team_name.upper(), total_team_players))
                        print("Players:\n" + ", ".join(names) + "\n --------------------------")
                        print("Guardians: \n" + ", ".join(guardians) + "\n --------------------------")
                        print("# Experienced players:\n{}"
                              "\n --------------------------\n"
                              "# Inexperienced players:\n{}"
                              "\n--------------------------\n"
                              "Average Height (inches):\n{}".format(experienced, no_experience, height_final))
                        input("\nPress ENTER to continue")
            elif choice == 2:
                print("Thank you!")
                input("Press ENTER to EXIT")
                exit(0)
            else:
                warning_principal()
                input("Press ENTER to try again")
                continue
