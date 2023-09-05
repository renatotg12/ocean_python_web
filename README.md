# Ocean Tech School

TRILHA Eventos Ocean Brasil

05/09/2023 - Renato Teixeira Gomes - renatotg10@gmail.com

Documentação criada com auxílio do ChatGPT (https://chat.openai.com/)

## Programando para Web com Python, CSS e HTML

### Criando um novo repositório local

```bash
echo "# ocean_python_web" >> README.md 
git init 
git add README.md 
git commit -m "primeiro commit" 
git branch -M main 
git remote add origin https://github.com/renatotg12/ocean_python_web.git
git push - sua origem principal
```

Esse código é um conjunto de comandos do Git, uma ferramenta de controle de versão, que realiza as seguintes ações:

1. `echo "# ocean_python_web" >> README.md`: Este comando adiciona um cabeçalho "# ocean_python_web" ao arquivo README.md. Isso é comumente usado para criar ou atualizar o arquivo README de um repositório Git com informações sobre o projeto.

2. `git init`: Inicializa um novo repositório Git no diretório local. Isso cria uma estrutura inicial para rastrear as mudanças nos arquivos do projeto.

3. `git add README.md`: Adiciona o arquivo README.md ao índice de mudanças do Git. Isso significa que o Git começará a rastrear as alterações neste arquivo.

4. `git commit -m "primeiro commit"`: Realiza um commit (confirmação) das mudanças adicionadas ao índice. O argumento `-m` permite adicionar uma mensagem de commit, que neste caso é "primeiro commit".

5. `git branch -M main`: Renomeia o nome padrão da branch principal de "master" para "main". Isso é uma prática comum para evitar terminologia que possa ser considerada insensível.

6. `git remote add origin https://github.com/renatotg12/ocean_python_web.git`: Adiciona um controle remoto chamado "origin" ao repositório local. Este controle remoto está associado à URL fornecida, que é o endereço do repositório remoto no GitHub.

7. `git push -u origin main`: Envia as mudanças (o commit "primeiro commit" e a branch "main" renomeada) para o repositório remoto no GitHub. O argumento `-u` configura a branch local "main" para acompanhar a branch remota "main". Isso permite que você simplesmente use `git push` no futuro para enviar alterações para a branch principal no GitHub.

Exemplo:
Suponha que você tenha um projeto chamado "ocean_python_web" e queira começar a rastrear as mudanças no Git e enviá-las para o GitHub. Você executa esses comandos em um diretório vazio onde o projeto está localizado. Após a execução desses comandos, o projeto será inicializado como um repositório Git local e as mudanças iniciais serão enviadas para o GitHub.

A partir desse ponto, você pode continuar trabalhando em seu projeto, fazendo commits, push de alterações e colaborando com outros desenvolvedores por meio do repositório GitHub.

### Exemplos de comandos GIT:

1. **Clonar um repositório remoto para o seu computador:**

   ```bash
   git clone https://github.com/usuario/exemplo.git
   ```

   Isso cria uma cópia local de um repositório remoto no GitHub em seu computador.

2. **Criar uma nova branch e mudar para ela:**

   ```bash
   git checkout -b minha-nova-feature
   ```

   Isso cria uma nova branch chamada "minha-nova-feature" e a torna a branch atual.

3. **Adicionar arquivos para commit:**

   ```bash
   git add arquivo1.py arquivo2.py
   ```

   Isso adiciona os arquivos especificados ao índice, preparando-os para um commit.

4. **Fazer um commit das mudanças:**

   ```bash
   git commit -m "Adiciona funcionalidade X"
   ```

   Isso cria um commit com uma mensagem descritiva das mudanças feitas.

5. **Enviar mudanças para o repositório remoto:**

   ```bash
   git push origin minha-nova-feature
   ```

   Isso envia os commits da branch atual ("minha-nova-feature") para o repositório remoto.

6. **Atualizar sua branch local com as mudanças do repositório remoto:**

   ```bash
   git pull origin main
   ```

   Isso atualiza sua branch local com as mudanças da branch principal do repositório remoto.

7. **Verificar o histórico de commits:**

   ```bash
   git log
   ```

   Isso mostra o histórico de commits no seu repositório local.

8. **Criar uma tag para uma versão específica:**

   ```bash
   git tag -a v1.0 -m "Versão 1.0"
   ```

   Isso cria uma tag chamada "v1.0" associada ao commit atual.

9. **Listar todas as tags:**

   ```bash
   git tag
   ```

   Isso lista todas as tags no repositório.

10. **Reverter um commit em uma branch:**

    ```bash
    git revert <ID_DO_COMMIT>
    ```

    Isso cria um novo commit que desfaz as mudanças introduzidas pelo commit especificado.

Estes são apenas alguns exemplos básicos de comandos Git. O Git oferece uma ampla gama de recursos para gerenciar seu fluxo de trabalho de desenvolvimento e colaboração com outros desenvolvedores em um projeto. Certifique-se de consultar a documentação oficial do Git para aprender mais sobre suas capacidades avançadas.

## Comandos GIT

### 1. `git status`

O comando `git status` é usado para verificar o estado atual do seu repositório Git. Ele fornece informações sobre quais arquivos foram modificados, adicionados ou removidos desde o último commit. É uma ferramenta útil para entender o que está acontecendo no seu projeto.

Exemplo de uso:
```bash
git status
```

### 2. `git add .`

O comando `git add .` é usado para adicionar todas as mudanças no diretório de trabalho ao índice (staging area) do Git. Isso significa que as mudanças serão preparadas para serem incluídas no próximo commit.

Exemplo de uso:
```bash
git add .
```

### 3. `git commit -am`

O comando `git commit -am "mensagem"` é usado para criar um novo commit que inclui todas as mudanças no índice com uma mensagem de commit associada. O `-a` indica que todas as mudanças (exceto arquivos não rastreados) devem ser incluídas no commit, e o `m` permite que você forneça uma mensagem de commit.

Exemplo de uso:
```bash
git commit -am "Adiciona novos recursos"
```

### 4. `git branch`

O comando `git branch` é usado para listar todas as branches no seu repositório Git. Ele exibe todas as branches locais e indica qual é a branch atual (a que está marcada com um asterisco).

Exemplo de uso:
```bash
git branch
```

### 5. `git push origin`

O comando `git push origin` é usado para enviar as mudanças do branch atual para um repositório remoto. O `origin` é o nome padrão do repositório remoto associado ao seu repositório local.

Exemplo de uso:
```bash
git push origin main
```

Neste exemplo, estamos enviando as mudanças do branch "main" para o repositório remoto. Certifique-se de substituir "main" pelo nome da branch que você deseja enviar. Este comando atualiza o repositório remoto com as mudanças que você fez localmente.

Lembre-se de que o Git é uma ferramenta poderosa para o controle de versão e colaboração em projetos de desenvolvimento de software. Os comandos mencionados acima são apenas alguns dos comandos básicos que você usará com frequência ao trabalhar com Git. Existem muitos outros comandos e recursos avançados disponíveis para gerenciar seu repositório Git de forma eficaz.