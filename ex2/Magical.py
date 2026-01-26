# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    Magical.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 13:47:26 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 13:47:27 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list):
        pass

    @abstractmethod
    def channel_mana(self, amount: int):
        pass

    @abstractmethod
    def get_magic_stats(self):
        pass
