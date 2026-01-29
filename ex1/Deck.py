# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    Deck.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 07:28:17 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 07:28:18 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

import random

from ex0 import (
    Card,
    NegativeValue,
    EmptyValue,
    ArtifactsEffects,
    GameErrors
)


class EmptyDeck(GameErrors):
    pass


class Player:
    def __init__(self, PV: int, name: str):
        if PV < 0:
            raise NegativeValue("PV")
        if name == "":
            raise EmptyValue("name")
        self.__name: str = name.capitalize()
        self.__PV: int = PV
        self.__deck: "Deck" | None = None
        self.__hand: list[Card] = []
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

    def get_hand(self) -> list[Card]:
        return self.__hand

    def get_mana(self) -> int:
        return self.__mana

    def get_health(self) -> int:
        return self.__PV

    def get_name(self) -> str:
        return self.__name

    def add_deck(self, deck: "Deck") -> None:
        self.__deck = deck

    def get_deck(self) -> "Deck" | None:
        return self.__deck

    def get_defense(self) -> int:
        return self.__defense

    def add_effects(self, effect: ArtifactsEffects):
        self.__effects.append(effect)

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
                print(f"\nMana added succesfully! New {self.__name}'s mana"
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


class Deck:
    def __init__(self, owner: Player):
        self.__owner: Player = owner
        self.__content: list = []
        owner.add_deck(self)

    def get_owner(self) -> Player:
        return self.__owner

    def get_content(self) -> list:
        return self.__content

    def add_card(self, card: Card) -> None:
        self.__content.append(card)
        card.set_owner(self.__owner)

    def remove_card(self, card_name: str) -> bool:
        card: Card = [card_rm for card_rm in self.__content if
                      card_rm.get_name() == card_name][0]
        try:
            self.__content.remove(card)
        except ValueError:
            return False
        return True

    def shuffle(self) -> None:
        random.shuffle(self.__content)

    def draw_card(self) -> Card:
        try:
            card = self.__content.pop(0)
            self.__owner.add_card(card)
            return card
        except IndexError:
            raise EmptyDeck("Your deck is empty, you"
                            f" ({self.__owner.get_name()}) lose.")

    def get_deck_stats(self) -> dict:
        nb_creatures: int = 0
        nb_spells: int = 0
        nb_artifacts: int = 0
        avg: float = 0
        for card in self.__content:
            avg += card.get_cost()
            match card.__class__.__name__:
                case "CreatureCard":
                    nb_creatures += 1
                case "ArtifactCard":
                    nb_artifacts += 1
                case "SpellCard":
                    nb_spells += 1
        avg /= len(self.__content)
        return {'total_cards': len(self.__content), 'creatures': nb_creatures,
                'spells': nb_spells, 'artifacts': nb_artifacts,
                'avg_cost': round(avg, 2)}
