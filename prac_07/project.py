"""
Project
Estimate: minutes
Actual:   minutes
"""

class Project:
    def __init__(self, name, date, priority, cost, completion_percentage):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def is_complete(self):
        return self.completion_percentage >= 100

    def string_changer(self):
        return f"{self.name}\t{self.date}\t{self.priority}\t{self.cost}\t{self.completion_percentage}"

    def __str__(self):
        return (f"{self.name}, start: {self.date}, priority {self.priority}, estimate: {self.cost}, "
                f"completion: {self.completion_percentage}%")