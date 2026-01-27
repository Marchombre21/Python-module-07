# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    SpellCard.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/25 11:12:20 by bfitte            #+#    #+#             #
#    Updated: 2026/01/25 11:12:21 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex0 import (
    Card,
    Player,
    VictoryError,
    Rarity,
    TypeCard,
    SpellsEffects
)


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 type_card: TypeCard, effect_type_card: SpellsEffects):
        super().__init__(name, cost, rarity, type_card)
        self.__effect_type_card: SpellsEffects = effect_type_card

    def play(self, game_state: dict) -> dict:
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
        super().play(game_state)
        owner: Player = self.get_owner()
        if self.is_playable(owner.get_mana()):
            print("Playable: True")
            owner.set_mana(-self.get_cost())
            effect = self.resolve_effect(game_state, owner)
            return {'card_played': self.get_name(), 'mana_used':
                    self.get_cost(), 'remaining mana': owner.get_mana(),
                    'effect': effect}
        else:
            print("Playable: False")
            return {'card_almost_played': self.get_name(), 'mana_almost_used':
                    self.get_cost(), "user's mana": owner.get_mana()}

    def resolve_effect(self, game_state: dict, owner: Player) -> str:
        ennemy: Player = [player for player in game_state["players"]
                          if player.get_name() !=
                          owner.get_name()][0]
        effect: str = ""
        match self.__effect_type_card.lower():
            case "damages":
                if ennemy.damage(3):
                    raise VictoryError(owner.get_name())
                effect: str = f"{self.get_name()} deals 3 damage to"\
                              f" {ennemy.get_name()} by-passing the defense."\
                              f" {ennemy.get_name()} has"\
                              f" {ennemy.get_health()} HP left"
            case "heal":
                owner.healing(3)
                effect: str = f"{self.get_name()} gives 3 health points to"\
                              f" {owner.get_name()} bringing them to"\
                              f" {owner.get_health()} HP"
            case "buff":
                owner.set_defense(3)
                effect: str = f"{self.get_name()} gives 3 defense points"
                f" to {owner.get_name()}"
            case "debuff":
                ennemy.set_defense(-3)
                effect: str = f"{self.get_name()} gives -3 defense points"
                f" to {ennemy.get_name()}"
        return effect
