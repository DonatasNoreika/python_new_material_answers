class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = population > 20000000 or area > 3000000

    def _get_density(self, country):
        result = round(country.population / country.area, 2)
        print(f"{country.name} population density: {result} people per square kilometer")
        return result

    def compare_pd(self, country):
        if self._get_density(self) > self._get_density(country):
            return f"{self.name} has a larger population density than {country.name}"
        else:
            return f"{self.name} has a smaller population density than {country.name}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
lithuania = Country("Lithuania", 2832000, 65300)
netherlands = Country("Netherlands", 17718800, 41865)

print(australia.is_big)
print(andorra.is_big)
print(lithuania.is_big)

# print(lithuania.compare_pd(andorra))
# print(lithuania.compare_pd(australia))
# print(australia.compare_pd(andorra))
print(netherlands.compare_pd(lithuania))
