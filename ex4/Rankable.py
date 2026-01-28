# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    Rankable.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/28 13:15:37 by bfitte            #+#    #+#             #
#    Updated: 2026/01/28 13:15:38 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from abc import ABC, abstractmethod


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
