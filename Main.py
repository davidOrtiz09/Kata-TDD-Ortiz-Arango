class Procesador:
    def __init__(self):
        pass

    @staticmethod
    def calcular(param):
        if param=="":
            return 0
        elif len(param.split(",")) == 2:
            return 2
        else:
            return 1

