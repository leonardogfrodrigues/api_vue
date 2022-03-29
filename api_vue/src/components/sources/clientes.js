import { http } from './config'

export default {
    /*atualizar: (cliente) => {
        return http.put('cliente', cliente);
    },
*/
    listar: () => {
        return http.get('clientes')
    },

    salvar: (cliente) => {
        return http.post('cliente', cliente);
    },


    /* apagar: (cliente) => {
         return http.delete('cliente', { data: cliente })
     }*/
}