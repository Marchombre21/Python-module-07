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
from ex3.CardFactory import CardFactory
from ex0 import (
    CreatureCard,
    Card,
    Rarity,
    SpellsEffects,
    ArtifactsEffects
    )
from ex1 import SpellCard, ArtifactCard, Deck, Player
from typing import Callable


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        """Initialize the card generator with predefined card data."""
        self._creatures = [
            {
                "name": "Fire Dragon",
                "cost": 5,
                "rarity": Rarity.LEGENDARY,
                "attack": 7,
                "health": 5,
                "defense": 5,
            },
            {
                "name": "Goblin Warrior",
                "cost": 2,
                "rarity": Rarity.COMMON,
                "attack": 2,
                "health": 1,
                "defense": 0,
            },
            {
                "name": "Ice Wizard",
                "cost": 4,
                "rarity": Rarity.RARE,
                "attack": 3,
                "health": 4,
                "defense": 2,
            },
            {
                "name": "Lightning Elemental",
                "cost": 3,
                "rarity": Rarity.UNCOMMON,
                "attack": 4,
                "health": 2,
                "defense": 1,
            },
            {
                "name": "Stone Golem",
                "cost": 6,
                "rarity": Rarity.RARE,
                "attack": 5,
                "health": 8,
                "defense": 2,
            },
            {
                "name": "Shadow Assassin",
                "cost": 3,
                "rarity": Rarity.UNCOMMON,
                "attack": 5,
                "health": 2,
                "defense": 0,
            },
            {
                "name": "Healing Angel",
                "cost": 4,
                "rarity": Rarity.RARE,
                "attack": 2,
                "health": 6,
                "defense": 2,
            },
            {
                "name": "Forest Sprite",
                "cost": 1,
                "rarity": Rarity.COMMON,
                "attack": 1,
                "health": 1,
                "defense": 1,
            },
        ]
        self._spells = [
            {
                "name": "Lightning Bolt",
                "cost": 3,
                "rarity": Rarity.COMMON,
                "effect_type": SpellsEffects.DAMAGES,
            },
            {
                "name": "Healing Potion",
                "cost": 2,
                "rarity": Rarity.COMMON,
                "effect_type": SpellsEffects.HEAL,
            },
            {
                "name": "Fireball",
                "cost": 4,
                "rarity": Rarity.UNCOMMON,
                "effect_type": SpellsEffects.DAMAGES,
            },
            {
                "name": "Shield Spell",
                "cost": 1,
                "rarity": Rarity.COMMON,
                "effect_type": SpellsEffects.BUFF,
            },
            {
                "name": "Meteor",
                "cost": 8,
                "rarity": Rarity.LEGENDARY,
                "effect_type": SpellsEffects.DAMAGES,
            },
            {
                "name": "Ice Shard",
                "cost": 2,
                "rarity": Rarity.COMMON,
                "effect_type": SpellsEffects.DAMAGES,
            },
            {
                "name": "Some debuff",
                "cost": 2,
                "rarity": Rarity.COMMON,
                "effect_type": SpellsEffects.DEBUFF,
            },
            {
                "name": "Divine Light",
                "cost": 5,
                "rarity": Rarity.RARE,
                "effect_type": SpellsEffects.HEAL,
            },
            {
                "name": "Magic Missile",
                "cost": 1,
                "rarity": Rarity.COMMON,
                "effect_type": SpellsEffects.DAMAGES,
            },
        ]
        self._artifacts = [
            {
                "name": "Mana Crystal",
                "cost": 2,
                "rarity": Rarity.COMMON,
                "durability": 5,
                "effect": ArtifactsEffects.MANA,
            },
            {
                "name": "Sword of Power",
                "cost": 3,
                "rarity": Rarity.UNCOMMON,
                "durability": 3,
                "effect": ArtifactsEffects.ATTACK,
            },
            {
                "name": "Ring of Wisdom",
                "cost": 4,
                "rarity": Rarity.RARE,
                "durability": 4,
                "effect": ArtifactsEffects.DRAW,
            },
            {
                "name": "Shield of Defense",
                "cost": 5,
                "rarity": Rarity.RARE,
                "durability": 6,
                "effect": ArtifactsEffects.HEALTH,
            },
            {
                "name": "Crown of Kings",
                "cost": 7,
                "rarity": Rarity.LEGENDARY,
                "durability": 8,
                "effect": ArtifactsEffects.COST,
            },
        ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """
        If a name was passed as argument and is in list, it create this
        creature.Else, a creature will be create according to a random
        choice in rarity possibilities.

        :return: A creature card
        :rtype: Card
        """
        creature: dict = {}
        if name_or_power and name_or_power in [
            creature["name"] for creature in self._creatures
        ]:
            creature = [
                creature
                for creature in self._creatures
                if creature["name"] == name_or_power
            ][0]
        else:
            rarity = random.choice(
                [
                    Rarity.COMMON,
                    Rarity.COMMON,
                    Rarity.COMMON,
                    Rarity.UNCOMMON,
                    Rarity.UNCOMMON,
                    Rarity.UNCOMMON,
                    Rarity.RARE,
                    Rarity.RARE,
                    Rarity.LEGENDARY,
                ]
            )
            if rarity == Rarity.COMMON:
                creature = random.choice(
                    [
                        creature
                        for creature in self._creatures
                        if creature["rarity"] == Rarity.COMMON
                    ]
                )
            elif rarity == Rarity.UNCOMMON:
                creature = random.choice(
                    [
                        creature
                        for creature in self._creatures
                        if creature["rarity"] == Rarity.UNCOMMON
                    ]
                )
            elif rarity == Rarity.RARE:
                creature = random.choice(
                    [
                        creature
                        for creature in self._creatures
                        if creature["rarity"] == Rarity.RARE
                    ]
                )
            elif rarity == Rarity.LEGENDARY:
                creature = random.choice(
                    [
                        creature
                        for creature in self._creatures
                        if creature["rarity"] == Rarity.LEGENDARY
                    ]
                )
        return CreatureCard(
            creature["name"],
            creature["cost"],
            creature["rarity"],
            creature["attack"],
            creature["health"],
            creature["defense"],
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        If a name was passed as argument and is in list, it create this spell.
        Else, a spell will be create according to a random choice in
        effect possibilities.

        :return: A spell card
        :rtype: Card
        """
        spell: dict = {}
        if name_or_power and name_or_power in\
                [spell["name"] for spell in self._spells]:
            spell = [
                spell for spell in self._spells if spell["name"] ==
                name_or_power][0]
        else:
            effect = random.choice(list(SpellsEffects))
            if effect == SpellsEffects.BUFF:
                spell = random.choice(
                    [
                        spell
                        for spell in self._spells
                        if spell["effect_type"] == SpellsEffects.BUFF
                    ]
                )
            elif effect == SpellsEffects.DAMAGES:
                spell = random.choice(
                    [
                        spell
                        for spell in self._spells
                        if spell["effect_type"] == SpellsEffects.DAMAGES
                    ]
                )
            elif effect == SpellsEffects.DEBUFF:
                spell = random.choice(
                    [
                        spell
                        for spell in self._spells
                        if spell["effect_type"] == SpellsEffects.DEBUFF
                    ]
                )
            elif effect == SpellsEffects.HEAL:
                spell = random.choice(
                    [
                        spell
                        for spell in self._spells
                        if spell["effect_type"] == SpellsEffects.HEAL
                    ]
                )
        return SpellCard(
            spell["name"],
            spell["cost"],
            spell["rarity"],
            spell["effect_type"],
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        If a name was passed as argument and is in list, it create this
        artifact.
        Else, an artifact will be create according to a random choice in
        rarity possibilities.

        :return: An artifact card
        :rtype: Card
        """
        artifact: dict = {}
        if name_or_power and name_or_power in [
            artifact["name"] for artifact in self._artifacts
        ]:
            artifact = [
                artifact
                for artifact in self._artifacts
                if artifact["name"] == name_or_power
            ][0]
        else:
            rarity = random.choice(
                [
                    Rarity.COMMON,
                    Rarity.COMMON,
                    Rarity.COMMON,
                    Rarity.UNCOMMON,
                    Rarity.UNCOMMON,
                    Rarity.UNCOMMON,
                    Rarity.RARE,
                    Rarity.RARE,
                    Rarity.LEGENDARY,
                ]
            )
            if rarity == Rarity.COMMON:
                artifact = random.choice(
                    [
                        artifact
                        for artifact in self._artifacts
                        if artifact["rarity"] == Rarity.COMMON
                    ]
                )
            elif rarity == Rarity.UNCOMMON:
                artifact = random.choice(
                    [
                        artifact
                        for artifact in self._artifacts
                        if artifact["rarity"] == Rarity.UNCOMMON
                    ]
                )
            elif rarity == Rarity.RARE:
                artifact = random.choice(
                    [
                        artifact
                        for artifact in self._artifacts
                        if artifact["rarity"] == Rarity.RARE
                    ]
                )
            elif rarity == Rarity.LEGENDARY:
                artifact = random.choice(
                    [
                        artifact
                        for artifact in self._artifacts
                        if artifact["rarity"] == Rarity.LEGENDARY
                    ]
                )
        return ArtifactCard(
            artifact["name"],
            artifact["cost"],
            artifact["rarity"],
            artifact["durability"],
            artifact["effect"],
        )

    def create_themed_deck(self, size: int, owner: Player) -> dict:
        """
        Create a deck of size cards with random number of
        each type of cards.

        :param size: Number of cards we want in deck
        :type size: int
        :param owner: Futur deck's owner
        :type owner: Player
        :return: A dict with owner's name and his deck
        :rtype: dict
        """
        deck: Deck = Deck(owner)
        creature: Callable = self.create_creature
        spell: Callable = self.create_spell
        artifact: Callable = self.create_artifact
        calls: list[Callable] = [creature, creature, spell, artifact]
        for _ in range(size):
            call: Callable = random.choice(calls)
            deck.add_card(call())
        return {"owner": owner.get_name(), "deck": deck}

    def get_supported_types(self) -> dict:
        """
        :return: All cards this factory can create.
        :rtype: dict
        """
        result: dict = {'creatures': [], 'spells': [], 'artifacts': []}
        for card in self._artifacts:
            result["artifacts"].append(card["name"])
        for card in self._creatures:
            result["creatures"].append(card["name"])
        for card in self._spells:
            result["spells"].append(card["name"])
        return result

    def get_name(self) -> str:
        return self.__class__.__name__
