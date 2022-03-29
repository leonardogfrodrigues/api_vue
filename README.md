<h1> API Rest </h1>

[![npm](https://img.shields.io/npm/v/vue-gapi.svg)](https://www.npmjs.com/package/vue-gapi) [![vuejs3](https://img.shields.io/badge/vue.js-3.x-brightgreen.svg?logo=vue.js)](https://v3.vuejs.org/)

## Sobre o Projeto
Consiste em uma API com interface frontend que permite realizar o cadastro de cliente com as seguintes características:

- Suporta GET, POST, DELETE, UPDATE
- Gera logs com nível 1, 2, 3, 4, 5
- Suporta banco de dados nosql
- Possui documentação declarada através de um endpoint

### Construído com:

- [Vue.js](https://vuejs.org/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [TinyDB](https://tinydb.readthedocs.io/en/latest/)

## Começando
### Pré-requisitos

Para utilizar e trabalhar neste projeto, você precisa instalar o Docker para executar a imagem criada.

Você pode instalar o Docker seguindo as [instruções] disponíveis no site oficial(https://docs.docker.com/get-docker/).

### Instalação
Para configurar o projeto localmente, siga os passos a seguir:

1. Puxe a imagem abaixo para executar a API localmente:

```shell
docker pull 
```
  
Como compilar o backend:

- Criar um ambiente virtuall com: python -m venv venv
- Instalar da biblioteca Flask: pip install flask
- Instalar a biblioteca de aplicações Werkzeug: pip install Werkzeug==0.16.0 (ou se requerido: pip install Werkzeug==2.0.3
- Instalar Flask-Pydantic-Spec para validação dos dados: pip install flask-pydantic-spec
- Instalar o TinyDB: pip install tinydb
- Instalar Flask-Cors para possíveis intercorrências ao rodar o frontend no navegador: pip install flask-cors
- Para rodar a API (backend): python main.py

Compilando o frontend:

- Após instalar o VUEjs, no terminal (podendo ser no terminal de seu editor) digite: vue create api_vue
- Acesse o diretório criado (na minha máquina foi acessado com: cd .\api_vue\
- Instale a Axios para estabelecer a conexão com o backend com: npm install axios --save
- Compile com: npm run serve 
