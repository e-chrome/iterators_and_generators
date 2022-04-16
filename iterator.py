from nested_list import nested_list

class FlatIterator:
    def __init__(self, list_):
        self.start = -1
        self.end = len(list_)
        self.list_ = list_

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.list_[self.start]


def print_items(list_):
    for item in FlatIterator(list_):
        if type(item) is list:
            print_items(item)
        else:
            print(item)


if __name__ == '__main__':
    print_items(nested_list)


