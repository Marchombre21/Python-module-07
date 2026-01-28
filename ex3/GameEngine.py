# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    GameEngine.py                                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/28 09:41:47 by bfitte            #+#    #+#             #
#    Updated: 2026/01/28 09:41:48 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex1 import (
    Player
)


class GameEngine:
    def __init__(self, game_state: dict):
        self.__factory: CardFactory | None = None
        self.__strategy: GameStrategy | None = None
        self.__nb_turn: int = 0
        self.__total_damages: int = 0
        self.__total_cards: int = 0
        self.__game_state: dict = game_state
        self.__player_turn: Player = game_state["players"][0]

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy
            ) -> None:
        self.__factory = factory
        self.__strategy = strategy
        print("Factory:", self.__factory.get_name())
        print("Strategy: ", self.__strategy.get_strategy_name())
        print("Available types:")
        for card in self.__factory.get_supported_types().values():
            print(card)
        for player in self.__game_state["players"]:
            factory.create_themed_deck(12, player)
            for _ in range(6):
                player.get_deck().draw_card()

    def simulate_turn(self) -> dict:
        self.__nb_turn += 1
        self.__player_turn.get_deck().draw_card()
        self.__player_turn.set_mana(2)
        resume = self.__strategy.execute_turn(self.__player_turn.get_hand(),
                                              self.__game_state["on_board"])
        self.__total_damages += resume["damage_dealt"]
        self.__total_cards += len(resume["cards_played"])
        self.__player_turn = [player for player in
                              self.__game_state["players"] if player !=
                              self.__player_turn][0]
        return resume

    def get_engine_status(self) -> dict:
        return {'turns_simulated': self.__nb_turn, 'strategy_used':
                self.__strategy.get_strategy_name(), 'total_damage':
                self.__total_damages, 'cards_created': self.__total_cards}
