import wikipedia

def main():
    """The program for import wikipedia and search"""

    title = input("Enter page title:")
    while title != "":
        try:

            # Do not know why can not use autosuggest function
            # , it will highlight an Unexpected argument error
            page = wikipedia.page(title)
            print(page.title)
            print(wikipedia.summary(title, sentences=1))
            print(f"{page.url}\n")

        # Do PageError exception and return message
        except wikipedia.exceptions.PageError:
            print(f"Page id {title} does not match any pages. Try another id!")

        # Do DisambiguationError exception and return message
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        title = input("Enter page title:")
    print("Thank you")

if __name__ == '__main__':
    main()