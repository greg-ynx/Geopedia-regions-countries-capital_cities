import sqlite3

class Continent:

    def __init__(self, name):
        self.name = name

    def get_id(self):
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT id_continent FROM Continents WHERE continent_name = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        print(answer)
        return answer

    def get_countries(self):
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT country_name FROM Countries WHERE country_continent = '{}'".format(self.name))
        answer = query.fetchall()
        self.connection.close()
        print(answer)
        return answer

    def get_countries_number(self):
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT number_of_countries FROM Continents WHERE continent_name = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        print(answer)
        return answer

    def get_capital_cities(self):
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT country_capital_city FROM Countries WHERE country_continent = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        print(answer)
        return answer