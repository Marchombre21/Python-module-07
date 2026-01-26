# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    FantasyCardFactory.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 16:19:13 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 16:19:14 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

import random
from ex3.CardFactory import (CardFactory,
                             Rarity,
                             TypeCard,
                             SpellsEffects,
                             ArtifactsEffects
                             )
from ex0 import Creature, Card
from ex1 import (
    SpellCard,
    ArtifactCard,
    Deck,
    Player
)


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        rarity = random.choice(list(Rarity))
        if rarity == Rarity.COMMON:
            attack = random.choice([1, 2, 3])
            defense = random.choice([1, 2, 3])
            health = random.choice([1, 2, 3])
            return Creature(name_or_power, 2, Rarity.COMMON, TypeCard.CREATURE,
                            attack, health, defense)
        elif rarity == Rarity.RARE:
            attack = random.choice([4, 5, 6])
            defense = random.choice([4, 5, 6])
            health = random.choice([4, 5, 6])
            return Creature(name_or_power, 4, Rarity.RARE, TypeCard.CREATURE,
                            attack, health, defense)
        elif rarity == Rarity.LEGENDARY:
            attack = random.choice([7, 8, 9])
            defense = random.choice([7, 8, 9])
            health = random.choice([7, 8, 9])
            return Creature(name_or_power, 6, Rarity.LEGENDARY,
                            TypeCard.CREATURE, attack, health, defense)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        effect = random.choice(list(SpellsEffects))
        if effect == SpellsEffects.BUFF:
            return SpellCard(name_or_power, 4, SpellsEffects.BUFF,
                             TypeCard.SPELL, effect)
        elif effect == SpellsEffects.DAMAGES:
            return SpellCard(name_or_power, 4, SpellsEffects.DAMAGES,
                             TypeCard.SPELL, effect)
        elif effect == SpellsEffects.DEBUFF:
            return SpellCard(name_or_power, 4, SpellsEffects.DEBUFF,
                             TypeCard.SPELL, effect)
        elif effect == SpellsEffects.HEAL:
            return SpellCard(name_or_power, 4, SpellsEffects.HEAL,
                             TypeCard.SPELL, effect)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        effect = random.choice(list(ArtifactsEffects))
        if effect == ArtifactsEffects.HEALTH:
            return ArtifactCard(name_or_power, 4, Rarity.RARE,
                                TypeCard.ARTIFACT, 5, effect)
        elif effect == ArtifactsEffects.MANA:
            return ArtifactCard(name_or_power, 4, Rarity.RARE,
                                TypeCard.ARTIFACT, 5, effect)

    def create_themed_deck(self, size: int, owner: Player) -> dict:
        deck: Deck = Deck(owner)
    # J'en suis là. Il faut que cette fonction appelle celles au dessus pour
    # créer un deck et le retourne (dans un dictionnaire)

    def get_supported_types(self) -> dict:
        pass
