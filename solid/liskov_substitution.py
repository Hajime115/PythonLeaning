"""リスコフの置換原則
サブクラスは、そのスーパークラスの代用ができなければならない
・methodA(x)という関数がTクラスのインスタンスxで実行できるなら
　Tクラスのサブクラスのsクラスのインスタンスyでも実行できなればならない
・サブクラス、スーパークラス間で実行できるものと実行できないものがあると
　サブクラスのコードをすべて理解する必要が生じる。
・継承元が実行できる関数は、継承先でも必ず実行できること。

[リスコフの置換原則を守った場合]
・スーパークラスの仕様を理解すれば、それを継承したサブクラスの中身を全て確認せず
　利用することができ、拡張性・保守性が向上する。
"""


class Rectangle:  # 長方形クラス

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, witdh):
        self._width = witdh

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def calcurate_area(self):
        return self._width * self._height


class Square(Rectangle):  # 正方形クラス(数学的には長方形の一部)

    def __init__(self, size):
        self._width = self._height = size

    @Rectangle.width.setter
    def width(self, size):
        self._width = self._height = size

    @Rectangle.height.setter
    def height(self, size):
        self._width = self._height = size


def print_area(obj):
    change_to_width = 10
    change_to_height = 20
    obj.width = change_to_width
    obj.height = change_to_height

    # 以下の実装によって、インスタンスがチェックされるのでリスコフの置換原則を満たす。
    # あるいは四角形(Quadrilateral)クラスという空クラスを作って正方形、長方形ともに継承させる。

    if isinstance(obj, Square):
        change_to_width = change_to_height

    print('予想面積 = {}, 実際面積 = {}'.format(
        change_to_height * change_to_width,
        obj.calcurate_area()
    ))


rc = Rectangle(2, 3)
print_area(rc)

sq = Square(5)
print_area(sq)
