#Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
class User:
    def __init__(self, ID, name):
        self._ID =ID
        self._name = name
        self._access_level = "user"
    def get_user_id(self):
        return self._ID

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self,name):
        self.name = name

class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self._access_level = "admin"

    def add_user(self, list_user, user):
        list_user.append(user)
        print(f"Добавлен пользователь {list_user[len(list_user)-1].get_name()}")

    def delete_user(self, list_user, user):
        list_user.remove(user)
        print(f"Удален пользователь {user.get_name()} \nСписок пользователей:")
        for i in range(len(list_user)):
            print(f"{list_user[i].get_user_id()} {list_user[i].get_access_level()} {list_user[i].get_name()}")

list_user = []
user1 = User( '1001', 'Василий')
user2 = User( '1002', 'Николай')
user3 = User( '1003', 'Егор')

admin1 = Admin("01", "Иван")
list_user.append(user1)
print(list_user[0].get_name())
admin1.add_user(list_user, user2)
admin1.add_user(list_user, user3)
admin1.delete_user(list_user, user1)