class Procesador:
    def __init__(self):
        pass

    @staticmethod
    def calcular(param):
        array = []
        if param == "":
            array.append(0)
            array.append(0)
            array.append(0)
            array.append(0)
        else:
            res = param.split(",")
            minimo = int(res[0])
            maximo = int(res[0])
            if len(res) > 1:
                for k in res:
                    if minimo > int(k):
                       minimo = int(k)
                    else:
                        maximo = int(k)

                array.append(len(res))
                array.append(minimo)
                array.append(maximo)
            else:
                array.append(len(res))
                array.append(minimo)
                array.append(int(param))
        return array
