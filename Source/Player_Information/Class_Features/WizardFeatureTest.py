from math import floor, sqrt
from typing import Any, Callable

from Source.Player_Information.ClassFeature import ClassFeature


class WizardFeatureTest(ClassFeature):
    def __init__(
        self, player: Any, func: Callable[[None], None], name: str, level: int
    ):
        super().__init__(player, func, name, level)

        self.strength = 100
        self._used_times = 0

    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)
        self._used_times += 1
        self.update_spell_strength()

    def update_spell_strength(self):
        self.strength = floor(sqrt(self._used_times) * 100 * 1.5)

    def can_use_feature(self) -> bool:
        return super().can_use_feature() and self._used_times <= 100