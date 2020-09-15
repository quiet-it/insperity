from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt
from examples import custom_style_2
import os
from questions import *
from ssh import *

def home():
    os.system('cls')
    menu = home_menu()
    print('Welcome Home!')
    if menu == "Jackson":
        sites("jackson")
    if menu == "Barnum":
        sites("barnum")
    if menu == "Saratoga":
        sites("saratoga")
    if menu == "Hazelwood":
        sites("hazelwood")
    if menu == "Chicago":
        sites("chicago")
    if menu == 'Exit':
        exit()


def sites(site):
    # global menu
    site = site
    os.system('cls')
    site_menu = menu(site+"_menu")
    if site_menu == "Home":
        home()
    elif site_menu == "Watch all clocks":
        watch_all_clocks(site)
        sites(site)
    elif site_menu == "Reboot all clocks":
        connect(site,'','restart')
        watch_all_clocks(site)
        sites(site)
    elif site_menu == "Service":
        connect(site,'','service')
        back()
        sites(site)
    elif site_menu == "Credentials":
        get_creds(site)
        back()
        sites(site)
    elif site_menu == "Clocks":
        clocks(site)

def clocks(site):
    os.system('cls')
    clocks = clocks_menu(site)
    tmp_arr = []
    for item_1 in hosts:
        for item_2 in hosts[item_1]:
            if hosts[item_1][item_2]['description'] == clocks:
                one_clock(item_2,clocks,site)
            elif clocks == "Home":
                home()
            elif clocks == "Back":
                sites(site)

def one_clock(name, description,site):
    menu = one_clock_menu(name, description)
    if menu == 'Home':
        home()
    elif menu == "Restart":
        connect(site,name,'restart')
        back()
        one_clock(name,description,site)
    elif menu == "Logs":
        connect(site,name,'log')
        back()
        one_clock(name,description,site)
    elif menu == "Service":
        connect(site,name,'service')
        back()
        one_clock(name,description,site)
    elif menu == "Credentials":
        get_creds(site,name)
        back()
        one_clock(name,description,site)
    elif menu == "Watch":
        print("Remember to close VNC window to exit!")
        os.system(hosts[site][name]['vnc'])
        one_clock(name,description,site)
    elif menu == "Back":
        clocks(site)

def watch_all_clocks(site):
    os.system('cls')
    print("To proceed to next clock, close current clock window")
    for item in hosts[site]:
        print("You are now watching: ", hosts[site][item]['description'])
        os.system(hosts[site][item] ['vnc'])
    sites(site)

def back():
    menu = back_menu()
    print(menu)
    if menu == "Back":
        return


if __name__ == '__main__':
    home()
