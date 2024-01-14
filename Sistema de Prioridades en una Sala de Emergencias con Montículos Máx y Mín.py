import random
import heapq

class Paciente:
    def __init__(self, nombre, nivelUrgencia, tiempoEspera):
        self.nombre = nombre
        self.nivelUrgencia = nivelUrgencia
        self.tiempoEspera = tiempoEspera

    def __lt__ (self, other):
        if self.nivelUrgencia == other.nivelUrgencia:
            return self.tiempoEspera > other.tiempoEspera
        else: 
            return self.nivelUrgencia > other.nivelUrgencia
    
class SalaEmergencia:
    def __init__(self):
        self.maxHeapUrgencia = []
        self.minHeapEspera = []

    def agregarPaciente(self, paciente):
        heapq.heappush(self.maxHeapUrgencia, paciente)
        heapq.heappush(self.minHeapEspera, (paciente.tiempoEspera, paciente))

    def atenderPaciente(self):
        if self.maxHeapUrgencia and self.maxHeapUrgencia[0].nivelUrgencia == 10:
            return heapq.heappop(self.maxHeapUrgencia)
        elif self.minHeapEspera and self.minHeapEspera[0][0] >= 5:
            return heapq.heappop(self.minHeapEspera)[1]
        elif self.maxHeapUrgencia:
            return heapq.heappop(self.maxHeapUrgencia)
        else:
            return None

sala = SalaEmergencia()
pacientes = []

for i in range(1, 21):
    nombre = f"Paciente {i}"
    nivel_urgencia = random.randint(1, 10)
    horas_espera = random.randint(1, 10)
    paciente = Paciente(nombre, nivel_urgencia, horas_espera)
    pacientes.append(paciente)
    sala.agregarPaciente(paciente)

print("Reporte pacientes atendidos:")
for i in range(1, 21):
    paciente = sala.atenderPaciente()
    print(f"{i}. {paciente.nombre} -Urgencia: {paciente.nivelUrgencia} -Espera: {paciente.tiempoEspera}")