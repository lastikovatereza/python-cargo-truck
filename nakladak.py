from DruhaLekce.nakladni_auto import NakladniAuto, NakladniAutoException

auto = NakladniAuto()
auto.vypis()
auto.naloz(500)
auto.vypis()
auto.vyloz(300)
auto.vypis()
auto.naloz(6000)
auto.vypis()
auto.vyloz(3000)
auto.vypis()

try:
    naklato = NakladniAuto(1000)
    naklato.naloz(500)
    naklato.vyloz(2000)
except NakladniAutoException as e:
    print(e)