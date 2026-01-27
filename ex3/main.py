from ex3.FantasyCardFactory import FantasyCardFactory
from ex1 import Player


def main():
    factory = FantasyCardFactory()
    bruno = Player(20, "bruno")
    cedric = Player(20, "cedric")
    bruno_deck = factory.create_themed_deck(12, bruno)
    cedric_deck = factory.create_themed_deck(12, cedric)
    print(bruno_deck["deck"].get_deck_stats())
    print(cedric_deck["deck"].get_deck_stats())


if __name__ == "__main__":
    main()
