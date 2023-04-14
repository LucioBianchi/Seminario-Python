nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,     74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def estudiantes(listaNombres):
    """ Recibe una lista con los nombres. Devuelve un diccionario que relaciona a los estudiantes con una tupla de sus notas """
    notas_general = notas_1 + notas_2
    dict = {}
    for i in range(len(listaNombres)):
        dict[listaNombres[i]] = (notas_1[i], notas_2[i])
    return dict

def promedio_estudiantes(dict_estudiantes):
    """ Recibe un diccionario con los estudiantes y sus notas. Devuelve un diccionario que relaciona a los estudiantes con su promedio """
    dict_promedios = {}
    for alumno in dict_estudiantes:
        dict_promedios[alumno] = (dict_estudiantes[alumno][0] + dict_estudiantes[alumno][1]) / 2
    return dict_promedios

def promedio_general(dict_promedios):
    """ Recibe un diccionario con los estudiantes y sus promedios. Devuelve el promedio general del curso """
    return sum(dict_promedios.values())/len(dict_promedios)

def mayor_promedio(dict_promedios):
    """ Recibe un diccionario con los estudiantes y sus promedios. Devuelve el nombre del estudiante con mayor promedio """
    max_alumno = max(dict_promedios , key = dict_promedios.get)
    return max_alumno

def menor_nota(dict_estudiantes):
    """" Recibe un diccionario con los estudiantes y sus notas. Devuelve el nombre del alumno con la nota mas baja """
    min_alumno = min(dict_estudiantes, key=lambda x: min(dict_estudiantes[x]))
    return min_alumno

# Creo una lista con todos los nombres
listaNombres = nombres.lstrip().rstrip().replace("'", "").split(",")

print('-'*10 + 'Inciso A' + '-'*10)
dict_estudiantes = (estudiantes(listaNombres))
print(dict_estudiantes, '\n')

print('-'*10 + 'Inciso B' + '-'*10)
dict_promedios = promedio_estudiantes(dict_estudiantes)
print(dict_promedios, '\n')

print('-'*10 + 'Inciso C' + '-'*10)
print(f'Promedio general: {round(promedio_general(dict_promedios),2)} \n')

print('-'*10 + 'Inciso D' + '-'*10)
max_alumno = mayor_promedio(dict_promedios)
print(f'Estudiante con mayor promedio: {max_alumno} (su promedio es: {dict_promedios[max_alumno]}) \n ')

print('-'*10 + 'Inciso E' + '-'*10)
min_alumno = menor_nota(dict_estudiantes)
print(f'Estudiante con nota mas baja: {min_alumno} (su nota es: {min(dict_estudiantes[min_alumno])})')





