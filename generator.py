from nested_list import nested_list


def flat_generator(list_):
    index = 0
    while index < len(list_):
        if type(list_[index]) is list:
            flat_generator(list_[index])
        else:
            yield list_[index]
            index += 1


for item in flat_generator(nested_list):
    print(item)