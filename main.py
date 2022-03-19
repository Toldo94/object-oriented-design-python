import math


class Wheel:
    def __init__(self, rim: float, tire: float) -> None:
        self._rim = rim
        self._tire = tire

    @property
    def rim(self):
        return self._rim

    @property
    def tire(self):
        return self._tire

    @property
    def diameter(self):
        return self.rim + (self.tire * 2)

    @property
    def circumrerence(self):
        return self.diameter * math.pi


class Gear:
    def __init__(self, chainring: int, cog: int, wheel: Wheel = None) -> None:
        self._chainring = chainring
        self._cog = cog
        self._wheel = wheel

    @property
    def cog(self):
        return self._cog

    @property
    def chainring(self):
        return self._chainring

    @property
    def wheel(self):
        return self._wheel

    @property
    def ratio(self):
        return self.chainring / self.cog

    @property
    def gear_inches(self):
        return self.ratio * self.wheel.diameter


def main():

    wheel = Wheel(26, 1.5)
    print(wheel.circumrerence)
    print(Gear(52, 11, wheel).gear_inches)
    print(Gear(52, 11).ratio)


if __name__ == "__main__":
    main()
