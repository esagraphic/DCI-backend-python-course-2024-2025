from abc import ABC, abstractmethod


class SortStrategyBase(ABC):
    @abstractmethod
    def sort(self, data): ...


class SortByKey(SortStrategyBase):
    def sort(self, data: dict):
        # TODO: Provide implementation to the abstract method
        # to sort a dictionary by key
        return dict(sorted(data.items()))


class SortByValue(SortStrategyBase):
    def sort(self, data: dict):
        # TODO: Provide implementation to the abstract method
        # to sort a dictionary by value
        return dict(sorted(data.items(), key=lambda item: item[1], reverse=True))


class SortInDescOrder(SortStrategyBase):
    def sort(self, data: list[int]):
        # TODO: Provide implementation to the abstract method
        # to sort a list in descending order
        return sorted(data,reverse=True)


class SortBySecondItem(SortStrategyBase):
    def sort(self, data: list[tuple[int]]):
        # TODO: Provide implementation to the abstract method
        # to sort a list of tuples by its second item
        return sorted(data,key=lambda x: x[1])
