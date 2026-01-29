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
    Rarity,
    GameErrors
)
from ex4 import DoubleError
from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


class BoycottedTournamentError(GameErrors):
    pass


def main():
    creatures = [
            {
                "name": "Fire Dragon",
                "cost": 5,
                "id": "dragon__001",
                "rarity": Rarity.LEGENDARY,
                "attack": 7,
                "health": 5,
                "defense": 5,
            },
            {
                "name": "Goblin Warrior",
                "cost": 2,
                "id": "goblin__001",
                "rarity": Rarity.COMMON,
                "attack": 2,
                "health": 1,
                "defense": 0,
            },
            {
                "name": "Ice Wizard",
                "cost": 4,
                "id": "wizard__001",
                "rarity": Rarity.RARE,
                "attack": 3,
                "health": 4,
                "defense": 2,
            },
            {
                "name": "Lightning Elemental",
                "cost": 3,
                "id": "elemental__001",
                "rarity": Rarity.UNCOMMON,
                "attack": 4,
                "health": 2,
                "defense": 1,
            },
            {
                "name": "Stone Golem",
                "cost": 6,
                "id": "golem__001",
                "rarity": Rarity.RARE,
                "attack": 5,
                "health": 8,
                "defense": 2,
            },
            {
                "name": "Shadow Assassin",
                "cost": 3,
                "id": "assassin__001",
                "rarity": Rarity.UNCOMMON,
                "attack": 5,
                "health": 2,
                "defense": 0,
            },
            {
                "name": "Healing Angel",
                "cost": 4,
                "id": "angel__001",
                "rarity": Rarity.RARE,
                "attack": 2,
                "health": 6,
                "defense": 2,
            },
            {
                "name": "Forest Sprite",
                "cost": 1,
                "id": "sprite__001",
                "rarity": Rarity.COMMON,
                "attack": 1,
                "health": 1,
                "defense": 1,
            },
        ]
    try:
        print("\n=== DataDeck Tournament Platform ===")
        platform: TournamentPlatform = TournamentPlatform()
        print("\nRegistering Tournament Cards...")
        count = 0
        while count < 5 and len(platform.get_ids()) < len(creatures):
            creature = random.choice(creatures)
            count += 1
            try:
                result = platform.register_card(TournamentCard(
                    creature["name"],
                    creature["cost"],
                    creature["rarity"],
                    creature["id"],
                    creature["attack"],
                    creature["defense"],
                    creature["health"]
                    ))
                print(result)
            except DoubleError as e:
                print(e)
                count -= 1
        print("\nCreating tournament match...")
        try:
            for i in range(5):
                ids_creatures = platform.get_ids()
                if len(ids_creatures) > 2:
                    first: str = random.choice(ids_creatures)
                    ids_creatures.remove(first)
                    second: str = random.choice(ids_creatures)
                    print("\nFight", i + 1)
                    print(platform.create_match(first, second))
                else:
                    raise BoycottedTournamentError("Not enough participants to"
                                                   " fighting")
        except GameErrors as e:
            print(e)
        print("\nTournament Leaderboard")
        for i, card in enumerate(platform.get_leaderboard()):
            print(f"{i + 1}. {card}")
        print("\nPlatform Report")
        print(platform.generate_tournament_report())
        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except GameErrors as e:
        print(e)


if __name__ == "__main__":
    main()
