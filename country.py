import sqlite3

class Country:

    def __init__(self, name):
        self.name = name

    def get_id(self):
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT id_country FROM Countries WHERE country_name = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        print(answer)
        return answer

    def get_capital_city(self):
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT country_capital_city FROM Countries WHERE country_name = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        print(answer)
        return answer[0]

    def get_continent(self):
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT country_continent FROM Countries WHERE country_name = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        print(answer)
        return answer[0]

    def get_continent_id(self):
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT country_continent_id FROM Countries WHERE country_name = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        print(answer)
        return answer