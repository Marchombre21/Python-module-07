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
    def __init__(self, name: str, cost: int, rarity: str, type_card: str,
                 attack: int, health: int, defense: int):
        super().__init__(name, cost, rarity, type_card)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("Defense must be a positive integer")
        self.__attack: int = attack
        self.__health: int = health
        self.__defense: int = defense
        self.__owner: Player | None = None

    def play(self, game_state: dict, owner: Player) -> dict:
        """If the player have enough mana points, the card will be added to
        the board, awarded to the owner and the cost will be substract from the
        owner's mana points

        Args:
            game_state (dict): The dict that lists the current states of
            the game.
            owner (Player): The player who play this card

        Returns:
            dict: The summary of the invocation
        """
        super().play(game_state, owner)
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
        """This card attack the opposing player. First, she attack the
        creatures who defend the opposing player

        Args:
            game_state (dict): The dict that lists the current states of
            the game.

        Returns:
            dict: The summary of the attack in key/value format
        """
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dictionnnary")
        on_board: list[Card] = [card for card in game_state["on_board"] if
                                card.get_owner() != self.get_owner()]
        if len(on_board) > 0:
            for card in on_board:
                if isinstance(card, Creature):
                    if self.duel(card):
                        game_state["on_board"].remove(card)
                        card.discard_pile()
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

    def get_health(self) -> int:
        return self.__health

    def duel(self, ennemy: "Creature") -> bool:
        """Compare attack minus ennemy's defense with ennemy's health.

        Args:
            ennemy (Creature): The instance of the opposing creature

        Returns:
            bool: True if this creature kill the opposing
        """
        return self.__attack - ennemy.get_defense() >= ennemy.get_health()

    def get_card_info(self) -> dict:
        result = super().get_card_info()
        result["attack"] = self.__attack
        result["defense"] = self.__defense
        return result

    def get_owner(self) -> Player:
        """Return the owner of this card
        """
        return self.__owner

    def set_owner(self, player: Player) -> None:
        """Assign this card to a player
        """
        self.__owner = player
