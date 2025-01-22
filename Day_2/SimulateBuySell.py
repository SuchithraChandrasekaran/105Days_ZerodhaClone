import random

class TradingSimulation:
    def __init__(self, initial_balance, buy_threshold, sell_threshold):
        self.balance = initial_balance
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
        self.position = 0  # 0 means no stocks, 1 means holding stocks
        self.stock_price = 100  # Initial stock price

    def buy(self, price):
        """Buy stock with the available balance."""
        if self.balance >= price:
            self.position = 1
            self.balance -= price
            print(f"Bought 1 stock at {price}. Balance: {self.balance:.2f}")

    def sell(self, price):
        """Sell stock and update balance."""
        if self.position == 1:
            self.balance += price
            self.position = 0
            print(f"Sold stock at {price}. Balance: {self.balance:.2f}")
    
    def simulate(self):
        """Simulate stock price fluctuations and buying/selling actions."""
        for _ in range(50):  # Simulate for 50 steps
            # Simulate price fluctuation (random change)
            price_change = random.uniform(-5, 5)  # Price changes between -5% to +5%
            new_price = self.stock_price * (1 + price_change / 100)
            print(f"New price: {new_price:.2f}")
            
            if self.position == 0 and price_change >= self.buy_threshold:
                self.buy(new_price)  # Buy condition
            
            elif self.position == 1 and price_change <= -self.sell_threshold:
                self.sell(new_price)  # Sell condition
            
            # Update stock price for the next iteration
            self.stock_price = new_price

# Set initial balance, buy threshold, and sell threshold
initial_balance = 1000  # Initial capital
buy_threshold = 2  # Buy when price rises by 2%
sell_threshold = 1  # Sell when price falls by 1%

# Create trading simulation instance
simulation = TradingSimulation(initial_balance, buy_threshold, sell_threshold)

# Run the simulation
simulation.simulate()
