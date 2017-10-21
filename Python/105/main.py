#!/usr/bin/env python3
from char import Character, Npc, Boss


def main():
    c1 = Character()
    npcs = [Npc("Mob of Madness", 15), Npc(), Boss()]
    c1.speak("Sup?")
    [npc.speak("Yo") for npc in npcs]
    [npc.damage(10) for npc in npcs]
    [npc.speak("No") for npc in npcs]


if __name__ == '__main__':
    main()
