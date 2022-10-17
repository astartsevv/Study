class Integer(int):
    'Измененный int, чтобы 2+2 =5'

    def __add__(self, arg):
        return super().__add__(arg) + 1


class List(list):
    'Измененный list, что больше 10 элементов нельзя положить'

    def __init__(self, arg):
        if len(arg) <= 10:
            return super().__init__(arg)

    def append(self, arg):
        if (self.__len__() + 1) <= 10:
            return super().append(arg)

    def extend(self, arg):
        if (self.__len__() + len(arg)) <= 10:
            return super().extend(arg)

    def insert(self, position, arg):
        if (self.__len__() + 1) <= 10:
            return super().insert(position, arg)


class UniqueList(list):
    'Лист с уникальными элементами, чтобы вел себя как множество'

    def __init__(self, arg):
        for a in arg:
            if self.count(arg) == 0:
                self.append(a)

    def append(self, arg):
        if self.count(arg) == 0:
            return super().append(arg)

    def extend(self, arg):
        for a in arg:
            print(self.count(a))
            if self.count(a) == 0:
                self.append(a)
        return self

    def insert(self, position, arg):
        if self.count(arg) == 0:
            return super().insert(position, arg)


if __name__ == '__main__':
    l = UniqueList([3, 4, 3, 5])
    print(l)
    l.append(4)
    print(l)
    l.extend([14, 35, 5])
    print(l)
    l.insert(4, 4)
    print(l)
