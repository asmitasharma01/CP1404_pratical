"""
Estimated time : 30 minutes
Actual time : 20 minutes
"""

from Practical_06.guitar import guitar

guitar_1 = guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = guitar("Another guitar", 2013, 1000)
print(f"{guitar_1.name} get_age() - Expected 100. Got {guitar_1.get_age()}")
print(f"{guitar_2.name} get_age() - Expected 9. Got {guitar_2.get_age()}")
print(f"{guitar_1.name} is_vintage() - Expected True. Got {guitar_1.is_vintage()}")
print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")
