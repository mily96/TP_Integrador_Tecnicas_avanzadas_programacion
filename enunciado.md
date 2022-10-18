# TP - TADP - 2C 2022

# Objetivo
Realizar el control de turnos y otorgamiento de licencias de conducir, tomando en consideración los siguientes requerimientos funcionales.

# Requerimientos Funcionales
- El examen consta de dos etapas. La primer etapa incluye la pregunta si utiliza o no anteojos. 
Si responde que no automáticamente deberá generarse el examen y permitirle responder el 
cuestionario. 
Si responde que si, se generará un turno random para que asista a una revisión. (La fecha 
deberá generarse de manera aleatoria).
- El usuario debería generar una clave para poder acceder al examen, la cual tendrá un tiempo 
de expiración de una hora.
- El cuestionario constará de 10 preguntas precargas de opción múltiple. Las mismas deberás 
cargarse de forma aleatoria. 
- La clave generada podrá utilizarse una sola vez. En caso que no termine la evaluación no 
podrá volver a usarla.
- Aprueba el examen con un 8 preguntas respondidas correctamente.
- En caso de reprobar el sistema deberá generar un nuevo turno aleatorio.
- La misma persona sólo podrá rendir un máximo de 3 veces el examen. 
- Los resultados del examen deberán guardarse durante 1 semana.
- Las preguntas deberán poder ser editables por un administrador del sistema.
- El administrador del sistema podrá acceder a una estadística diaria de cuantos rindieron el 
examen, cuantos aprobaron, reprobaron o estuvieron ausentes.