class Profesor:
    def __init__(self ,el_nombre, el_gmail):
        self.nombre = el_nombre
        self.gmail = el_gmail
    
    def dame_tu_nombre(self):
        return self.nombre


class Alumno:
    def __init__(self , el_elegido):
        self.nombre = el_elegido
        self.inasistencia = 0
        self.dieta = ""
        self.mentor = None

    def mentoria(self,profesor):
        self.mentor = profesor
    
    def falta(self):
        self.inasistencia +=1

    def elegir_dieta(self ,la_dieta):
        self.dieta = la_dieta

    def es_vegano(self):
        self.dieta = "vegano"


    def esta_libre(self):
        if self.inasistencia >5:
            return "ESTA LIBRE"
        else:
            return "todo piola"
    


profe_elio = Profesor("ELIO", "elio@gmail.com")
profe_gabi = Profesor("Gabi","gabielcrak@gmail.com")

print(profe_elio.dame_tu_nombre())
print(profe_gabi.dame_tu_nombre())

alumno_colo = Alumno("FRANCO")
alumno_emma = Alumno("emmaden")

alumno_colo.falta()
alumno_colo.falta()
alumno_colo.falta()
alumno_colo.falta()
alumno_colo.falta()
alumno_colo.falta()
print(alumno_colo.esta_libre())

alumno_emma.elegir_dieta("vegetariano")
print(alumno_emma.dieta)
alumno_colo.es_vegano
print(alumno_colo.dieta)

alumno_colo.mentoria(profe_elio)
print(alumno_colo.mentor)




import ipdb; ipdb.set_trace()


