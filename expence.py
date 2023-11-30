class Expense:

    def _init_(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def _repr_(self):
        return f"<Expense: {self.name}, {self.category}, Rs.{self.amount:.2f} >"
