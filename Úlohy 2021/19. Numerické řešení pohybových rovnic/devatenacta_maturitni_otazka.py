def a():
    """
    Těleso se pohybuje nerovnoměrně zrychleně. Počáteční zrychlení v čase t=0 má hodnotu 1m/s**2.
    Počáteční rychlost tělesa je nulová. Stejně tak je nulová počáteční dráha tělesa.
    Aktuální zrychlení a tělesa bude záviset na okamžité rychlosti v čase t vztahem: a = 1 + 0,2v
    Tedy hodnota zrychlení se bude lehce lineárně zvyšovat s rostoucí rychlostí.
    Vytvořte model, který zjistí hodnoty okamžité rychlosti, dráhy a zrychlení v čase t = 10s.
    Nápověda: Jedná se o “jednoduchý” úkol z kinematiky, není tedy třeba řešit sílu ani hmotnost.
    V dalším časovém kroku se jen dopočítá aktuální hodnota zrychlení dle poslední
    známé aktuální rychlosti. A provede se další časový krok, ve kterém se předpokládá,
    že se těleso pohybuje rovnoměrně zrychleně. Doporučený časový krok je 0,1 s
    """
    t = 0  # Celkový čas
    t_delta = 0.1  # Časový úsek, podle kterého počítáme aktuální rychlost a dráhu
    a = 0  # Zrychlení
    s = 0  # Celková dráha
    v_2 = 0  # Nová rychlost

    while t <= 10:
        v_1 = v_2  # v_1 je stará rychlost
        v_2 = v_1 + a * 0.1
        s = s + ((v_2 + v_1) / 2) * t_delta
        a = 1 + 0.2 * v_2

        t += t_delta

    print(f"V čase {t} je rychlost: {v_2}, dráha: {s}, zrychlení: {a}")


def b():
    """
    Těleso se pohybuje nerovnoměrně zrychleně. Počáteční zrychlení v čase t=0 má hodnotu 10 m/s**2.
    Počáteční rychlost tělesa je nulová. Počáteční dráha tělesa je nulová.
    Aktuální zrychlení a tělesa bude záviset na okamžité dráze tělesa s vztahem: a = 10 - 0,1s
    Tedy hodnota zrychlení se bude lehce lineárně snižovat s rostoucí dráhou tělesa.
    Vytvořte model, který zjistí hodnoty okamžité rychlosti, dráhy a zrychlení v čase t = 5s.
    Nápověda: Jedná se o “jednoduchý” úkol z kinematiky, není tedy třeba řešit sílu ani hmotnost.
    V dalším časovém kroku se jen dopočítá aktuální hodnota zrychlení dle poslední
    známé aktuální dráhy (tedy vlastně polohy). A provede se další časový krok, ve kterém se předpokládá, že
    se těleso pohybuje rovnoměrně zrychleně. Doporučený časový krok je 0,1 s.
    """


a()