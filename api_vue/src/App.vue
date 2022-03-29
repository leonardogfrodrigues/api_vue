Vue.createApp({
  data() {
    return {
      counter: 1
    }
  }
}).mount('#basic-event')
<template>
  <div id="app">
    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="#" class="brand-logo center">Cadastro de Clientes</a>
      </div>
    </nav>

    <div class="container">
      <ul>
        <li v-for="(erro, index) of errors" :key="index">
          campo <b>{{ erro.field }}</b> - {{ erro.defaultMessage }}
        </li>
      </ul>

      <form>
        <label>Nome</label>
        <input type="text" placeholder="Nome" v-model="cliente.nome" />
        <label>Telefone</label>
        <input type="text" placeholder="Telefone" v-model="cliente.telefone" />
        <label>E-mail</label>
        <input type="text" placeholder="Email" v-model="cliente.email" />
        <label>Endereco</label>
        <input type="text" placeholder="Endereco" v-model="cliente.endereco" />
        <label>Profissao</label>
        <input
          type="text"
          placeholder="Profissao"
          v-model="cliente.profissao"
        />
        <label>Upload curriculo</label><br /><br />

        <input type="file" name="Cadastro" /><br /><br />
        <div id="basic-event">
          <button onclick="alert(Enviado com sucesso!)">Enviar</button><br><br>
          <button>Novo cadastro</button>
          </div>
         <!-- <p>O botão acima foi clicado {{ counter }} vezes.</p>
        
         <Popup>
          <p>Enviado com sucesso!</p>
        </Popup>-->
      </form>

      <!-- <td>
              <button
                @click="editar(cliente)"
                class="waves-effect btn-small blue darken-1"
              >
                <i class="material-icons">create</i>
              </button>
              <button
                @click="remover(cliente)"
                class="waves-effect btn-small red darken-1"
              >
                <i class="material-icons">delete_sweep</i>
              </button>
            </td>-->
    </div>
  </div>
</template>

<script>
import Cliente from "./components/sources/clientes";
import Popup from "./components/Popup";

export default {
  name: "app",
  data() {
    return {
      cliente: {
        telefone: "",
        nome: "",
        email: "",
        endereco: "",
        profissao: "",
        curriculo: "",
      },
      clientes: [],
      errors: [],
    };
  },
  mounted() {
    Cliente.listar().then((resposta) => {
      console.log(resposta);
    });
    // this.listar()
  },
};

/* methods:
  {

    listar()
    {
      Cliente.listar().then(resposta => {
        this.clientes = resposta.data
      }).catch(e => {
        console.log(e)
      })
    }*/

/*  salvar()
    {
      if(!this.cliente.telefone){
        Cliente.salvar(this.cliente).then(resposta => {
          this.cliente = {}
          alert('Cadastrado com sucesso!')
          this.listar()
          this.errors = {}
        }).catch(e => {
          this.errors = e.response.data.errors
        })
      }else{
        Cliente.atualizar(this.cliente).then(resposta => {
          this.cliente = {}
          this.errors = {}
          alert('Atualizado com sucesso!')
          this.listar()
        }).catch(e => {
          this.errors = e.response.data.errors
        })
      }

      Cliente.salvar(this.cliente).then(resposta => {
        alert('Cadastrado!')
      })

    }

    editar(cliente)
    {
      this.cliente = cliente
    }
    remover(cliente)
    {
      if(confirm('Deseja excluir o cliente?')){
        Cliente.apagar(cliente).then(resposta => {
          this.listar()
          this.errors = {}
        }).catch(e => {
          this.errors = e.response.data.errors
        })
      }
    }
  }
*/
</script>


