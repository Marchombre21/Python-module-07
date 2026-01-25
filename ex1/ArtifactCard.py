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
    Player
)


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, type_card: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity, type_card)
        self.__durability = durability
        self.__effect = effect

    def play(self, game_state: dict, owner: Player) -> dict:
        super().play(game_state, owner)
