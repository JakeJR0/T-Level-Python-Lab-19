import pandas as pd


class Budget:

    def get_budget(self, budget_name):
        for i in self.budget_data.index:
            if self.budget_data.loc[i, "budget_name"] == budget_name:
                budget_total = self.budget_data.loc[i, "budget_total"]
                budget_remaining = self.budget_data.loc[i, "budget_remaining"]

                return budget_total, budget_remaining

        return None

    @property
    def budget_total(self):
        budget = 0
        remaining = 0
        for i in self.budget_data.index:
            budget += self.budget_data.loc[i, "budget_total"]
            remaining += self.budget_data.loc[i, "budget_remaining"]

        return budget, remaining

    @property
    def budget_spent(self):
        budget = 0
        remaining = 0
        for i in self.budget_data.index:
            budget += self.budget_data.loc[i, "budget_total"]
            remaining += self.budget_data.loc[i, "budget_remaining"]

        return f"{self.currency}{remaining - budget}"

    @property
    def budget_dataframe(self):
        return self.budget_data

    @budget_dataframe.deleter()
    def budget_dataframe(self):
        self.budget_data = pd.DataFrame({
            "budget_name": [],
            "budget_total": [],
            "budget_remaining": []
        })

    def add_budget(self, budget_name="", budget_total=0, budget_remaining=-1):
        if len(budget_name) < 2 or budget_total < 0:
            return False

        if budget_remaining == -1:
            budget_remaining = budget_total

        self.budget_data.loc[len(self.budget_data.index)] = [budget_name, budget_total, budget_remaining]
        return True

    def withdraw(self, budget_name="", amount=0):
        if amount <= 0:
            return False

        if len(budget_name) < 2:
            return False

        for i in self.budget_data.index:
            if self.budget_data.loc[i, "budget_name"] == budget_name:
                remaining = self.budget_data.loc[i, "budget_remaining"]
                if remaining < amount:
                    return False
                else:
                    self.budget_data.loc[i, "budget_remaining"] = remaining - amount

    def deposit(self, budget_name="", amount=0):
        if amount <= 0:
            return False

        if len(budget_name) < 2:
            return False

        for i in self.budget_data.index:
            if self.budget_data.loc[i, "budget_name"] == budget_name:
                budget = self.budget_data.loc[i, "budget_total"]
                self.budget_data.loc[i, "budget_remaining"] += amount
                if self.budget_data.loc[i, "budget_remaining"] > budget:
                    self.budget_data.loc[i, "budget_total"] = self.budget_data.loc[i, "budget_remaining"]




    def __init__(self, currency=""):
        self.budget_data = pd.DataFrame({
            "budget_name": [],
            "budget_total": [],
            "budget_remaining": []
        })

        self.currency = currency
