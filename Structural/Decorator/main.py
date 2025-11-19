############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-19
#   Last Modified   :   2025-11-19
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines a Decorater design pattern
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

class TextTag:
    """Represents a base text tag"""

    def __init__(self, text: str) -> None:
        self._text = text

    def render(self) -> str:
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"


def main():
    
    simple_hello = TextTag("This is text to decorate!") ### create simple text
    print("before:", simple_hello.render())
    
    italic_hello = ItalicWrapper(simple_hello)  ### pass simple text tag to Italic decorator
    print("itaic : ", italic_hello.render())
    
    bold_hello = BoldWrapper(simple_hello)  ### pass simple text tag to bold decorator
    print("italic :", bold_hello.render())
    
    italic_bold_hello = ItalicWrapper(BoldWrapper(simple_hello))  ### pass simple text tag to bold decorator
    print("italic + bold : ", italic_bold_hello.render())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
