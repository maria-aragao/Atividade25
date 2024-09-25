# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

def contar_aprovados():
    aprovado = 0
    total_alunos = 5

    for i in range(total_alunos):
        try:
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            
            if nota >= 7:
                aprovado += 1
                
        except ValueError:
            print("Por favor, digite uma nota válida.")
            continue  # Ignora a iteração atual e pede a nota novamente

    print(f"Total de alunos aprovados: {aprovado}")

contar_aprovados()
