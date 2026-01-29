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
    Rarity,
    ArtifactsEffects
)


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 durability: int, effect: ArtifactsEffects):
        super().__init__(name, cost, rarity)
        self.__durability: int = durability
        self.__effect: ArtifactsEffects = effect
        self.__type: str = "Artifact"

    def play(self, game_state: dict) -> dict:
        super().play(game_state)
        owner: Player = self.get_owner()
        if self.is_playable(owner.get_mana()):
            owner.remove_card(self)
            owner.set_mana(-self.get_cost())
            print(f"Playable: True, Name: {self.get_name()}, Cost:"
                  f" {self.get_cost()}, New {owner.get_name()}'s mana points:"
                  f" {owner.get_mana()}")
            game_state.setdefault("on_board", []).append(self)
            owner.add_effects(self.__effect)
        return {'card_played': self.get_name(), 'mana_used': self.get_cost(),
                'effect': self.__effect}

    def activate_ability(self) -> dict:
        owner: Player = self.get_owner()
        self.__durability -= 1
        match self.__effect:
            case "Permanent: +1 mana per turn":
                owner.set_mana(1)
            case "Permanent: +1 HP per turn":
                (owner.healing(1))
        if self.__durability <= 0:
            owner.remove_effects(self.__effect)
        return {"name": self.get_name(), "effect": self.__effect.value}

    def get_type(self) -> str:
        return self.__type
