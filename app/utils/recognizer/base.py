from abc import ABC, abstractmethod


class BaseRecognizer(ABC):
    name = None

    @abstractmethod
    def recognize(self, column_name: str, values: list) -> dict:
        """
        :return
        {
            type: xxx,
            confidence: 0.xx
        }
        """
        pass
