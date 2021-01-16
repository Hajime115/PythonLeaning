"""インターフェース分離の原則
インターフェース上に必要のないメソッドを追加して
継承先が無駄なコードを作成することがないようにする

・継承するインターフェースの持つメソッドは必要最小限のものにする
・インターフェースを持つメソッドを増やしすぎることで
　継承先のクラスに無駄なコードが増えてしまい、コードが複雑になり利用者は混乱する
・インターフェースの継承先が増える為、インターフェースの修正による
　継承先のクラスの修正量が多くなり保守性が低下する
・一つのインターフェースに色々と詰め込まない
"""
from abc import ABCMeta, abstractmethod

""" 以下アスリート I/Fは、スイムもロングジャンプも持っている為
    子クラスアスリート1はそれら全てを継承する必要がある。"""

# class Athlete(metaclass=ABCMeta):

#     @abstractmethod
#     def swim(self):
#         pass

#     @abstractmethod
#     def high_jump(self):
#         pass

#     @abstractmethod
#     def long_jump(self):
#         pass

# class Athlete1(Athlete):

#     def swim(self):
#         print('I swim')

#     def high_jump(self):
#         pass

#     def long_jump(self):
#         pass


"""以下アスリート I/Fは、何も持っていなくて
   子クラスでスイムアスリート、ジャンプアスリートと派生する為
   アスリート１及びアスリート２は適切な子クラスを継承すればよい"""


class Athlete(metaclass=ABCMeta):
    pass


class SwimAthlete(Athlete):

    @abstractmethod
    def swim(self):
        pass


class JumpAthlete(Athlete):

    @abstractmethod
    def high_jump(self):
        pass

    @abstractmethod
    def long_jump(self):
        pass


class Athlete1(SwimAthlete):
    def swim(self):
        print('I swim')


class Athlete2(JumpAthlete):

    def high_jump(self):
        print('I hight jump')

    def long_jump(self):
        print('I long jump')


john = Athlete1()
john.swim()

tetsu = Athlete2()
tetsu.high_jump()
tetsu.long_jump()
