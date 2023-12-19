from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QMessageBox


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()


    def create_connection(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("CAR_SERVICE_db.db")

        if not db.open():
            # QtWidgets.QMessageBox.critical(None, "Cannot open database",
            #                                 "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QSqlQuery()
        query.exec("""CREATE TABLE IF NOT EXISTS пользователи (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      имя TEXT,
                      фамилия TEXT,
                      логин TEXT,
                      пароль TEXT,
                      возраст INTEGER,
                      номер_телефона TEXT,
                      super_user TEXT DEFAULT no)""")

        query.exec("""CREATE TABLE IF NOT EXISTS услуги (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      название_услуги TEXT,
                                      цена REAL)""")

        query.exec("""CREATE TABLE IF NOT EXISTS заказы (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              id_пользователь INTEGER REFERENCES пользователи(id) null,
                              id_услуги INTEGER REFERENCES услуги(id) null,
                              марка_машины TEXT,
                              описание_проблемы TEXT,
                              дата TEXT)""")


        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new1(self, firstname, lastname, login, password, age, number_phone, admin):
        sql_query = "INSERT INTO пользователи (имя, фамилия, логин, пароль, возраст, номер_телефона, super_user) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [firstname, lastname, login, password, age, number_phone, admin])

    def add_new2(self, id_user, id_service, mark, description, date):
        sql_query = "INSERT INTO заказы (id_пользователь, id_услуги, марка_машины, описание_проблемы, дата) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [id_user, id_service, mark, description, date])

    def add_new3(self, name, price):
        sql_query = "INSERT INTO услуги (название_услуги, цена) VALUES (?, ?)"
        self.execute_query_with_params(sql_query, [name, price])

    def change1(self, firstname, lastname, login, password, age, number_phone, admin, id):
        sql_query = "UPDATE пользователи SET имя=?, фамилия=?, логин=?, пароль=?, возраст=?, номер_телефона=?, super_user=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [firstname, lastname, login, password, age, number_phone, admin, id])

    def change2(self, id_user, id_service, mark, description, date, id):
        sql_query = "UPDATE заказы SET id_пользователь=?, id_услуги=?, марка_машины=?, описание_проблемы=?, дата=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [id_user, id_service, mark, description, date, id])

    def change3(self, name, price, id):
        sql_query = "UPDATE услуги SET название_услуги=?, цена=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [name, price, id])

    def delete1(self, id):
        sql_query = "DELETE FROM пользователи WHERE id=?"
        self.execute_query_with_params(sql_query, [id])

    def delete2(self, id):
        sql_query = "DELETE FROM заказы WHERE id=?"
        self.execute_query_with_params(sql_query, [id])
    def delete3(self, id):
        sql_query = "DELETE FROM услуги WHERE id=?"
        self.execute_query_with_params(sql_query, [id])

    def get_user(self, login, password):
        query = QSqlQuery()
        query.prepare("SELECT * FROM пользователи WHERE логин = ? AND пароль = ?")
        query.bindValue(0, login)
        query.bindValue(1, password)
        if query.exec() and query.next():
            return query.record()
        else:
            return None

    def add_user(self, login, password):
        sql_query = "INSERT INTO пользователи (логин, пароль) VALUES (?, ?)"
        self.execute_query_with_params(sql_query, [login, password])

    def add_data_user(self, firstname, lastname, age, number_phone, id):
        sql_query = "UPDATE пользователи SET имя=?, фамилия=?, возраст=?, номер_телефона=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [firstname, lastname, age, number_phone, id])

    def add_data_order(self, id, mark, description, date):
        sql_query = "INSERT INTO заказы (id_пользователь, марка_машины, описание_проблемы, дата) VALUES (?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [id, mark, description, date])

    def info(self, info_date):
        query = QSqlQuery()
        query.prepare("select услуги.цена from услуги join заказы on услуги.id = заказы.id_услуги WHERE заказы.дата =?")
        query.bindValue(0, info_date)
        query.exec()
        prices_list = []
        while query.next():
            price = query.value(0)
            prices_list.append(price)
        query = QSqlQuery()
        query.prepare("SELECT COUNT(*) FROM заказы WHERE дата=?")
        query.bindValue(0, info_date)
        query.exec()
        while query.next():
             count = query.value(0)
             count_list = list(range(1, count))

        return prices_list, count_list














































