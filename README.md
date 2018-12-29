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