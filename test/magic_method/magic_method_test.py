# coding:utf-8
import collections

# collections.nametuple是python自带的构建一个只有属性没有方法的类的模块，这里构造了一个叫做Card的类，只有rank和suit两个属性，没有方法
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    RANKS = [str(n) for n in range(2, 11)] + list('JQKA')
    SULTS = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.SULTS for rank in self.RANKS]
    #
    def __len__(self):
        return len(self._card)

    def __getitem__(self, item):
        return self._card[item]


if __name__ == '__main__':
    rd = FrenchDeck()
    print(len(rd))
    print(rd[15])
