from panflute import *
from sys import stderr


def bold(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))


headers = []


def duplicateHeaders(elem, doc):
    if type(elem) == Header:
        header = stringify(elem)
        if header in headers:
            print("Duplicate header: " + header, file=stderr)
        else:
            headers.append(header)


def headerToUppercase(elem, doc):
    if type(elem) == Header and elem.level >= 3:
        return elem.walk(stringToUpperCase)


def stringToUpperCase(elem, doc):
    if type(elem) == Str:
        elem.text = elem.text.upper()


if __name__ == "__main__":
    run_filters([headerToUppercase, duplicateHeaders], prepare=bold)
