class Procesador:
    def __init__(self):
        pass

    @staticmethod
    def calcular(param):
        if param=="":
            return 0
        else:
            return  len(param.split(","))

