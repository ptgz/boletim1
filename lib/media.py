def media(notas: list):
    try:
        return sum(notas) / len(notas)
    except Exception as e:
        print("deu erro")


def truncarFloat(float_number, decimal_places=1):
    multiplier = 10**decimal_places
    return int(float_number * multiplier) / multiplier
