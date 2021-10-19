# Script Name: rugby_matches.py
# Author: Tanmoy Debnath 121324683

def rugbymatch():
    #enter team names
    team1 = input("Enter the name of team 1: ")
    team2 = input("Enter the name of team 2: ")

    #get number of tries for each team
    tries_for_team1 = int(input(("Enter the number of tries for ") + team1 + (": ")))
    tries_for_team2 = int(input(("Enter the number of tries for ") + team2 + (": ")))

    #get number of points for each team
    points_team1 = int(input(("Enter the number of converted/penalty for ") + team1 + (": ")))
    points_team2 = int(input(("Enter the number of converted/penalty for ") + team2 + (": ")))

    #print results for individual teams
    print(team1 , tries_for_team1, points_team1)
    print(team2 , tries_for_team2, points_team2)

rugbymatch()

def req_name_and_age():
    rugby_name = input("Rugby players name: ")
    days_old = int(input("Enter no. of days old: "))

    no_of_years = days_old // 365
    remaining_days = days_old % 365

    print(rugby_name , "is" , str(no_of_years) , "years and" , str(remaining_days) , "days old")

req_name_and_age()

