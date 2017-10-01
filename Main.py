class Procesador:
    def __init__(self):
        pass

    @staticmethod
    def calcular(param):
        array = []
        if param == "":
            array.append(0)
        else:
            array.append(len(param.split(",")))
        return array




