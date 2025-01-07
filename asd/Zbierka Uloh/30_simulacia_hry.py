'''
30. Simulácia hry [3 body]
Napíšte program, ktorý:
a) Simuluje hru „Kameň, papier, nožnice“ medzi používateľom a počítačom.
b) Sleduje skóre hráča a počítača.
c) Po každom kole zobrazí štatistiku a umožní pokračovať alebo ukončiť hru.
'''

import random

def print_score(p_score, c_score, round_counter):
    print(f"\n====== Skóre - kolo {round_counter} ======")
    print(f"Hráč: {p_score}")
    print(f"Počítač: {c_score}")

def comp_win(c_score, round_counter):
    print("\nPočítač vyhral!")
    c_score += 1
    round_counter += 1
    return c_score, round_counter

def player_win(p_score, round_counter):
    print("\nHráč vyhral!")
    p_score += 1
    round_counter += 1
    return p_score, round_counter

def play_round(player_score, comp_score, round_counter):
    choices = ['kamen', 'papier', 'noznice']
    comp_pick = random.choice(choices)
    player_pick = input("Zadajte, čo chcete hrať (kamen, papier, noznice): ").lower()
    
    while player_pick not in choices:
        player_pick = input("Prosím zadajte správny vstup (kamen, papier, noznice): ").lower()

    print(f"\nPočítač vybral: {comp_pick}")
    print(f"Hráč vybral: {player_pick}")

    match (player_pick, comp_pick):
        case (player, comp) if player == comp:
            print("Remíza!")
        case ("kamen", "papier"):
            comp_score, round_counter = comp_win(comp_score, round_counter)
        case ("papier", "noznice"):
            comp_score, round_counter = comp_win(comp_score, round_counter)
        case ("noznice", "kamen"):
            comp_score, round_counter = comp_win(comp_score, round_counter)
        case _:
            player_score, round_counter = player_win(player_score, round_counter)
    
    print_score(player_score, comp_score, round_counter)
    return player_score, comp_score, round_counter


choices = ['kamen', 'papier', 'noznice']
ans = 'a'
player_score = 0
comp_score = 0
round_counter = 0

print("======= Kameň-Papier-Nožnice =======")

while ans == 'a':
    player_score, comp_score, round_counter = play_round(player_score, comp_score, round_counter)
    ans = input("Chcete si zahrať ďalšie kolo? (a/n): ").lower()
    print("\n")

print("\nĎakujem za hru!")