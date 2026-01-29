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

from .Card import Card, Player, GameErrors, Rarity


class VictoryError(GameErrors):
    def __init__(self, name: str):
        details = f"Victory of {name}!!!"
        super().__init__(details)


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 attack: int, health: int, defense: int):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("Defense must be a positive integer")
        self.__attack: int = attack
        self.__health: int = health
        self.__defense: int = defense
        self.__type: str = "Creature"

    def play(self, game_state: dict) -> dict:
        super().play(game_state)
        owner: Player = self.get_owner()
        if self.is_playable(owner.get_mana()):
            owner.remove_card(self)
            owner.set_mana(-self.get_cost())
            print(f"Playable: True, Name: {self.get_name()}, Cost:"
                  f" {self.get_cost()}, New {owner.get_name()}'s mana points:"
                  f" {owner.get_mana()}")
            game_state.setdefault("on_board", []).append(self)
            return {'card_played': self.get_name(), 'mana_used':
                    self.get_cost(), 'remaining mana': owner.get_mana(),
                    'effect': 'Creature summoned to battlefield'}
        else:
            print("Playable: False")
            return {'card_almost_played': self.get_name(), 'mana_almost_used':
                    self.get_cost(), "user's mana": owner.get_mana()}

    def get_type(self) -> str:
        return self.__type

    def attack_target(self, target: dict) -> dict:
        """This card attack the opposing player. First, she attack the
        creatures who defend the opposing player

        Args:
            target (dict): The dict that lists the current states of
            the game.

        Returns:
            dict: The summary of the attack in key/value format
        """
        if not isinstance(target, dict):
            raise ValueError("target must be a dictionnnary")
        on_board: list[Card] = [card for card in target.get("on_board", []) if
                                card.get_owner() != self.get_owner() and
                                card.get_type() == "Creature"]
        if len(on_board) > 0:
            for card in on_board:
                owner: Player = card.get_owner()
                if isinstance(card, CreatureCard):
                    if self.duel(card):
                        target["on_board"].remove(card)
                        damages: int = self.__attack - card.get_defense()\
                            - card.get_health()
                        if owner.damage(damages):
                            raise VictoryError(self.get_owner().get_name())
                        return {'attacker': self.get_name(), 'target':
                                card.get_name(), 'damage_dealt': damages,
                                'combat_resolved': True, "Ennemy's HP remain":
                                owner.get_health()}
                    else:
                        card.set_health(-(self.__attack - card.get_defense()))
                        return {'attacker': self.get_name(), 'target':
                                card.get_name(), 'damage_dealt':
                                self.__attack - card.get_defense(),
                                'combat_resolved': False, "Ennemy's HP remain":
                                owner.get_health()}
        else:
            ennemy: Player = [player for player in target["players"]
                              if player.get_name() !=
                              self.get_owner().get_name()][0]
            if ennemy.damage(self.__attack):
                raise VictoryError(self.get_owner().get_name())
            return {'attacker': self.get_name(), 'target':
                    ennemy.get_name(), 'damage_dealt': self.__attack,
                    "Ennemy's HP remain": ennemy.get_health()}
        return {}

    def get_defense(self) -> int:
        return self.__defense

    def get_health(self) -> int:
        return self.__health

    def set_health(self, quantity: int) -> None:
        if not isinstance(quantity, int):
            raise ValueError("You must use an int to modify health")
        self.__health += quantity

    def duel(self, ennemy: "CreatureCard") -> bool:
        """Compare attack minus ennemy's defense with ennemy's health.

        Args:
            ennemy (CreatureCard): The instance of the opposing creature

        Returns:
            bool: True if this creature kill his opponent
        """
        return self.__attack - ennemy.get_defense() >= ennemy.get_health()

    def get_card_info(self) -> dict:
        result = super().get_card_info()
        result["attack"] = self.__attack
        result["defense"] = self.__defense
        return result
