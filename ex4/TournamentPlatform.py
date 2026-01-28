# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    TournamentPlatform.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/28 15:16:34 by bfitte            #+#    #+#             #
#    Updated: 2026/01/28 15:16:35 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex4 import TournamentCard
from ex0 import GameErrors


class DoubleError(GameErrors):
    pass


class TournamentPlatform():
    def __init__(self):
        self.__registered_cards: list[TournamentCard] = []
        self.__total_matchs: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("All participants must be TournamentCards")
        if card.get_id() in [card.get_id() for card in
                             self.__registered_cards]:
            raise DoubleError("Impossible to register two participants with "
                              "same id.")
        res = card.get_rank_info()
        self.__registered_cards.append(card)
        result: str = (
            f"{res['name']} (ID: {res['id']}):\n"
            f"- Interfaces: {res['interfaces']}\n"
            f"-Rating: {res['rating']}\n"
            f"- Record: {res['wins']}-{res['losses']}"
        )
        return result

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.__total_matchs += 1
        if not isinstance(card1_id, str) or card1_id == "":
            raise ValueError("All id must be non-empty strings")
        if not isinstance(card2_id, str) or card2_id == "":
            raise ValueError("All id must be non-empty strings")
        first: TournamentCard = [card for card in self.__registered_cards if
                                 card.get_id() == card1_id][0]
        second: TournamentCard = [card for card in self.__registered_cards if
                                  card.get_id() == card2_id][0]
        result_match: dict = {}
        result_fight: dict = first.attack(second)
        print("Defense result:", result_fight)
        if result_fight["still_alive"]:
            result_fight = second.attack(first)
            print("Defense result:", result_fight)
            if result_fight["still_alive"]:
                result_match = {"winner": "no one", "loser": "non one",
                                "winner_rating": "no change", "loser_rating":
                                "no change"}
            else:
                first.update_losses(1)
                second.update_wins(1)
                result_match = {"winner": second.get_id(), "loser":
                                first.get_id(), "winner_rating":
                                second.calculate_rating(),
                                "loser_rating": first.calculate_rating()}
        else:
            second.update_losses(1)
            first.update_wins(1)
            result_match = {"winner": first.get_id(), "loser":
                            second.get_id(), "winner_rating":
                            first.calculate_rating(),
                            "loser_rating": second.calculate_rating()}
        return result_match

    def get_ids(self) -> list[str]:
        return [card.get_id() for card in self.__registered_cards]
