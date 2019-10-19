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

Trás também script já pronto para checagem do código:

### Pytest

Já temos o comando para rodar os testes dos seu código com report de cobertura.

`pipenv run test`

### Mypy

Já temos um script pronto que roda o `mypy`, para fazer análise estátia no seu código. Muito útil para quem já usa type hints.

`pipenv run lint`

### Black

Usamos o `black` para formatar o código na tentativa de terminar com as discussões sobre fomatação. Deixe a formatação para um formatador e concentre-se na lógica do código. =D

`pipenv run fmt` para efetivamente formatar o código. Recomendado rodar a cada save ou antes de comitar.
`pipenv run fmt-check` para colocar no seu pipeline, pois caso algum código esteja fora do padrão de formatação fará o build falhar.

### isort

Usamos o isort para ordenar os imports do seu código. Os parâmetros do isort geram uma formatação compatível com o black. Dessa forma podemos rodar os dois e eles concordarão em relação à versão final do código formatado.

`pipenv run isort` para ordenar os imports.
`pipenv run isort-check` para checar se existe algum import fora do lugar, útil para colocar em seu pipeline.

# CI/CD

Uma configuração do circleci já está pronta em `.circleci/config.yml`. Pode ser usada pra rodar a pipeline de build/check do seu projeto.


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

`lembrando que dentro da sua aplicação o que vale é justamente o nome que foi definido no arquivo config.py, sem o prefixo`
