"""依存性逆転の原則
ソフトウェアモジュール間の依存関係を切り離す

・高水準なモジュールは、低水準のモジュールに依存してはいけない。両者は抽象化に依存すべき。
・抽象化は詳細に依存すべきでなく、詳細は抽象化に依存すべきである
・依存性逆転の原則を守る事で、低水準モジュールを継承したクラスを利用した機能拡張が容易になる。
"""


# class Book:
#     def __init__(self, content):
#         self.content = content


# class Formater:
#     def format(self, book: Book):
#         return book.content


# class AFormatter:
#     def format(self, book: Book):
#         return book.content + 'A'


# class Printer:
#     def print(self, book: Book):
#         formatter = Formater()
#         formatted_book = formatter.format(book)
#         print(formatted_book)


# book = Book('My Book')
# printer = Printer()
# printer.print(book)

from abc import ABCMeta, abstractmethod, abstractproperty


class IBook(metaclass=ABCMeta):

    @abstractproperty
    def content(self):
        pass


class Book(IBook):

    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return self._content


class EBook(IBook):

    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return 'E' + self._content


class IFormatter(metaclass=ABCMeta):

    @abstractmethod
    def format(self, i_book: IBook):
        pass


class XmlFormatter(IFormatter):

    def format(self, i_book: IBook):
        return '<xml>' + i_book.content + '</xml>'


class HtmlFormatter(IFormatter):

    def format(self, i_book: IBook):
        return '<h1>' + i_book.content + '</h1>'


class Printer:

    def __init__(self, i_formatter: IFormatter):
        self._i_formatter = i_formatter

    def print(self, i_book: IBook):
        formatted_book = self._i_formatter.format(i_book)
        print(formatted_book)


book = Book('My Book')
html_formatter = HtmlFormatter()
html_printer = Printer(html_formatter)
html_printer.print(book)

xml_formatter = XmlFormatter()
xml_printter = Printer(xml_formatter)
xml_printter.print(book)

ebook = EBook('My EBook')
xml_printter.print(ebook)
