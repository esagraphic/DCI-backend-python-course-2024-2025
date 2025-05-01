from abc import ABC, abstractmethod

# Abstract base class
class Bank(ABC):
    @abstractmethod
    def loan(self):
        """Abstract method for loan services."""
        pass

    @abstractmethod
    def debit(self):
        """Abstract method for debit services."""
        pass

    @property
    @abstractmethod
    def credit(self):
        """Abstract property for credit services."""
        pass

# Concrete class for a local bank
class KabulBank(Bank):
    def loan(self):
        print("Loan service available at Kabul Bank.")
    
    def debit(self):
        print("Debit service available at Kabul Bank.")
    
    @property
    def credit(self):
        return "Credit service available at Kabul Bank."

# Example usage
if __name__ == "__main__":
    bank = KabulBank()
    
    bank.loan()       # Output: Loan service available at Kabul Bank.
    bank.debit()      # Output: Debit service available at Kabul Bank.
    print(bank.credit)  # Output: Credit service available at Kabul Bank.
