from sort_strategy import SortByKey, SortBySecondItem, SortByValue, SortInDescOrder


class Sort:
    def __init__(self):
        self.sort_by_key = SortByKey()
        self.sort_by_value = SortByValue()
        self.sort_by_second_item = SortBySecondItem()
        self.sort_in_desc_order = SortInDescOrder()

    def sort(self, data, strategy: str):
        if strategy == "sort_by_key":
            return self.sort_by_key.sort(data)

        if strategy == "sort_by_value":
            return self.sort_by_value.sort(data)

        if strategy == "sort_by_second_item":
            return self.sort_by_second_item.sort(data)

        if strategy == "sort_in_desc_order":
            return self.sort_in_desc_order.sort(data)


if __name__ == "__main__":
    d = {"a": 4, "f": 1, "e": 2}
    l = [3, 4, 5, 2, 1, 6]
    t = [(1, 2), (2, 1), (5, 3)]

    sort = Sort()

    # Sort dictionary by key
    print(sort.sort(d, strategy="sort_by_key"))  # {'f': 1, 'e': 2, 'a': 4}

    # Sort dictioanry by value
    print(sort.sort(d, strategy="sort_by_value"))  # {'a': 4, 'e': 2, 'f': 1}

    # Sort list in descending order
    print(sort.sort(l, strategy="sort_in_desc_order"))  # [6, 5, 4, 3, 2, 1]

    # Sort list of tuples by it's tuple's second number
    print(sort.sort(t, strategy="sort_by_second_item"))  # [(2, 1), (1, 2), (5, 3)]
