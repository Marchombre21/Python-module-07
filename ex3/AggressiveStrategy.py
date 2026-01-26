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

class AgressiveStrategy(GameStrategy):
    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda x: x != "Enemy Player")

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        

    def get_strategy_name(self) -> str:
        return self.__class__.__name__