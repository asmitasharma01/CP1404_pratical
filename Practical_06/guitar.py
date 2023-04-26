"""
Estimated time : 30 minus
Actual time : 20 minus
"""

AGE_LIMIT = 50
CURRENT_YEAR = 2022


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, age_limit):
        return self.get_age(CURRENT_YEAR) >= age_limit

    def __lt__(self, other):
        return self.year < other.year


guitar = Guitar("Gibson Les Paul", 1960, 10000)
print(guitar)
print("Is it vintage?", guitar.is_vintage(50))
