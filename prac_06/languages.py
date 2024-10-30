"""
Languages
Estimate: 20 minutes
Actual:   28 minutes

import the ProgrammingLanguage from programming_language
python = in ProgrammingLanguage, language = "Python", typing = "Dynamic", reflection = True, year = 1991
display python
languages = [
    in ProgrammingLanguage, language = "Python", typing = "Dynamic", reflection = True, year = 1991
    in ProgrammingLanguage language = "Ruby", typing = "Dynamic", reflection = True, year = 1995
    in ProgrammingLanguage language = "Visual Basic", typing = "Static", reflection = False, year = 1991
]
display message
for ProgrammingLanguage in languages
    if reflection part in ProgrammingLanguage equal to True
    display current language in ProgrammingLanguage
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
print(python)

languages = [
    ProgrammingLanguage("Python", "Dynamic", True, 1991),
    ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
    ProgrammingLanguage("Visual Basic", "Static", False, 1991)
]

print("The dynamically typed languages are:")
for ProgrammingLanguage in languages:
    if ProgrammingLanguage.reflection:
        print(ProgrammingLanguage.language)
