from typing import Any


class Descriptor:
    def __set_name__(self, owner, name) -> None:
        self.storage_name = name

    def __get__(self, instance, owner) -> Any:
        return instance.__dict__[self.storage_name]

    def __set__(self, instance, value) -> None:
        instance.__dict__[self.storage_name] = value
