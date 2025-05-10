def inverter_string(texto): # criei uma função chamada inverter string que vai receber um texto
    invertida = "" # variável vazia pra guardar o texto invertido
    for caractere in texto: #loop por cada letra que estiver no texto
        invertida = caractere + invertida  
    return invertida 


entrada = input("Digite uma palavra ou frase para inverter: ") #receber a palavra do usuario 


resultado = inverter_string(entrada) #chamando a função


print("String invertida:", resultado)
