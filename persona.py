class Persona:
    def __init__(self, nombre:str ="colo",apellido: str = "messi",dni: int = "26622387"):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__= dni

    def __str__(self):
        print(f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__du__}')
