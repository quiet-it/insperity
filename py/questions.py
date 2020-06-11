from PyInquirer import style_from_dict, Token, prompt

import os
from hosts import *

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})
# choices = []
this_clock = []

def home_menu():
    home_prompt = {
        "type" : "list",
        "name" : "home",
        "message" : "Please pick the site:",
        "choices" : ['Saratoga', "Barnum", 'Jackson', 'Exit']
    }
    menu = prompt(home_prompt,style = style)

    return menu['home']

def menu(site):
    os.system('cls')
    print( site.capitalize(), " site")
    questions = {
        "type" : "list",
        "name" : site+"_menu",
        "message" : "What you want to do next?",
        "choices" : ['Home', 'Watch all clocks', 'Clocks', "Reboot all clocks", "Service"]
    }
    menu = prompt(questions,style = style)
    return menu[ site + '_menu']

def back_menu():
    question = {
        "type" : "list",
        "name" : "back",
        "message" : "Go back?",
        "choices" : ['Back'],
    }
    menu = prompt(question,style = style)
    return menu['back']

def clocks_menu(site):
    os.system('cls')
    choices = []
    print( site.capitalize(), " site")
    for item in hosts[site]:
        choices.append(hosts[site][item]['description']) #Find these 2 vars on the top
        this_clock.append(item)
    questions = {
        "type" : "list",
        "name" : site+"_clocks",
        "message" : "Pick one clock to see it's menu",
        "choices" : ['Home'] + choices + ['Back']
    }
    menu = prompt(questions,style = style)
    return menu[ site + '_clocks']

def one_clock_menu(name, description):
    os.system('cls')
    print( description.capitalize(), "menu")
    questions = {
        "type" : "list",
        "name" : name+"_menu",
        "message" : "This clock name: "+description,
        "choices" : ['Home', "Watch", 'Restart', 'Logs', "Service", "Back"]
    }
    menu = prompt(questions,style = style)
    return menu[ name + '_menu']

# def saratoga_menu():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("Saratoga site")
#     saratoga_prompt = {
#         "type" : "list",
#         "name" : "saratoga_menu",
#         "message" : "What you want to do next?",
#         "choices" : ['Home', 'Watch all clocks', 'Clocks', "Reboot all clocks", "Service"]
#     }
#     menu = prompt(saratoga_prompt,style = style)
#     return menu['saratoga_menu']
