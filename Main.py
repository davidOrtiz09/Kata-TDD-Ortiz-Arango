class Procesador:
    def __init__(self):
        pass

    @staticmethod
    def calcular(param):
        array = []
        if param == "":
            array.append(0)
            array.append(0)
        else:
            res = param.split(",")
            minimo = int(res[0])
            array.append(len(res))
            array.append(minimo)
        return array




