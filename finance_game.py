import random

# Constants
STARTING_CAPITAL = 1000
STARTING_HAPPINESS = 50
TURNS = 10
INTEREST_RATE = 0.05
INVESTMENT_MULTIPLIER = [0.5, 1.2, 2.0]  # Risk levels
EVENTS = [
    {"name": "Market Crash", "effect": -0.3},  # -30% wealth
    {"name": "Economic Boom", "effect": 0.5},  # +50% wealth
    {"name": "Unexpected Bonus", "effect": 0.2},  # +20% wealth
    {"name": "Medical Emergency", "effect": -200},  # -200 money
]

def random_event():
    """Simulate a random financial event."""
    return random.choice(EVENTS)

def display_status(turn, money, happiness):
    """Display the player's current status."""
    print(f"\n--- Turn {turn}/{TURNS} ---")
    print(f"Money: ${money:.2f}")
    print(f"Happiness: {happiness}/100")

def save_money(money):
    """Simulate saving money and earning interest."""
    return money + (money * INTEREST_RATE)

def invest_money(money, risk_level):
    """Simulate investing money with a risk level."""
    multiplier = random.choice(INVESTMENT_MULTIPLIER[:risk_level])
    return money * multiplier

def spend_money(money, happiness, amount):
    """Simulate spending money and gaining happiness."""
    if amount > money:
        print("You don't have enough money to spend that much!")
        return money, happiness
    happiness += min(100 - happiness, int(amount / 10))  # Gain happiness
    return money - amount, happiness

def game():
    """Run the finance game."""
    money = STARTING_CAPITAL
    happiness = STARTING_HAPPINESS

    print("Welcome to the Finance Game!")
    print(f"Start with ${STARTING_CAPITAL} and {STARTING_HAPPINESS} happiness.")
    print(f"Try to maximize your wealth and happiness in {TURNS} turns!\n")

    for turn in range(1, TURNS + 1):
        display_status(turn, money, happiness)

        # Choose an action
        print("\nActions:")
        print("1. Save Money (earn interest)")
        print("2. Invest Money (risk and reward)")
        print("3. Spend Money (increase happiness)")
        action = input("Choose an action (1/2/3): ")

        if action == "1":
            money = save_money(money)
            print(f"You saved your money. New balance: ${money:.2f}")
        elif action == "2":
            risk_level = int(input("Choose risk level (1 = low, 2 = medium, 3 = high): "))
            invested_money = invest_money(money, risk_level)
            money = invested_money
            print(f"Your investment resulted in: ${money:.2f}")
        elif action == "3":
            amount = int(input("How much money do you want to spend? "))
            money, happiness = spend_money(money, happiness, amount)
            print(f"You spent ${amount}. New happiness: {happiness}/100")
        else:
            print("Invalid action. Skipping turn.")

        # Random event
        event = random_event()
        if "effect" in event and isinstance(event["effect"], float):
            money += money * event["effect"]
        elif "effect" in event:
            money += event["effect"]
        print(f"Random Event: {event['name']}! Your new balance: ${money:.2f}")

    # Final Results
    print("\n--- Game Over ---")
    print(f"Final Money: ${money:.2f}")
    print(f"Final Happiness: {happiness}/100")
    if money >= STARTING_CAPITAL * 2 and happiness > 80:
        print("Congratulations! You mastered financial success!")
    else:
        print("Better luck next time! Keep learning about finance.")

if __name__ == "__main__":
    game()
