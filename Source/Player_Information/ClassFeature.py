from abc import ABC, abstractmethod
from typing import Any, Callable


class ClassFeature:
    def __init__(
        self, player: Any, func: Callable[[None], None], name: str, level: int
    ):
        self.player = player
        self.func = func
        self.name = name
        self.level = level

    def __call__(self, *args, **kwargs) -> None:
        if self.can_use_feature():
            self.func(self.player)
        else:
            print("ERROR")

    def can_use_feature(self) -> bool:
        return self.player.level >= self.level
