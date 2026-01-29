# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 08:25:02 by bfitte            #+#    #+#             #
#    Updated: 2026/01/26 08:25:03 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from ex0 import (
    Card,
    CreatureCard,
    GameErrors,
    SpellsEffects
)

from ex1 import (
    Deck,
    Player,
    SpellCard,
    ArtifactCard
)


def main():
    try:
        cards_bruno: list[Card] = [
            SpellCard("Lightning Bolt", 3, "common", SpellsEffects.DAMAGES),
            SpellCard("Divine light", 3, "common", SpellsEffects.HEAL),
            ArtifactCard("Mana Crystal", 2, "rare", 5,
                         "Permanent: +1 mana per turn'"),
            CreatureCard("Fire Dragon", 5, "Legendary", 7, 15, 3),
            CreatureCard("Elf Archer", 2, "Common", 2, 8, 0)
        ]
        cards_cannelle: list[Card] = [
            SpellCard("Lightning Bolt", 3, "common", SpellsEffects.DAMAGES),
            SpellCard("Divine light", 3, "common", SpellsEffects.HEAL),
            ArtifactCard("Mana Crystal", 2, "rare", 5,
                         "Permanent: +1 mana per turn"),
            CreatureCard("Fire Dragon", 5, "Legendary", 7, 15, 3),
            CreatureCard("Elf Archer", 2, "Common", 2, 8, 0)
        ]
        print("\n=== DataDeck Deck Builder ===\n")
        print("Building deck with different card types...\n")
        bruno = Player(20, "bruno")
        cannelle = Player(20, "cannelle")
        game_state = {}
        game_state["players"] = [bruno, cannelle]
        game_state["on_board"] = []
        deck_cannelle = Deck(cannelle)
        deck_bruno = Deck(bruno)
        for card_bruno, card_cannelle in zip(cards_bruno, cards_cannelle):
            deck_bruno.add_card(card_bruno)
            deck_cannelle.add_card(card_cannelle)
        print("Cannelle's deck", deck_cannelle.get_deck_stats())
        print("Bruno's deck", deck_cannelle.get_deck_stats())
        print("\nDrawing and playing cards:\n")
        deck_cannelle.shuffle()
        deck_bruno.shuffle()
        bruno.set_mana(30)
        cannelle.set_mana(30)
        for _ in range(3):
            card: Card = deck_bruno.draw_card()
            print(f"\nDrew: {card.get_name()} ({card.get_type()})")
            print(f"Play result: {card.play(game_state)}")
            card: Card = deck_cannelle.draw_card()
            print(f"\nDrew: {card.get_name()} ({card.get_type()})")
            print(f"Play result: {card.play(game_state)}")
        print("\nPolymorphism in action: Same interface,"
              " different card behaviors!")
        for obj in game_state["on_board"]:
            print(obj.get_name(), obj.get_owner().get_name())
        print(deck_bruno.get_deck_stats())
        print(deck_cannelle.get_deck_stats())
    except (GameErrors, Exception) as e:
        print(e)


if __name__ == "__main__":
    main()
