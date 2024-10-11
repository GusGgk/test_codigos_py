def contar_a(s):
    # Converte a string para minúsculas para facilitar a contagem
    s_lower = s.lower()
    
    # Conta a quantidade de 'a's
    count = s_lower.count('a')
    
    # Verifica se a letra 'a' existe
    if count > 0:
        print(f"A letra 'a' aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Entrada do usuário
string_input = input("Informe uma palavra: ")
contar_a(string_input)
