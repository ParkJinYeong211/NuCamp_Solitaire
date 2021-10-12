class Card():
    _suit: str
    _value: int
    _isRed: bool
    _flipped: bool

    def GetValue(self, value):
        return dict(zip(range(1, 14), "A234567890JQK"))[value]

    def __init__(self, suit, value):
        if suit not in ["C", "D", "H", "S"]:
            raise ValueError(f"{suit} is invalid suit.")
            return None
        if value not in range(1, 14):
            raise ValueError(f"{value} is invalid card value.")
            return None

        self._suit = suit
        self._value = self.GetValue(value)
        self._flipped = False

        if suit == "D" or suit == "H":
            self._isRed = True
        else:
            self._isRed = False

    def __str__(self):
        # return f"{self._value} of {self._suit}(red)" if self._isRed else f"{self._value} of {self._suit}(black)"
        return f"{self._value}{self._suit}"

    def Flip_Card(self):
        self._flipped = True
