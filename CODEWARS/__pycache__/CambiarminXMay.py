"""
aden Smith, el hijo de Will Smith, es la estrella de películas como The Karate Kid (2010) y After Earth (2013). Jaden también es conocido por parte de su filosofía que transmite a través de Twitter . Cuando escribe en Twitter, es conocido por escribir casi siempre con mayúscula cada palabra. Para simplificar, tendrá que poner cada palabra en mayúsculas, verifique cómo se espera que sean las contracciones en el ejemplo a continuación.

Su tarea es convertir las cadenas a cómo las escribiría Jaden Smith. Las cadenas son citas reales de Jaden Smith, pero no están en mayúsculas de la misma forma en que las escribió originalmente.

Ejemplo:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real" 

"""
def to_jaden_case(string):
    # ...
    contador = 0
    texto = ""
    anterior = ""
    for palabra in string:
        contador += 1
        if palabra == " ":
            anterior = palabra
            texto += anterior
        elif anterior == " ":
            letra = palabra.upper()
            anterior = palabra
            texto += letra
        elif contador == 1:
            texto += palabra.upper()
        else:
            texto += palabra.lower()
            anterior = palabra
    
    return texto

def to_jaden_case1(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)

def to_jaden_case2(string):
    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case("nafsQLYdea bl rIWZH BKF pqBphuuQN dO GXjVIdEoIO R hGVChcJFnM P lLxFqH z QJCRobWzy ShZhqW kHwbfJdUT uq AcYgDYsYI PgGjm IGg HJP ZarOmaEfuH q lNhXFeWpW C HcpratGY rgjYk qEXxzXfZy OcE PNePno XACwXkQ zHF WiZtGd jUJQSnRyO JXB xkDzJrhLeN kbUuE tG nFnTBoU AalqDKF LqHyKyN oSysM EBfH mDOecayuiI mrrSkBtijA hQdVoKlIW MU hEcs bDnrkWRe U tfcQ umGJ WngWsrQHD dQNqVOGsG xthwsl egjQp AKIZao Z NrSlr nyEdyNr XzwsZfXF tSiwO jEzdtBewph pGqpF nBaazGxhMl mjF"))
print(to_jaden_case1("nafsQLYdea bl rIWZH BKF pqBphuuQN dO GXjVIdEoIO R hGVChcJFnM P lLxFqH z QJCRobWzy ShZhqW kHwbfJdUT uq AcYgDYsYI PgGjm IGg HJP ZarOmaEfuH q lNhXFeWpW C HcpratGY rgjYk qEXxzXfZy OcE PNePno XACwXkQ zHF WiZtGd jUJQSnRyO JXB xkDzJrhLeN kbUuE tG nFnTBoU AalqDKF LqHyKyN oSysM EBfH mDOecayuiI mrrSkBtijA hQdVoKlIW MU hEcs bDnrkWRe U tfcQ umGJ WngWsrQHD dQNqVOGsG xthwsl egjQp AKIZao Z NrSlr nyEdyNr XzwsZfXF tSiwO jEzdtBewph pGqpF nBaazGxhMl mjF"))
print(to_jaden_case2("nafsQLYdea bl rIWZH BKF pqBphuuQN dO GXjVIdEoIO R hGVChcJFnM P lLxFqH z QJCRobWzy ShZhqW kHwbfJdUT uq AcYgDYsYI PgGjm IGg HJP ZarOmaEfuH q lNhXFeWpW C HcpratGY rgjYk qEXxzXfZy OcE PNePno XACwXkQ zHF WiZtGd jUJQSnRyO JXB xkDzJrhLeN kbUuE tG nFnTBoU AalqDKF LqHyKyN oSysM EBfH mDOecayuiI mrrSkBtijA hQdVoKlIW MU hEcs bDnrkWRe U tfcQ umGJ WngWsrQHD dQNqVOGsG xthwsl egjQp AKIZao Z NrSlr nyEdyNr XzwsZfXF tSiwO jEzdtBewph pGqpF nBaazGxhMl mjF"))