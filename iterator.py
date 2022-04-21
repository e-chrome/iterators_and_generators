from nested_list import nested_list


class FlatIterator:
    def __init__(self, some_list):
        self.main_cursor = 0
        self.second_cursor = -1
        self.main_len = len(some_list)
        self.main_list = some_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.main_cursor == self.main_len:
            raise StopIteration
        if type(self.main_list[self.main_cursor]) is not list:
            self.main_cursor += 1
            self.second_cursor = -1
            return self.main_list[self.main_cursor - 1]

        self.second_cursor += 1
        self.second_len = len(self.main_list[self.main_cursor])

        if self.second_cursor == self.second_len:
            self.main_cursor += 1
            self.second_cursor = 0
        if self.main_cursor == self.main_len:
            raise StopIteration
        return self.main_list[self.main_cursor][self.second_cursor]


def print_items(list_):
    for item in FlatIterator(list_):
        if type(item) is list:
            print_items(item)
        else:
            print(item)


if __name__ == '__main__':
    print_items(nested_list)


