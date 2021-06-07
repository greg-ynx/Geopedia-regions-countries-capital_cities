import sqlite3

class Continent:

    def __init__(self, name):
        self.name = name

    def get_id(self):
        """
        Select Continent's id

        :return:
        answer[0] : int
            Continent's id
        """
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT id_continent FROM Continents WHERE continent_name = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        return answer[0]

    def get_countries(self):
        """
        Select Continent's countries

        :return:
        answer : tuple
            tuple of countries
        """
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT country_name FROM Countries WHERE country_continent = '{}'".format(self.name))
        answer = query.fetchall()
        self.connection.close()
        return answer

    def get_countries_count(self):
        """
        Select Continent's countries count

        :return:
        answer[0] : int
            Count of countries in the continent
        """
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT continent_number_of_countries FROM Continents WHERE continent_name = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        return answer[0]

    def get_capital_cities(self):
        """
        Select all capital cities from the continent

        :return:
        answer : tuple
            tuple of all capital_cities within the continent
        """
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()
        query = self.cursor.execute("SELECT country_capital_city FROM Countries WHERE country_continent = '{}'".format(self.name))
        answer = query.fetchone()
        self.connection.close()
        return answer