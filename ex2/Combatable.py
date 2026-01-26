# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    Combatable.py                                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 12:44:49 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 12:44:50 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from abc import ABC, abstractmethod
from ex0 import Card


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Card) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
