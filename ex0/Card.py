# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    Card.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/28 17:37:53 by bfitte            #+#    #+#             #
#    Updated: 2026/01/28 17:37:54 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#


from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"
    UNCOMMON = "Uncommon"


class SpellsEffects(Enum):
    DAMAGES = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class ArtifactsEffects(Enum):
    MANA = "Permanent: +1 mana per turn"
    HEALTH = "Permanent: +1 HP per turn"
    ATTACK = "Permanent: +2 attack to equipped creature"
    DRAW = "Permanent: Draw an extra card each turn"
    COST = "Permanent: +1 cost reduction to all cards"


class GameErrors(Exception):
    """An error class to handle all kind of errors with subclasses
    """
    def __init__(self, details: str | None = None):
        message: str | None = details
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
        self.__hand: list = []
        self.__mana: int = 6
        self.__defense: int = 0
        self.__effects: list[ArtifactsEffects] = []

    def add_card(self, card: "Card") -> None:
        """Add played card in player's hand

        Args:
            card (Card): An instance of the played card
        """
        self.__hand.append(card)

    def remove_card(self, card: "Card") -> None:
        self.__hand.remove(card)

    def get_mana(self) -> int:
        return self.__mana

    def get_health(self) -> int:
        return self.__PV

    def get_name(self) -> str:
        return self.__name

    def add_deck(self, deck: list) -> None:
        self.__hand = deck

    def get_defense(self) -> int:
        return self.__defense

    def add_effects(self, effect: ArtifactsEffects):
        self.__effects.append(effect)

    def remove_effects(self, effect: ArtifactsEffects):
        try:
            self.__effects.remove(effect)
        except ValueError as e:
            raise ValueError(e)

    def set_defense(self, modification: int) -> None:
        """Modify player's defense points. When he gets some damages we
        decrease (or increase) them by the defense value

        Raises:
            ValueError: Impossible to change an int by a no-int value.
        """
        if not isinstance(modification, int):
            raise ValueError("If you want to modify defense points, you have"
                             " to do that with an int value")
        self.__defense += modification

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
            if quantity >= 0:
                print(f"\nMana added successfully! New {self.__name}'s mana"
                      f" points: {self.__mana}\n")

    def healing(self, health_points: int) -> None:
        """Heal your player adding some health points to his HP

        Args:
            health_points (int): Quantity to add to his HP

        Raises:
            ValueError: Positive int value mandatory
        """
        if not isinstance(health_points, int) or health_points < 0:
            raise ValueError("If you want to healing your player, you have"
                             " to do that with a positive int value")
        self.__PV += health_points

    def damage(self, damages: int) -> bool:
        """deduct some health points according to damages quantity

        Args:
            damages (int): Quantity of points to deduct from health points

        Returns:
            bool: True if the player who suffer the damages is dead
        """
        if damages < 0:
            raise NegativeValue("damages")
        self.__PV -= max(damages - self.__defense, 0)
        return self.__PV <= 0


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 ):
        self.__name: str = name.capitalize()
        self.__cost: int = cost
        self.__rarity: Rarity = rarity
        self.__owner: Player | None = None

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """If the player have enough mana points, the card will be added to
        the board, awarded to the owner and the cost will be substract from the
        owner's mana points

        Args:
            game_state (dict): The dict that lists the current states of
            the game.
            owner (Player): The player who play this card

        Returns:
            dict: The summary of the invocation
        """
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dictionnnary")
        return {}

    @abstractmethod
    def get_type(self):
        pass

    def get_card_info(self) -> dict:
        """Return principals informations about the card

        Returns:
            dict: All informations in key/value format
        """
        return {"name": self.__name, "cost":
                self.__cost, "rarity": self.__rarity}

    def is_playable(self, available_mana: int) -> bool:
        """Check if the player have enough mana points to play this card

        Args:
            available_mana (int): Quantity of mana points
        """
        return available_mana >= self.__cost

    def get_cost(self) -> int:
        """Return the cost in mana points to play this card
        """
        return self.__cost

    def get_name(self) -> str:
        return self.__name

    def get_owner(self) -> Player:
        """Return the owner of this card
        """
        return self.__owner

    def set_owner(self, player: Player) -> None:
        """Assign this card to a player
        """
        self.__owner = player
