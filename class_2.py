class Jet:
    name = "falcon"
    model = 'F-35'

    # создаем методы класса
    def country(self):
        print ("USA")


# Создаем объект класса Car под названием car_a
jet_a = Jet()


print(jet_a.country())