class Continent:

    def __init__(self, connection, name):
        self.connection = connection
        self.name = name
        self.cursor = self.connection.cursor()

    def get_id(self):
        request = self.cursor.execute("SELECT id_continent FROM Continents WHERE continent_name = '{}'".format(self.name))
        answer = request.fetchone()
        print(answer)
        return answer

    def get_countries(self):
        request = self.cursor.execute("SELECT country_name FROM Countries WHERE country_continent = '{}'".format(self.name))
        answer = request.fetchall()
        print(answer)
        return answer

    def get_countries_number(self):
        request = self.cursor.execute("SELECT number_of_countries FROM Continents WHERE continent_name = '{}'".format(self.name))
        answer = request.fetchone()
        print(answer)
        return answer

    def get_capital_cities(self):
        request = self.cursor.execute("SELECT country_capital_city FROM Countries WHERE country_continent = '{}'".format(self.name))
        answer = request.fetchone()
        print(answer)
        return answer