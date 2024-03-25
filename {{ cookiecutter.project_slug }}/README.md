# Name Service

## Stack da API

## Execução da API
Primeiro você precisa do `pyenv` e do `poetry`, para gerenciar o `python` e o ambiente virtual, respectivamente. Caso não tenha instalado, aqui está uma [documentação](https://github.com/nayannanara/poetry-documentation) para te ajudar.

Em seguida, execute:

``` shell
pyenv local 3.12
poetry env use 3.12
poetry install
```

Crie um arquivo `.env` e insira as credenciais de `local.env`

Execute também para instalar o `pre-commit`:

```shell
make setup-dev
```

Para subir o banco de dados e o rabbitmq, caso não tenha o [docker](https://docs.docker.com/engine/install/ubuntu/) e o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
docker-compose up -d
```

## API

Para subir a API, execute:
```bash
make run
```
e acesse: http://127.0.0.1:8000/docs


## Executar testes

Para executar os testes, execute:

```bash
make test
```

Caso queira executar um teste específico, execute:

```bash
make test-matching K=nomedoteste
```
