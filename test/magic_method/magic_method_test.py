# coding:utf-8
import collections
from random import choice

# collections.nametuple是python自带的构建一个只有属性没有方法的类的模块，这里构造了一个叫做Card的类，只有rank和suit两个属性，没有方法
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    RANKS = [str(n) for n in range(2, 11)] + list('JQKA')
    SULTS = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.SULTS for rank in self.RANKS]

    """获取长度的魔术方法"""

    def __len__(self):
        return len(self._card)

    """通过索引获取元素的魔术方法"""

    def __getitem__(self, item):
        return self._card[item]

    """集合类型可以用in关键字判断元素在对象集合中，列表，元祖，字符串都属于集合"""

    def __contains__(self, item):
        pass


"""元素大小比较函数"""
suit_value = dict(spades=3, diamonds=2, clubs=1, hearts=0)


def compare_card(card):
    """黑桃A的值是：4 * 12 + 3, 黑桃表示"""
    rank_value = FrenchDeck.RANKS.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]
    # return suit_value[card.suit] * len(FrenchDeck.RANKS) + card.rank


if __name__ == '__main__':
    rd = FrenchDeck()
    print(len(rd))
    print(rd[15])
    """choice这个方法相当于随机得到一个len范围内的索引值来访问对象的某个索引元素"""
    print(choice(rd))

    """列表的特殊用法"""
    print(rd[12::13])
    """反向迭代列表"""
    for card in reversed(rd):
        print(card)
    if Card(rank='4', suit='diamonds') in rd:
        print('support __contais__')

    for card in sorted(rd, key=compare_card):
        print(card)
