from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AgressiveStrategy
from ex3.GameEngine import GameEngine
from ex1 import Player
from ex0 import GameErrors


def main():
    try:
        print("\n=== DataDeck Game Engine ===\n")
        factory = FantasyCardFactory()
        bruno = Player(20, "bruno")
        cedric = Player(20, "cedric")
        game_state = {"players": [bruno, cedric], "on_board": []}
        game_engine = GameEngine(game_state)
        strategy = AgressiveStrategy(game_state)
        print("Configuring Fantasy Card Game...")
        game_engine.configure_engine(factory, strategy)
        print("\nSimulating aggressive turn...")
        print("Hand:")
        for card in bruno.get_hand():
            print(card.get_name())
        for i in range(8):
            print(f"\nTurn {i + 1} execution:")
            print("Actions:", game_engine.simulate_turn())
        print("\nGame report:")
        print(game_engine.get_engine_status())
        print("\nAbstract Factory + Strategy Pattern: Maximum"
              " flexibility achieved!")
    except GameErrors as e:
        print(e)


if __name__ == "__main__":
    main()
