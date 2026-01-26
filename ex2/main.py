# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 14:24:47 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 14:24:48 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex2 import EliteCard
from ex0.Card import GameErrors


def main():
    try:
        print("\n=== DataDeck Ability System ===\n")
        print("EliteCard capabilities:")
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
        print("\nPlaying Arcane Warrior (Elite Card):\n")
        arcane_warrior1 = EliteCard("Arcane Warrior", 5, "rare", "elite",
                                    5, 2, 8, 20)
        arcane_warrior2 = EliteCard("Arcane Warrior", 5, "rare", "elite",
                                    5, 2, 8, 20)
        print("Combat phase:")
        print(arcane_warrior1.attack(arcane_warrior2))
        print("\nMagic phase:")
        name = arcane_warrior1.get_name()
        print("Spell cast:", arcane_warrior2.cast_spell("Fireball",
                                                        [name]))
        print("Mana channel:", arcane_warrior1.channel_mana(3))
        print("\nMultiple interface implementation successful!")
    except (Exception, GameErrors) as e:
        print(e)


if __name__ == "__main__":
    main()
