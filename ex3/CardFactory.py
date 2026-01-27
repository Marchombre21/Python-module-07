# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    CardFactory.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 15:27:49 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 15:27:50 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from abc import ABC, abstractmethod
from ex0 import Card


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass
