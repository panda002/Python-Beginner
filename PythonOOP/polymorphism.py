class India:
    def language(self):
        print("We speak Hindi in India")


class USA:
    def language(self):
        print("We speak English in US")


obj_india = India()
obj_usa = USA()

for country in obj_india, obj_usa:
    country.language()
