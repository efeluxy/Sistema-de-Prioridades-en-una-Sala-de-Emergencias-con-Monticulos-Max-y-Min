# Ejercicio de Feedback 01. Montículos
En este repositorio se encuentra el código que simula la atencion a pacientes en una sala de emergencias respetando las prioridades de atención establecidas.

·Félix Godoy Salinas·
-Acceso al repositorio del proyecto:
https://github.com/efeluxy/Sistema-de-Prioridades-en-una-Sala-de-Emergencias-con-Monticulos-Max-y-Min

-Ejercicio a realizar- 
Sistema de Prioridades en una Sala de Emergencias con Montículos Máx y Mín. 

-Reflexión del proyecto-
Para realizar este ejercicio tenemos una serie de pautas a seguir en el enunciado, las pautas son las siguientes:
  1. Implementación:
      Diseña las clases Paciente (con atributos como nombre, nivel_urgencia y horas_espera) y SalaEmergencias (con los montículos max y min como atributos, y métodos para gestionarlos).
  2. Simulación:
      Genera una lista de pacientes aleatorios con niveles de urgencia y tiempos de espera variados.
      Añade estos pacientes a la SalaEmergencias, asegurando que sean incorporados a ambos montículos.
  3. Atención:
      Desencola y atiende a los pacientes siguiendo estas reglas:
      Si hay pacientes con un nivel de urgencia de 10 (el más alto), atiéndelos inmediatamente.
      Si no hay pacientes con urgencia máxima, pero hay pacientes que han esperado más de 5 horas, atiéndelos.
      En caso contrario, atiende al paciente con la mayor urgencia.
  4. Reporte:
      Luego de simular la atención de 20 pacientes, genera un reporte que muestre los pacientes atendidos, en qué orden y después de cuánto tiempo de espera.

Según estas instrucciones empezamos el código creando dos clases principales, 'Pacientes' y 'SalaEmergencia', cada una con su funcion '__init__' para declarar sus respectivas variables.

En la clase paceinte declaramos las variables self, nombre, nivelUrgencia, tiempoEspera, y para la clase sala de espera declaramos dos listas, las cuales serán los montículos máximo y mínimo del ejercicio. 
Entonces, asignamos el montículo máximo a el nivel de urgencia 'self.maxHeapUrgencia = []' y el mínimo al tiempo de espera 'self.minHeapEspera = []'.

Ahora creamos la clase 'agregarPaciente' la que se encargará de añadir los pacientes a ambos montículos. Además, asignamos las variables de nivel de urgencia y tiempo de espera a estos montículos para después interactuar con ellos.

Como última función, la denominamos 'atenderPaciente' y, en esta, se realizará el proceso de atención a los pacientes que haya en la sala. En esta misma introducimos la lógica para clasificar a los pacientes atendidos y sus preferencias.

Por último, creamos la variable 'sala' que representa a los pacientes en la sala y, la variable (lista) 'pacientes' donde se guardarán los datos de los pacientes. 
Después de eso, realizamos un bucle simple apra generar la información de 20 pacientes y poder generar un reporte.
Una vez los datos se han procesado, realizamos otro bucle simple para mostrar todos los datos ordenados según han sido atendidos.


Con todo el código realizado y funcional, recibimos el reporte y analizamos el resultado.
En conclusión, el resultado que obtenemos són los 20 pacientes diferentes, cada uno con sus datos (nivel de urgencia y teimpo de espera) generados aleatóriamente.
Estos se ordenan en orden de mayor a menor nivel de urgencia y, a su vez, dentro de cada valor de urgencia, se ordena de mayor a menor tiempo de espera.
Esto indica que, se atenderan de nivel de urgencia 10, 9 , 8... y, si se tienen varios pacientes con el mismo nivel de urgencia, se atienden según su su tiempo de espera de mayor a menor, 10, 9, 8...
