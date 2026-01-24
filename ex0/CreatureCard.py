# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    CreatureCard.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/24 07:48:54 by bfitte            #+#    #+#             #
#    Updated: 2026/01/24 07:48:55 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex0.Card import Card, Player, GameErrors


class VictoryError(GameErrors):
    def __init__(self, name: str):
        details = f"Victory of {name}!!!"
        super().__init__(details)


class Creature(Card):
    def __init__(self, name: str, cost: int, rarity: str, type: str,
                 attack: int, health: int, defense: int):
        super().__init__(name, cost, rarity, type)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("Defense must be a positive integer")
        self.__attack: int = attack
        self.__health: int = health
        self.__defense: int = defense
        self.__graveyard: bool = False
        self.__owner: Player | None = None

    def play(self, game_state: dict, owner: Player) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dictionnnary")
        if not isinstance(owner, Player):
            raise ValueError("Who is playing?")
        if self.is_playable(owner.get_mana()):
            print("Playable: True")
            game_state["on_board"].append(self)
            owner.set_mana(-self.get_cost())
            self.set_owner(owner)
            return {'card_played': self.get_name(), 'mana_used':
                    self.get_cost(), 'remaining mana': owner.get_mana(),
                    'effect': 'Creature summoned to battlefield'}
        else:
            print("Playable: False")
            return {'card_almost_played': self.get_name(), 'mana_almost_used':
                    self.get_cost(), "user's mana": owner.get_mana()}

    def attack_target(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dictionnnary")
        on_board: list[Card] = [card for card in game_state["on_board"] if
                                card.get_owner() != self.get_owner()]
        if len(on_board) > 0:
            for card in on_board:
                if isinstance(card, Creature):
                    if self.duel(card):
                        game_state["on_board"].remove(card)
                        card.turn_to_death()
                        damages: int = self.__attack - card.get_defense()\
                            - card.get_health()
                        if card.get_owner().damage(damages):
                            raise VictoryError(self.__owner.get_name())
                        return {'attacker': self.get_name(), 'target':
                                card.get_name(), 'damage_dealt': damages,
                                'combat_resolved': True}
                    else:
                        return {'attacker': self.get_name(), 'target':
                                card.get_name(), 'damage_dealt': 0,
                                'combat_resolved': False}
        else:
            ennemy: Player = [player for player in game_state["players"]
                              if player.get_name() !=
                              self.__owner.get_name()][0]
            if ennemy.damage(self.__attack):
                raise VictoryError(self.__owner.get_name())
            return {'attacker': self.get_name(), 'target':
                    ennemy.get_name(), 'damage_dealt': self.__attack}

    def get_defense(self) -> int:
        return self.__defense

    def turn_to_death(self) -> None:
        self.__graveyard = True

    def get_health(self) -> int:
        return self.__health

    def duel(self, ennemy: "Creature") -> bool:
        return self.__attack - ennemy.get_defense() >= ennemy.get_health()

    def get_card_info(self) -> dict:
        result = super().get_card_info()
        result["attack"] = self.__attack
        result["defense"] = self.__defense
        return result

    def get_owner(self) -> Player:
        return self.__owner

    def set_owner(self, player: Player) -> None:
        self.__owner = player
