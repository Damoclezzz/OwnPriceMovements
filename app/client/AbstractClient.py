from abc import ABC, abstractmethod
from typing import Any


class AbstractClient(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url

    @abstractmethod
    def get_last_hour_klines(self, pair: str) -> Any:
        pass
