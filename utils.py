# calcula los movimientos de cada persona de un viaje
# la lista_deudas es una lista de listas [Persona, balance]
# siendo balance = pagado - coste viaje
def calcular_balance(persona):
    return(persona.cantidad_pagada - persona.coste_viaje)

def seleccionar_balance(persona_balance):
    return(persona_balance[1])

def calcular_lista_deudas(personas):
    lista_deudas = []
    for persona in personas:
        lista_deudas.append([persona, calcular_balance(persona)])
    return(lista_deudas)

def calcular_movimientos(lista_deudas):
    lista_deudas.sort(key=seleccionar_balance)
    if len(lista_deudas) < 1:
        return('')
    else:
        if -lista_deudas[0][1] < lista_deudas[-1][1]:
            lista_deudas[-1][1] += lista_deudas[0][1]
            return('{persona_paga} paga la cantidad de {cantidad}€ a {persona_recibe} \n'.format(persona_recibe=lista_deudas[-1][0], cantidad=-lista_deudas[0][1], persona_paga=lista_deudas[0][0]) + calcular_movimientos(lista_deudas[1:])) 
        elif -lista_deudas[0][1] > lista_deudas[-1][1]:
            lista_deudas[0][1] += lista_deudas[-1][1]
            return('{persona_paga} paga la cantidad de {cantidad}€ a {persona_recibe} \n'.format(persona_recibe=lista_deudas[-1][0], cantidad=lista_deudas[-1][1], persona_paga=lista_deudas[0][0]) + calcular_movimientos(lista_deudas[:-1]))
        else:
            return('{persona_paga} paga la cantidad de {cantidad}€ a {persona_recibe} \n'.format(persona_recibe=lista_deudas[-1][0], cantidad=-lista_deudas[0][1], persona_paga=lista_deudas[0][0]) + calcular_movimientos(lista_deudas[1:-1]))


