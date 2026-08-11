from abc import ABC, abstractmethod


class MaskRule(ABC):

    @abstractmethod
    def apply(self, value, config):
        pass
