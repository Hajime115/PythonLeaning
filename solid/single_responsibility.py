"""単一責任の原則
全てのモジュールとクラスは一つの役割を提供して責任をもつべきとする原則

・役割が複数ある場合、各クラスが何なのか複雑化してしまう。
・一つの役割に別の役割が複雑に依存してしまい、一つの役割の変更が別の役割に影響を与える可能性があり、保守性の低下を招く

[単一責任の原則を守った場合]
・クラス、モジュールを分けることで、可読性が向上する
・役割を分けることで、他のクラスから利用できやすくなり拡張性が向上する
"""


class UserInfo:

    """ ユーザー情報を保持するという役割"""

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return "{},{},{}".format(
            self.name, self.age, self.phone_number
        )

    """以下は単一責任の原則に背くので、FileManagerクラスを作る"""
    # def write_str_to_file(self, filename):
    #     with open(filename, mode="w") as fh:
    #         fh.write(str(self))


class FileManager:

    @staticmethod
    def write_str_to_file(obj, filename):
        with open(filename, mode="w") as fh:
            fh.write(str(obj))


user_info = UserInfo('Taro', 21, '000-0000-0000')
# user_info.write_str_to_file('solid/Generated/tmp.txt')
FileManager.write_str_to_file(user_info, "solid/Generated/tmp.txt")
