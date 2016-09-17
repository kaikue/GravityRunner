import LevelObject

class Collectible(LevelObject.LevelObject):
    def __init__(self, on_floor):
        LevelObject.LevelObject.__init__(self, "img/coin.png", on_floor)