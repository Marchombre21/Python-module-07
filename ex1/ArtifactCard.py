# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ArtifactCard.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/25 15:56:07 by bfitte            #+#    #+#             #
#    Updated: 2026/01/25 15:56:08 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex0 import (
    Card,
    Player,
    VictoryError,
    Rarity,
    TypeCard,
    ArtifactsEffects
)


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 type_card: TypeCard, durability: int,
                 effect: ArtifactsEffects):
        super().__init__(name, cost, rarity, type_card)
        self.__durability: int = durability
        self.__effect: ArtifactsEffects = effect

    def play(self, game_state: dict) -> dict:
        super().play(game_state)
        owner: Player = self.get_owner()
        if self.is_playable(owner.get_mana()):
            print("Playable: True")
            owner.set_mana(-self.get_cost())
            owner.add_effects(self.__effect)
        return {'card_played': self.get_name(), 'mana_used': self.get_cost(),
                'effect': self.__effect}

    def activate_ability(self, owner: Player) -> dict:
        self.__durability -= 1
        match self.__effect:
            case "Permanent: +1 mana per turn":
                owner.set_mana(1)
            case "Permanent: +1 HP per turn":
                if (owner.damage(1)):
                    raise VictoryError(owner.get_name())
        if self.__durability <= 0:
            owner.remove_effects(self.__effect)
