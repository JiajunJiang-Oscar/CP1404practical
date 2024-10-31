"""
Guitar
Estimate: 20 minutes
Actual:   27 minutes
"""

from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1924)
guitar2 = Guitar("Another Guitar", 2015)

print(f"{guitar1.name} get_age() -Expected 100. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() -Expected 9. Got {guitar2.get_age()}")

print(f"{guitar1.name} get_age() -Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} get_age() -Expected False. Got {guitar2.is_vintage()}")
