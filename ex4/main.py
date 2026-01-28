# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/28 16:51:45 by bfitte            #+#    #+#             #
#    Updated: 2026/01/28 16:51:46 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

import random
from ex0 import (
    TypeCard,
    Rarity,
    GameErrors
)
from ex4 import (
    TournamentPlatform,
    TournamentCard,
    DoubleError
)


def main():
    creatures = [
            {
                "name": "Fire Dragon",
                "cost": 5,
                "id": "dragon__001",
                "type_card": TypeCard.CREATURE,
                "rarity": Rarity.LEGENDARY,
                "attack": 7,
                "health": 5,
                "defense": 5,
            },
            {
                "name": "Goblin Warrior",
                "cost": 2,
                "id": "goblin__001",
                "type_card": TypeCard.CREATURE,
                "rarity": Rarity.COMMON,
                "attack": 2,
                "health": 1,
                "defense": 0,
            },
            {
                "name": "Ice Wizard",
                "cost": 4,
                "id": "wizard__001",
                "type_card": TypeCard.CREATURE,
                "rarity": Rarity.RARE,
                "attack": 3,
                "health": 4,
                "defense": 2,
            },
            {
                "name": "Lightning Elemental",
                "cost": 3,
                "id": "elemental__001",
                "type_card": TypeCard.CREATURE,
                "rarity": Rarity.UNCOMMON,
                "attack": 4,
                "health": 2,
                "defense": 1,
            },
            {
                "name": "Stone Golem",
                "cost": 6,
                "id": "golem__001",
                "type_card": TypeCard.CREATURE,
                "rarity": Rarity.RARE,
                "attack": 5,
                "health": 8,
                "defense": 2,
            },
            {
                "name": "Shadow Assassin",
                "cost": 3,
                "id": "assassin__001",
                "type_card": TypeCard.CREATURE,
                "rarity": Rarity.UNCOMMON,
                "attack": 5,
                "health": 2,
                "defense": 0,
            },
            {
                "name": "Healing Angel",
                "cost": 4,
                "id": "angel__001",
                "type_card": TypeCard.CREATURE,
                "rarity": Rarity.RARE,
                "attack": 2,
                "health": 6,
                "defense": 2,
            },
            {
                "name": "Forest Sprite",
                "cost": 1,
                "id": "sprite__001",
                "type_card": TypeCard.CREATURE,
                "rarity": Rarity.COMMON,
                "attack": 1,
                "health": 1,
                "defense": 1,
            },
        ]
    try:
        platform: TournamentPlatform = TournamentPlatform()
        for i in range(5):
            creature = random.choice(creatures)
            try:
                platform.register_card(TournamentCard(
                    creature["name"],
                    creature["cost"],
                    creature["rarity"],
                    creature["id"],
                    creature["type_card"],
                    creature["attack"],
                    creature["defense"],
                    creature["health"]
                    ))
            except DoubleError as e:
                print(e)
                i -= 1
        for _ in range(5):
            ids_creatures = platform.get_ids()
            first: str = random.choice(ids_creatures)
            ids_creatures.remove(first)
            second: str = random.choice(ids_creatures)
            print(platform.create_match(first, second))
    except GameErrors as e:
        print(e)


if __name__ == "__main__":
    main()
