# Simulando a situação com três interruptores e lâmpadas

# Função para identificar qual interruptor controla cada lâmpada
def identificar_lampadas():
    # Estado dos interruptores (0 = desligado, 1 = ligado)
    interruptores = {
        'Interruptor 1': 1,  # Primeiro interruptor ligado
        'Interruptor 2': 0,  # Segundo interruptor desligado
        'Interruptor 3': 0   # Terceiro interruptor desligado
    }

    # Simulando o atraso de 10 minutos (apenas uma representação)
    print("Ligue o primeiro interruptor por 10 minutos...")
    # Agora, desligue o primeiro interruptor e ligue o segundo
    interruptores['Interruptor 1'] = 0  # Desligar primeiro
    interruptores['Interruptor 2'] = 1  # Ligar segundo

    # Verificando as lâmpadas
    print("\nVerifique as lâmpadas na sala:")
    
    # Identificando as lâmpadas
    for interruptor, estado in interruptores.items():
        if estado == 1:
            print(f"A lâmpada controlada por {interruptor} está ligada.")
        else:
            print(f"A lâmpada controlada por {interruptor} está desligada.")
    
    print("\nConclusão:")
    print("1. A lâmpada ligada é do Interruptor 2.")
    print("2. A lâmpada desligada e quente é do Interruptor 1.")
    print("3. A lâmpada desligada e fria é do Interruptor 3.")

# Chamando a função
identificar_lampadas()
