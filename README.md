# Servidor de Desafios

## Como usar

### Criando novos desafios

Entre no Django admin (`/admin/challenges/challenge`) e clique 
em `ADICIONAR CHALLENGE`. A data limite não é obrigatória. A opção 
`Function name` define qual deve ser o nome da função enviada pelo aluno.

O arquivo de testes define a bateria de testes pelos quais a função enviada pelo
aluno passará. Ele deve seguir o seguinte exemplo:

    from challenge_test_lib import challenge_test as ch

    # O nome da classe deve necessariamente ser TestCase
    class TestCase(ch.TestCaseWrapper):
        TIMEOUT = 2  # Limite de tempo em segundos por teste (default: 3s)
    
        # A mensagem de erro é definida por meio de um decorator.
        # Ela não é obrigatória. Caso não seja definida, uma mensagem
        # padrão será apresentada em caso de erro.
        # Todos os testes devem começar com 'test_'
        @ch.error_message('Verificar quando os argumentos forem zero')
        def test_argumentos_zero(self):
            # A challenge_test_lib foi construída com base no unittest.
            # Assim, quaisquer asserts do unittest podem ser utilizados.
            # Para mais opções: 
            # https://docs.python.org/3/library/unittest.html#assert-methods
            # A função submetida pelo aluno estará disponível como 
            # self.challenge_fun. Neste exemplo ela recebe 3 argumentos, 
            # mas a quantidade e tipo dos argumentos pode ser diferente
            self.assertAlmostEquals(self.challenge_fun(0, 0, 0), 0.0)

        # Outro exemplo de teste
        @ch.error_message('Verificar quando o número de meses é zero')
        def test_zero_meses(self):
            self.assertAlmostEquals(self.challenge_fun(100, 0, 0.1), 100.0)


## Configuração do servidor

### Setup

Todas as dependências estão no arquivo `requirements.txt`:

    $ pip install -r requirements.txt

Além disso, é necessário instalar a biblioteca customizada de execução de testes. 
Para isso, vá até a pasta `ChallengeTestRunner` e instale a biblioteca:

    $ cd ChallengeTestRunner
    $ python setup.py install
   
### Servidor de Produção

Para utilizar as configurações de produção é necessário que o arquivo 
`InsperProgChallenges/production_settings.py` exista (ele pode estar vazio).

Para atualizar o servidor de produção basta executar um `git pull` e reiniciar o 
Apache.

### Configuração do lambda

Execute o script `prepare_lambda_code.sh`. Faça o upload do arquivo 
`lambda_code.zip` na função `testRunner` na Amazon.