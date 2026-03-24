from decimal import Decimal

class BankAccount:
    def __init__(self, owner: str, balance: Decimal = Decimal("0")) -> None:
        self.owner = owner
        self.balance = balance
    

    def deposit(self, amount: Decimal):
        self.balance += amount
        print(f"存钱 {amount}, 最新余额 {self.balance}")


    def withdraw(self, amount: Decimal):
        if amount > self.balance:
            print(f"提取{amount}, 余额不足, 当前余额{self.balance}")
        else:
            self.balance -= amount
            print(f"提取{amount}, 当前余额{self.balance}")
    

    def __repr__(self) -> str:
        return f"账户：{self.owner}, 余额为 {self.balance}"
    

b = BankAccount("Jacian", Decimal("100"))
b.deposit(Decimal("1000"))
b.withdraw(Decimal("900.3"))
print(b)