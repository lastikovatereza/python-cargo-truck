class NakladniAutoException(Exception):
    def __init__(self, zprava):
        self.zprava = zprava

class NakladniAuto:
    def __init__(self):
        self.velikost_nakladu = 0
        self.max_kapacita = 5000

    def naloz(self, mnozstvi):
        if self.velikost_nakladu + mnozstvi > self.max_kapacita:
            dostupne_misto = self.max_kapacita - self.velikost_nakladu
            print(f"Nelze nalozit {mnozstvi} kg. Zbývá místo jen pro {dostupne_misto} kg.")
        else:
            self.velikost_nakladu += mnozstvi
            print(f"Právě jsi naložil {mnozstvi} jednotek nákladu.")

    def vyloz(self, mnozstvi):
        if mnozstvi > self.velikost_nakladu:
            raise NakladniAutoException(
                f"Nelze vyložit {mnozstvi} kg. Aktuální náklad je jen {self.velikost_nakladu} kg.")
        else:
            self.velikost_nakladu -= mnozstvi
            print(f"Právě jsi vyložil {mnozstvi} jednotek nákladu.")

    def vypis(self):
        print(f"Aktualni náklad: {self.velikost_nakladu} jednotek.")