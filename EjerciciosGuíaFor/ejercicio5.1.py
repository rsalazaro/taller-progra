horas = [55,4,7,7,12,12,20,20,23,5]
minutos = [30,29,40,70,0,30,15,40,15,29]

indice = 0

for hora in horas:
    # Aplicando la validación de datos
    if hora >= 0 and hora <= 23:
        if minutos[indice] >= 0 and minutos[indice] <=60:
            if hora >= 5 and hora < 12:
                if hora == 5 and minutos[indice] < 30:
                    print('[%d:%d] Buenas noches' %(hora, minutos[indice]))
                else:
                    print('[%d:%d] Buenos días' %(hora, minutos[indice]))
            elif hora >= 12 and hora <= 20:
                if hora == 12 and minutos[indice] == 0:
                    print('[%d:%d] Buenos días' %(hora, minutos[indice]))
                elif hora == 20 and minutos[indice] > 15:
                    print('[%d:%d] Buenas noches' %(hora, minutos[indice]))
                else:
                    print('[%d:%d] Buenas tardes' %(hora, minutos[indice]))
            else:
                print('[%d:%d] Buenas noches' %(hora, minutos[indice]))
            
        else:
            print('El minuto %d no es un minuto válido' %minutos[indice])
    else:
        print('La hora %d no es una hora válida' %hora)
    
    # Importante, el incremento del indice va al final, o podría causar errores
    indice = indice + 1