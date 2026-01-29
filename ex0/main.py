# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/24 14:52:50 by bfitte            #+#    #+#             #
#    Updated: 2026/01/24 14:52:51 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex0 import Player, CreatureCard, GameErrors


def main():
    try:
        print("\n=== DataDeck Card Foundation ===\n")
        game_state = {}
        bruno = Player(20, "bruno")
        gildas = Player(20, "gildas")
        game_state["players"] = [bruno, gildas]
        game_state["on_board"] = []
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 20, 5)
        goblin = CreatureCard("Goblin", 2, "Common", 1, 5, 0)
        dragon.set_owner(bruno)
        bruno.add_card(dragon)
        goblin.set_owner(gildas)
        gildas.add_card(goblin)
        print("Testing Abstract Base Class Design:\n")
        print("CreatureCard Info:")
        print(dragon.get_card_info())
        print("\nPlaying Fire Dragon with 6 mana available:")
        print("Play result:", dragon.play(game_state))
        print("\nPlaying Goblin with 6 mana available:")
        print("Play result:", goblin.play(game_state))
        print("\nFire Dragon attacks Goblin Warrior:")
        print(dragon.attack_target(game_state))
        print("\nTesting insufficient mana (4 available):")
        dragon2 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 20, 5)
        dragon2.set_owner(gildas)
        gildas.add_card(dragon2)
        print(dragon2.play(game_state))
        print("\nAbstract pattern successfully demonstrated!")
    except (GameErrors, Exception) as e:
        print(e)


if __name__ == "__main__":
    main()
