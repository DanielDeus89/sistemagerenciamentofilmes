# Sistema Gerenciamento Filmes
 
---

Atividade: Sistema de Gerenciamento de Filmes

Crie um programa que gerencie uma lista de filmes. O programa deve oferecer as seguintes opções no menu:

---

 Funcionalidades
1. Cadastrar novo filme:
   - Solicite o título, o diretor e o ano de lançamento.
   - Verifique se o título do filme já está cadastrado (não permita duplicatas).
   - Certifique-se de que o ano é um número válido e que o filme não seja do futuro (ano <= ano atual).

2. Listar filmes cadastrados:
   - Exiba os filmes em formato de tabela, com as colunas:
     - Título
     - Diretor
     - Ano de Lançamento

3. Atualizar informações de um filme:
   - Solicite o título do filme.
   - Permita alterar o diretor e/ou o ano de lançamento.

4. Excluir um filme:
   - Solicite o título do filme a ser excluído e remova-o da lista, caso exista.

5. Sair do programa:
   - Finalize o programa exibindo uma mensagem de despedida.

---

 Estrutura do Menu
O menu deve ser exibido repetidamente até que o usuário escolha sair.

Exemplo:
```
🎥 GERENCIAMENTO DE FILMES 🎥
1. Cadastrar novo filme
2. Listar filmes cadastrados
3. Atualizar informações de um filme
4. Excluir um filme
5. Sair

Escolha uma opção: _
```

---

 Regras
- Use uma lista para armazenar os filmes no formato:
  ```python
  {'titulo': 'Matrix', 'diretor': 'Lana e Lilly Wachowski', 'ano_lancamento': 1999}
  ```
- Valide todas as entradas:
  - O título do filme não pode estar vazio.
  - O ano de lançamento deve ser um número inteiro válido.
  - O título não pode ser duplicado.
- Exiba mensagens claras e amigáveis para o usuário.

---

 Exemplo de Execução

 Cadastrar Filme
```
Digite o título do filme: Matrix
Digite o diretor do filme: Lana e Lilly Wachowski
Digite o ano de lançamento: 1999

✅ O filme 'Matrix' foi cadastrado com sucesso!
```

 Listar Filmes
```
🎥 Lista de Filmes 🎥
------------------------------------------
Título               | Diretor             | Ano de Lançamento
--------------------------------------------------------------
Matrix               | Lana e Lilly Wachowski | 1999
```

 Atualizar Informações
```
Digite o título do filme que deseja atualizar: Matrix

Informações atuais: {'titulo': 'Matrix', 'diretor': 'Lana e Lilly Wachowski', 'ano_lancamento': 1999}
Digite o novo diretor (ou pressione Enter para manter o atual): James Cameron
Digite o novo ano de lançamento (ou pressione Enter para manter o atual): 1999

✅ As informações do filme 'Matrix' foram atualizadas com sucesso!
```

 Excluir Filme
```
Digite o título do filme que deseja excluir: Matrix

✅ O filme 'Matrix' foi excluído com sucesso!
```

---

 Como Começar
1. Crie funções para cada opção do menu:
   - `cadastrar_filme`
   - `listar_filmes`
   - `atualizar_filme`
   - `excluir_filme`
2. Use um loop `while` no `main()` para exibir o menu e chamar as funções.
3. Teste entradas válidas e inválidas para cada funcionalidade.

---
