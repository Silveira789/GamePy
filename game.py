from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3, 4]: \n'))

    calc: Calcular = Calcular(dificuldade)

    print(f"Informe o resultado da seguinte operação: ")
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo ? [1 - sim, 0 - não] \n'))

    if continuar == 1:
        print('')
        jogar(pontos)
    elif continuar == 0:
        print("_______________________________________")
        print(f'Você finalizou com {pontos} ponto(s)')
        print('Fim de jogo, obrigado por jogar!')
    else:
        print('Opção inválida!!')


if __name__ == '__main__':
    main()
