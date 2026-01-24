# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    Card.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/24 07:35:41 by bfitte            #+#    #+#             #
#    Updated: 2026/01/24 07:35:42 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from abc import ABC, abstractmethod


class GameErrors(Exception):
    def __init__(self, details: str | None = None):
        message: str = details
        super().__init__(message)


class NegativeValue(GameErrors):
    def __init__(self, value_name: str):
        details: str = f"The {value_name} can't be negative."
        super().__init__(details)


class EmptyValue(GameErrors):
    def __init__(self, value_name: str):
        details: str = f"The {value_name} can't be empty."
        super().__init__(details)


class Player:
    def __init__(self, PV: int, name: str):
        if PV < 0:
            raise NegativeValue("PV")
        if name == "":
            raise EmptyValue("name")
        self.__name: str = name.capitalize()
        self.__PV: int = PV
        self.__cards: list["Card"] = []
        self.__mana: int = 6

    def add_card(self, card: "Card") -> None:
        self.__cards.append(card)

    def get_mana(self) -> int:
        return self.__mana

    def get_health(self) -> int:
        return self.__PV

    def get_name(self) -> str:
        return self.__name

    def set_mana(self, quantity: int) -> None:
        """Add or remove mana from stocks.

        Args:
            quantity (int): There will have a check before to verify
            if there is enough mana to do this action but I add a
            condition anyway.
        """
        if self.__mana + quantity < 0:
            self.__mana = 0
        else:
            self.__mana += quantity

    def damage(self, damages: int) -> bool:
        if damages < 0:
            raise NegativeValue("damages")
        self.__PV -= damages
        return self.__PV <= 0


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str, type: str):
        self.__name = name
        self.__cost = cost
        self.__rarity = rarity
        self.__type = type

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self.__name, "cost":
                self.__cost, "rarity": self.__rarity, "type": self.__type}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.__cost

    def get_cost(self):
        return self.__cost

    def get_name(self):
        return self.__name
