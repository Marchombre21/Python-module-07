# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    TournamentCard.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/28 13:18:29 by bfitte            #+#    #+#             #
#    Updated: 2026/01/28 13:18:30 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex0 import Card, TypeCard, Rarity, NegativeValue
from ex2 import Combatable
from ex4 import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        id: str,
        type_card: TypeCard,
        attack: int,
        defense: int,
        health: int,
    ):
        super().__init__(name, cost, rarity, type_card)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("Defense must be a positive integer")
        if not isinstance(id, str) or id == "":
            raise ValueError("Id must be a non-empty string")
        self.__wins: int = 0
        self.__losses: int = 0
        self.__id: str = id
        self.__attack: int = attack
        self.__defense: int = defense
        self.__health: int = health

    def play(self, game_state: dict) -> dict:
        super().play(game_state)
        if self.is_playable(game_state["mana"]):
            print("Playable: True")
            game_state["on_board"].append(self)
            game_state["mana"] -= self.get_cost()
            return {
                "card_played": self.get_name(),
                "mana_used": self.get_cost(),
                "effect": "Creature summoned to battlefield",
            }
        else:
            print("Playable: False")
            return {
                "card_almost_played": self.get_name(),
                "mana_almost_used": self.get_cost(),
            }

    def attack(self, target: "TournamentCard") -> dict:
        if not isinstance(target, type(self)):
            raise ValueError("The target must be a TournamentCard")
        print(
            f"\nAttack result: 'attacker': {self.get_name()}, 'target':"
            f" {target.get_name()}, 'damage': {self.get_attack()},"
            f"'combat_type': 'melee'"
        )
        return target.defend(self.get_attack())

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise ValueError("Damages must be integers")
        if incoming_damage < 0:
            raise NegativeValue("damages")
        damages = max(incoming_damage - self.get_defense(), 0)
        alive = damages < self.get_health()
        return {
            "defender": self.get_name(),
            "damage_taken": damages,
            "damage_blocked": self.get_defense(),
            "still_alive": alive,
        }

    def get_combat_stats(self) -> dict:
        return {
            "summary": "It's a dict that summarize combat stats",
            "reason": "Rules are a little (very) unclear",
        }

    def calculate_rating(self) -> int:
        rating = max(1200 + 16 * self.__wins - self.__losses * 7, 0)
        return rating

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int):
            raise ValueError("You only can update wins with integers")
        self.__wins += wins

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int):
            raise ValueError("You only can update losses with integers")
        self.__losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.get_name(),
            "id": self.get_id(),
            "interfaces": self.get_inheritance(),
            "rating": self.calculate_rating(),
            "wins": self.__wins,
            "losses": self.__losses,
        }

    def get_id(self) -> str:
        return self.__id

    def get_inheritance(self) -> list:
        return [cls.__name__ for cls in self.__class__.__bases__]

    def get_defense(self) -> int:
        return self.__defense

    def get_attack(self) -> int:
        return self.__attack

    def get_health(self) -> int:
        return self.__health
