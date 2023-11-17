import re


def balanced_brackets(my_string: str):
    bracket = re.compile(r"(\(|\)|\[|\])")
    end_string = "".join(bracket.findall(my_string))

    if len(end_string) == 0:
        return True
    if not (end_string[0] == "(" and end_string[-1] == ")") and not (
        end_string[0] == "[" and end_string[-1] == "]"
    ):
        return False

    # remove first and last character
    return balanced_brackets(end_string[1:-1])


if __name__ == "__main__":
    ok = balanced_brackets("square[brackets]")
    print(ok)
