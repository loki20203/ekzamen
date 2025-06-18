class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)
        print(f"LOG: {message}")

    def get_logs(self):
        return self.logs


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.account_number = account_number
        self.balance = initial_balance
        self.logger = Logger()

    def deposit(self, amount):
        self.balance += amount
        self.logger.log(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.logger.log(f"Attempted to withdraw {amount} from account {self.account_number}, but insufficient funds.")
            raise InsufficientFundsError("Insufficient balance for this withdrawal.")
        self.balance -= amount
        self.logger.log(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")

# Приклад використання:
if __name__ == "__main__":
    account = BankAccount("UA1234567890", 1000)

    account.deposit(500)
    
    try:
        account.withdraw(200)
        account.withdraw(2000)  
    except InsufficientFundsError as e:
        print(f"Error: {e}")

    logger = Logger()
    print("\nTransaction Logs:")
    for log in logger.get_logs():
        print(log)
