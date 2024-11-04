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

def main():
    """Use to show the program languages in format"""

    from prac_06.programming_language import ProgrammingLanguage

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    # storage three languages in a list
    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for ProgrammingLanguage in languages:

        # if reflection of ProgrammingLanguage equal to True
        if ProgrammingLanguage.reflection:
            print(ProgrammingLanguage.language)

main()
