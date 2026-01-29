# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    EliteCard.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 13:50:10 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 13:50:11 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex0 import (
    Card,
    NegativeValue,
    EmptyValue,
    Rarity
)
from ex2 import (
    Combatable,
    Magical
)


class EliteCard(Card, Combatable, Magical):
    """An elite class that combine an abstract class (Card) and two interfaces
    (Combatable and Magical)
    """
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 attack: int, defense: int, mana: int, health: int):
        super().__init__(name, cost, rarity)
        if not isinstance(name, str) or\
           not isinstance(rarity, str):
            raise ValueError("Name and rarity must be strings")
        if not isinstance(cost, int) or\
           not isinstance(attack, int) or\
           not isinstance(mana, int) or\
           not isinstance(health, int) or\
           not isinstance(defense, int):
            raise ValueError("Cost, attack, mana, health and defense must"
                             " be integers")
        if name == "":
            raise EmptyValue("name")
        if rarity == "":
            raise EmptyValue("rarity")
        self.__attack: int = attack
        self.__defense: int = defense
        self.__mana: int = mana
        self.__health: int = health
        self.__type: str = "Elite"

    def play(self, game_state: dict) -> dict:
        super().play(game_state)
        return {"type": "A dictionnary", "why": "Because"}

    def attack(self, target: Card) -> dict:
        if not isinstance(target, Card):
            raise ValueError("The target of an attack must be a card")
        print(f"Attack result: 'attacker': {self.get_name()}, 'target':"
              f" {target.get_name()}, 'damage': {self.get_attack()},"
              f"'combat_type': 'melee'")
        return target.defend(self.get_attack())

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise ValueError("Damages must be integers")
        if incoming_damage < 0:
            raise NegativeValue("damages")
        damages = incoming_damage - self.get_defense()
        defense = max(incoming_damage - damages, 0)
        alive = damages < self.get_health()
        return {'defender': self.get_name(), 'damage_taken': damages,
                'damage_blocked': defense, 'still_alive': alive}

    def get_combat_stats(self) -> dict:
        return {"summary": "It's a dict that summarize combat stats", "reason":
                "Rules are a little (very) unclear"}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if spell_name == "":
            raise EmptyValue("spell_name")
        return {'caster': self.get_name(), 'spell': spell_name,
                'targets': targets, 'mana_used': 4}

    def channel_mana(self, amount: int) -> dict:
        return {'channeled': amount, 'total_mana': self.get_mana()}

    def get_magic_stats(self) -> dict:
        return {"summary": "It's a dict that summarize magic stats", "reason":
                "Rules are a little (very) unclear"}

    def set_attack(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("You can't modify the attack value with"
                             " something else than an int")
        self.__attack += value

    def set_defense(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("You can't modify the defense value with"
                             " something else than an int")
        self.__defense += value

    def set_health(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("You can't modify the health value with"
                             " something else than an int")
        self.__health += value

    def set_mana(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("You can't modify the mana value with"
                             " something else than an int")
        self.__mana += value

    def get_attack(self) -> int:
        return self.__attack

    def get_defense(self) -> int:
        return self.__defense

    def get_mana(self) -> int:
        return self.__mana

    def get_health(self) -> int:
        return self.__health

    def get_type(self) -> str:
        return self.__type
