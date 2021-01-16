"""開放閉鎖の原則
クラス、モジュール、関数等のソフトウェアの部品は拡張に対しては開いており、修正に対しては閉じているべき

・アプリケーションに変更があった場合、コードを追加して拡張し容易に対応できる
・モジュールの動作を変更する場合には、ソースコードを直接修正するようなことはないようにする

[開放閉鎖の原則を守った場合]
・機能拡張が用意になりソフトウェアの拡張性が向上する
・機能拡張時にテストをする際に、拡張機能だけを実施すればよく、元のソースコードはテストをしなくてよいため、保守性も向上する
"""

from abc import ABCMeta, abstractmethod

# 以下の実装だとCompartionを増やせば良い為、出来たコードに修正を加える事はない


class UserInfo:

    def __init__(self, user_name, job_name, nationality):
        self.user_name = user_name
        self.job_name = job_name
        self.nationality = nationality

    def __str__(self):
        return '{} {} {}'.format(
            self.user_name, self.job_name, self.nationality
        )


class Comparation(metaclass=ABCMeta):

    @abstractmethod
    def is_equal(self, other):
        pass


class Filter(metaclass=ABCMeta):

    @abstractmethod
    def filter(self, comparation, item):
        pass


class JobNameComparation(Comparation):

    def __init__(self, job_name):
        self.job_name = job_name

    def is_equal(self, other):
        return self.job_name == other.job_name


class NationalityComparation(Comparation):

    def __init__(self, nationality):
        self.nationality = nationality

    def is_equal(self, other):
        return self.nationality == other.nationality


class UserInfoFilter(Filter):
    def filter(self, comparation, items):
        for item in items:
            if comparation.is_equal(item):
                yield item


# 以下の実装だと、ソースコードに手を入れる必要がある
# class UserInfoFilter:

#     @staticmethod
#     def filter_user_job(users, job_name):
#         for user in users:
#             if user.job_name == job_name:
#                 yield user

#     @staticmethod
#     def filter_users_nationality(users, nationality):
#         for user in users:
#             if user.nationality == nationality:
#                 yield user

# for man in UserInfoFilter.filter_user_job(user_list, 'police man'):
#     print(man)

# for man in UserInfoFilter.filter_users_nationality(user_list, 'Japan'):
#     print(man)


taro = UserInfo('taro', 'salary man', 'Japan')
jiro = UserInfo('jiro', 'police man', 'Japan')
john = UserInfo('john', 'salary man', 'USA')

user_list = [taro, jiro, john]
user_info_filter = UserInfoFilter()

salary_man_comparation = JobNameComparation('salary man')
for user in user_info_filter.filter(salary_man_comparation, user_list):
    print(user)

japan_comparation = NationalityComparation('Japan')
for user in user_info_filter.filter(japan_comparation, user_list):
    print(user)
