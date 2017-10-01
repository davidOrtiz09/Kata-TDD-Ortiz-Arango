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
            if len(res) > 1:
                if int(res[0]) > int(res[1]):
                    minimo = int(res[1])
                array.append(len(res))
                array.append(minimo)
            else:
                array.append(len(res))
                array.append(minimo)
        return array
