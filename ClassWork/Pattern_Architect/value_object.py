from dataclasses import dataclass




@dataclass(frozen=True)
class Money:
    amount: float
    currency: str


    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
        if not self.currency or len(self.currency) != 3:
            raise ValueError("Currency must be a valid 3-letter ISO code")


    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add amounts with different currencies")
        return Money(self.amount + other.amount, self.currency)


    def subtract(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot subtract amounts with different currencies")
        return Money(self.amount - other.amount, self.currency)


    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"




# Пример использования
if __name__ == "__main__":
    salary = Money(5000.00, "USD")
    bonus = Money(1000.00, "USD")
    total_income = salary.add(bonus)


    print(f"Base Salary: {salary}")
    print(f"Bonus: {bonus}")
    print(f"Total Income: {total_income}")


    # Попробуем сложить суммы в разных валютах
    try:
        euros = Money(1000.00, "EUR")
        total_income.add(euros)
    except ValueError as e:
        print(f"Error: {e}")