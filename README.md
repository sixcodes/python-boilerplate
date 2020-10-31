# Python Boilerplate

A ideia desse projeto é já ser um "start" para seu projeto python. O que temos aqui são configurações pré prontas para que você possa se dedicar inteiramente ao código do seu projeto.


## Pipfile

O Pipfile já tráz algumas dependencias de desenvolvimento, como:

```
asynctest = "==0.12.1"
pytest = "==4.0.1"
pytest-cov = "==2.6.0"
codecov = "==1.0.0"
mypy = "==0.630"
black = "==18.9b0"
isort = "==4.3.15"
```

O Pipfile já vem com alguns scripts que ajudam nas tarefas do dia a dia e nas checagens do CI.

- ``pipenv run test``

    Roda os testes do projeto. Esse script está configurado para medir a cobertura do pacote ``myproj``. Esse pacote deve ser ajustado para o pacote onde seu código vai ficar.

- ``pipenv run lint``

    Roda o ``mypy`` para fazer checagem estática de tipos no código.

- ``pipenv run fmt`` e ``pipenv run fmt-check``

    Roda o black para formatar o código. O comando ``pipenv run fmt-check`` apenas checa se alguma formatação seria necessária. É útil para rodar no processo de CI.

- ``pipenv run isort`` e ``pipenv run isort-check``

    Formata o código ordenando os imports usando o projeto isort. O comando ``pipenv run isort-check`` apenas checa se algum import precisa ser reformatado. É útil para rodar no processo de CI.


# CI/CD

Esse repositorio já possui alguns workflows do Github Actions pré-configurados. Os workflows são:

- `.github/workflows/pull-request.yaml`

    Esse workflow roda em cada PR aberto no projeto. Roda os testes em múltiplas versões do python e faz checagem de formatação de código, lint (com mypy) e formatação de imports (com isort).

    Esse workflow faz também upload do relatório de coverage para o [codeclimate](https://codeclimate.com). Perceba que o upload é feito em apenas um versão do python, isso porque o codeclimate rejeita múltiplos upload para um mesmo commit, então precisamos escolher uma das rodadas de teste para fazer o upload.

    Para que o upload para o codeclimate funciona você precisa criar um token no CodeClimate e colocar esse token como um secret no seu repositório. O Nome do secret **deve ser**: ``CC_TEST_REPORTER_ID``. Mais sobre a documentação do codeclimate com githubactions: https://docs.codeclimate.com/docs/github-actions-test-coverage

# Pydantic - Configuração baseada em variáveis de ambiente

Para facilitar na criação de um novo serviço e seguindo as boas práticas definidas no [12factors](https://12factor.net/config) sobre configurações.
Adicionamos o uso no pydantic para criar e validar essas informações para nós.

Exemplo de uso:

```python
    from config import settings

    print(settings.DEBUG)
```

Para configurar uma variável de ambiente é necessário ficar atento ao prefixo.
o default do projeto verificar inicialmente para uma variável de ambiente chamada `NAMESPACE`caso não a
encontre o prefixo será `DEV_`, o que isso significa?

O uso ficará da seguinte forma quando configuramos o namespace sempre adicionaremos o prefixo no
momento de exportar as variaveis de ambiente.

```python
    NAMESPACE=PROD PROD_DEBUG=False python main.py
```

Caso não definimos nenhum namespace, o prefixo será `DEV`, ou seja

```python
    DEV_REDIS_PORT=1234 python main.py
```

Lembrando que dentro da sua aplicação o que vale é justamente o nome que foi definido no arquivo config.py, sem o prefixo.
