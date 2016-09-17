import LevelObject

class Obstacle(LevelObject.LevelObject):
    def __init__(self, on_floor):
        LevelObject.LevelObject.__init__(self, "img/spikes.png", on_floor)