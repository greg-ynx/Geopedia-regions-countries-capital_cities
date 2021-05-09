class Country:

    def __init__(self, connection, name):
        self.connection = connection
        self.name = name
        self.cursor = self.connection.cursor()

    def get_id(self):
        request = self.cursor.execute("SELECT id_country FROM Countries WHERE country_name = '{}'".format(self.name))
        answer = request.fetchone()
        print(answer)
        return answer

    def get_capital_city(self):
        request = self.cursor.execute("SELECT country_capital_city FROM Countries WHERE country_name = '{}'".format(self.name))
        answer = request.fetchone()
        print(answer)
        return answer

    def get_continent(self):
        request = self.cursor.execute("SELECT country_continent FROM Countries WHERE country_name = '{}'".format(self.name))
        answer = request.fetchone()
        print(answer)
        return answer

    def get_continent_id(self):
        request = self.cursor.execute("SELECT country_continent_id FROM Countries WHERE country_name = '{}'".format(self.name))
        answer = request.fetchone()
        print(answer)
        return answer