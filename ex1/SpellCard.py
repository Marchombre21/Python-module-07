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
    SpellsEffects
)


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 effect_type: SpellsEffects):
        super().__init__(name, cost, rarity)
        self.__effect_type: SpellsEffects = effect_type
        self.__type: str = "Spell"

    def play(self, game_state: dict) -> dict:
        super().play(game_state)
        owner: Player = self.get_owner()
        if self.is_playable(owner.get_mana()):
            owner.remove_card(self)
            owner.set_mana(-self.get_cost())
            print(f"Playable: True, Name: {self.get_name()}, Cost:"
                  f" {self.get_cost()}, New {owner.get_name()}'s mana points:"
                  f" {owner.get_mana()}")
            effect = self.resolve_effect(game_state)
            return {'card_played': self.get_name(), 'mana_used':
                    self.get_cost(), 'remaining mana': owner.get_mana(),
                    'effect': effect}
        else:
            print("Playable: False")
            return {'card_almost_played': self.get_name(), 'mana_almost_used':
                    self.get_cost(), "user's mana": owner.get_mana()}

    def resolve_effect(self, target: dict) -> str:
        owner: Player = self.get_owner()
        ennemy: Player = [player for player in target["players"]
                          if player.get_name() !=
                          owner.get_name()][0]
        effect: str = ""
        match self.__effect_type:
            case SpellsEffects.DAMAGES:
                if ennemy.damage(3):
                    raise VictoryError(owner.get_name())
                effect = (f"{self.get_name()} deals 3 damage to"
                          f" {ennemy.get_name()} by-passing the defense."
                          f" {ennemy.get_name()} has"
                          f" {ennemy.get_health()} HP left")
            case SpellsEffects.HEAL:
                owner.healing(3)
                effect = (f"{self.get_name()} gives 3 health points to"
                          f" {owner.get_name()} bringing them to"
                          f" {owner.get_health()} HP")
            case SpellsEffects.BUFF:
                owner.set_defense(1)
                effect = f"{self.get_name()} gives 1 defense points"
                f" to {owner.get_name()}"
            case SpellsEffects.DEBUFF:
                ennemy.set_defense(-1)
                effect = f"{self.get_name()} gives -1 defense points"
                f" to {ennemy.get_name()}"
        return effect

    def get_effect(self) -> SpellsEffects:
        return self.__effect_type

    def get_type(self) -> str:
        return self.__type
