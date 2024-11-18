
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
        filmes.append({'titulo': titulo, 'diretor': diretor, 'ano_lancamento': ano_lancamento})
        print(f"\n✅ O filme '{titulo}' foi cadastrado com sucesso!")

        continuar = input('Deseja cadastrar outro filme? (s/n): ').strip().lower()
        if continuar == 'n':
            break



def listar_filmes():
    if not filmes:
        print("❌ Nenhum titulo cadastrado ainda.")
        input('Pressione Enter para voltar ao menu.')
        return


    print('🎥 Lista de Filmes 🎥')
    print('-' * 60)
    print(f"{'Título'.ljust(20)} | {'Diretor'.ljust(20)} | {'Ano de Lançamento'}")
    print('-' * 60)

    for filme in filmes:
        print(f"{filme['titulo'].ljust(20)} | {filme['diretor'].ljust(20)} | {filme['ano_lancamento']}")

    print('')
    input('Pressione Enter para voltar ao menu.')

def atualizar_filme():
    print('Atualizar Informações')
    titulo = input('Digite o título do filme que deseja atualizar: ').strip()
    for filme in filmes:
        if filme['titulo'].lower() == titulo.lower():
            print(f'Informações atuais: {filme}')

        novo_diretor = input('Digite o novo diretor (ou pressione Enter para manter o atual): ').strip()
        if novo_diretor:
            filme['diretor'] = novo_diretor

        novo_ano = input('Digite o novo ano de lançamento (ou pressione Enter para manter o atual): ')	  .strip()
        if novo_ano.isdigit():
            filme['ano_lancamento'] = int(novo_ano)

        print(f"\n✅ As informações do filme '{filme['titulo']}' foram atualizadas com sucesso!")
        input('Pressione Enter para voltar ao menu.')
        return

    print(f"❌ Filme '{titulo}' não encontrado.")
    input('Pressione Enter para voltar ao menu.')

def excluir_filme():
    if not filmes:
        print("❌ Nenhum título cadastrado ainda.")
        input('Pressione Enter para voltar ao menu.')
        return



    titulo = input('Digite o título do filme que deseja excluir: ').strip()
    for i, filme in enumerate(filmes):
        if filme['titulo'].lower() == titulo.lower():
            filmes.pop(i)
            print(f"\n✅ O filme '{filme['titulo']}' foi excluído com sucesso!")
            input('Pressione Enter para voltar ao menu.')
            return

    print(f"❌ Filme '{titulo}' não encontrado.")
    input('Pressione Enter para voltar ao menu.')



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
                print("\n👋 Obrigado por usar o Gerenciamento de Filmes! Até a próxima!")
                break
            else:
                print('❌ Opção inválida. Escolha entre 1 e 5.')

                input('Pressione Enter para voltar ao menu.')
        except ValueError:
            print('❌ Insira um número válido.')
            input('Pressione Enter para voltar ao menu.')




if __name__ == '__main__':
    main()

