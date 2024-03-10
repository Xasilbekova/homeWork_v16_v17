class Mashina:
    def __init__(self, nom, tur, ishlab_chiqarilgan_yili, narxi=4000):
        self.nom = nom
        self.tur = tur
        self.ishlab_chiqarilgan_yili = ishlab_chiqarilgan_yili
        self.narxi = narxi

    def malumot(self):
        return f"Nomi: {self.nom}, Turi: {self.tur}, Yili: {self.ishlab_chiqarilgan_yili}, Narxi: ${self.narxi}"

mashinalar = [
    Mashina("Toyota Camry", "Yengil", 2019, 25000),
    Mashina("BMW X5", "Yengil", 2020, 55000),
    Mashina("Ford F-150", "Yuk avtomobili", 2018, 35000),
    Mashina("Honda Civic", "Yengil", 2017),
    Mashina("Chevrolet Silverado", "Yuk avtomobili", 2016, 30000),
    Mashina("Mercedes-Benz E-Class", "Yengil", 2021, 60000),
    Mashina("Toyota RAV4", "Yengil", 2019, 28000),
    Mashina("Tesla Model S", "Yengil", 2022, 80000),
    Mashina("Nissan Altima", "Yengil", 2015, 20000),
    Mashina("Jeep Wrangler", "Yuk avtomobili", 2018, 40000)
]

mashinalar = sorted(mashinalar, key=lambda x: x.ishlab_chiqarilgan_yili)

for mashina in mashinalar:
    print(mashina.malumot())
