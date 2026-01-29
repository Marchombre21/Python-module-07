# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    AggressiveStrategy.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 15:31:53 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 15:31:54 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex3.GameStrategy import GameStrategy
from ex1 import Player
from ex0 import (
    Card,
    SpellsEffects
)


class AgressiveStrategy(GameStrategy):
    def __init__(self, game_state: dict):
        self.__game_state: dict = game_state

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Sort the list by putting the creatures with the fewest HP first

        :param available_targets: List of targets
        :type available_targets: list
        :return: return the sorted list
        :rtype: list
        """
        if len(available_targets) > 0:
            return sorted(available_targets, key=lambda x: x.get_health())
        else:
            return available_targets

    def execute_turn(self, hand: list[Card], battlefield: list) -> dict:
        """
        Assigns each player to a variable, then sort the battlefield according
        to strategy. At the begining, the player play his cards in hand,
        starting with low-cost creatures as long as he have enough mana.
        Then creatures attack.

        :param hand: Cards in player's hand
        :type hand: list[Card]
        :param battlefield: List of all cards on board
        :type battlefield: list
        :return: A dictionnary that summarize stats of the turn
        :rtype: dict
        """
        player_turn: Player = hand[0].get_owner()
        enemy: Player = [enemy for enemy in self.__game_state["players"] if
                         enemy != player_turn][0]
        self.prioritize_targets([card for card in battlefield if
                                 card.get_type() == "Creature"])
        result: dict = {'cards_played': [], 'mana_used': 0, 'targets_attacked':
                        set(), 'damage_dealt': 0, "Ennemy's HP remain":
                        enemy.get_health()}
        aggressive_hand: list = sorted(hand, key=lambda x: x.get_type() ==
                                       "Creature" and x.get_cost() < 4,
                                       reverse=True)
        print("\nHand:")
        for card in aggressive_hand:
            print(card.get_name())
        print()
        for card in aggressive_hand:
            if card.is_playable(player_turn.get_mana()):
                result["cards_played"].append(card.get_name())
                result["mana_used"] += card.get_cost()
                card.play(self.__game_state)
                if card.get_type() == "Spell":
                    if card.get_effect() == SpellsEffects.DAMAGES:
                        result["damage_dealt"] += 3
                        result["targets_attacked"].add(
                            enemy.get_name()
                            )
                        result["Ennemy's HP remain"] =\
                            enemy.get_health()
        for creature in [creature for creature in self.__game_state["on_board"]
                         if creature.get_owner() == player_turn and
                         creature.get_type() == "Creature"]:
            res = creature.attack_target(self.__game_state)
            result["damage_dealt"] += res["damage_dealt"]
            result["targets_attacked"].add(res["target"])
            result["Ennemy's HP remain"] = res["Ennemy's HP remain"]
        return result

    def get_strategy_name(self) -> str:
        return self.__class__.__name__
