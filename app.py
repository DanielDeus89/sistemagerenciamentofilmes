
filmes = [ ]

def exibir_opcoes():
    print('''
🎥 GERENCIAMENTO DE FILMES 🎥
1. Cadastrar novo filme
2. Listar filmes cadastrados
3. Atualizar informações de um filme
4. Excluir um filme
5. Sair
    ''')

def cadastrar_filme():
    while True:
        # Validação do título
        titulo = input('Digite o título do filme: ').strip()
        if not titulo:
            print('❌ O título do filme não pode estar vazio! Tente novamente.')
            continue

        # Verificar duplicatas
        if any(filme['titulo'].lower() == titulo.lower() for filme in filmes):
            print('❌ Este filme já está cadastrado! Tente outro.')
            continue

        # Validação do diretor
        diretor = input('Digite o diretor do filme: ').strip()
        if not diretor:
            print('❌ O diretor do filme não pode estar vazio! Tente novamente.')
            continue

        # Validação do ano de lançamento
        while True:
            try:
                ano_lancamento = int(input('Digite o ano de lançamento: ').strip())
                if ano_lancamento > 0:
                    break
                else:
                    print('❌ O ano de lançamento deve ser um número positivo válido.')
            except ValueError:
                print('❌ Insira um número válido para o ano de lançamento.')

        # Armazenar o filme
        dados_do_filme = {'titulo': titulo, 'diretor': diretor, 'ano_lancamento': ano_lancamento}
        filmes.append(dados_do_filme)

        print(f"\n✅ O filme '{titulo}' foi cadastrado com sucesso!")

        # Perguntar se deseja cadastrar outro filme
        while True:
            continuar = input('Deseja cadastrar outro filme? (s/n): ').strip().lower()
            if continuar == 's':
                break  # Reinicia o loop para cadastrar outro filme
            elif continuar == 'n':
                print("\n👍 Cadastro concluído! Retornando ao menu principal...")
                return  # Sai da função e retorna ao menu principal
            else:
                print('❌ Opção inválida! Digite "s" para Sim ou "n" para Não.')


def listar_filmes():
    if not filmes:
        print("❌ Nenhum titulo cadastrado ainda.")
        print('')
        input('Enter para voltar para Menu')
        return


    print('🎥 Lista de Filmes 🎥')
    print('-'*60)
    print('Título'.ljust(15) + '|  Diretor'.ljust(25) + '| Ano de Lançamento')
    print('-'*60)

    for filme in filmes:
        busca_filme = filme['titulo']
        busca_diretor = filme['diretor']
        busca_ano = filme['ano_lancamento']

        print(f"{busca_filme.ljust(14)} | {busca_diretor.ljust(35)} | {busca_ano}")

    print('')
    input('Enter para voltar para Menu')

def atualizar_filme():
    print('Atualizar Informações')
    titulo = input('Digite o título do filme que deseja atualizar: ')
    for filme in filmes:
        if filme['titulo'].lower() == titulo.lower():
            print(f'Informações atuais: {filme}')

        novo_diretor = input('Digite o novo diretor (ou pressione Enter para manter o atual): ')
        if novo_diretor:
            filme['diretor'] = novo_diretor

        novo_ano = int(input('Digite o novo ano de lançamento (ou pressione Enter para manter o atual): '))
        if novo_ano > 0:
            filme['ano_lancamento'] = novo_ano

        print(f"\n✅ As informações do livro '{filme['titulo']}' foram atualizadas com sucesso!")
        return

    print(f"❌ Livro '{titulo}' não encontrado.")

    print('')
    input('Enter para voltar para Menu')

def excluir_filme():
    if not filmes:
        print("❌ Nenhum titulo cadastrado ainda.")
        print('')
        input('Enter para voltar para Menu')
        return



    titulo = print(input('Digite o título do filme que deseja excluir: '))
    for i, filme in enumerate(filmes):
        filmes.pop(i)
        print(f"\n✅ O filme '{filme['titulo']} foi excluído com sucesso!")
        return



def main():
    while True:
        exibir_opcoes()
        try:
            opcao = int(input('Escolha uma opção: _'))

            if opcao == 1:
                cadastrar_filme()
            elif opcao == 2:
                listar_filmes()
            elif opcao == 3:
                atualizar_filme()
            elif opcao == 4:
                excluir_filme()
            elif opcao == 5:
                break
            else:
                print('❌ Opção inválida. Escolha entre 1 e 5.')
                print('')
                input('Enter para voltar para Menu')
        except ValueError:
            print('❌ Insira um número válido.')
            print('')
            input('Enter para voltar para Menu')





if __name__ == '__main__':
    main()

