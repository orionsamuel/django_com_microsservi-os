$(document).ready(() => {
    (function(win, doc){
        'use strict';

        //Verifica se o usuário realmente quer deletar o dado
        if(doc.querySelector('.btnDel')){
            let btnDel = doc.querySelectorAll('.btnDel');
            for(let i = 0; i < btnDel.length; i++){
                btnDel[i].addEventListener('click', function(event){
                    if(confirm("Tem certeza que quer deletar?")){
                        return true;
                    }else{
                        event.preventDefault();
                    }
                });
            }
        }
        
        const modalBase = $('#modalCadastro')
        modalBase.on('show.bs.modal', function (e) {
            const button = e.relatedTarget
            let check = button.getAttribute('data-bs-check')
            let id = button.getAttribute('data-bs-id-pizza')
            let title = button.getAttribute('data-bs-title')
            let description = button.getAttribute('data-bs-description')
            let type = button.getAttribute('data-bs-type')
            let creator = button.getAttribute('data-bs-creator')

            if(check === 'true'){
                $('#btn-salvar').html("Atualizar")
                document.getElementById('form').action = '/update/'+id+'/'
            }else{
                $('#btn-salvar').html("Cadastrar")
                document.getElementById('form').action = '/pizzas/create/'
            }

            $('#check_edit').val(check)
            $('#id-pizza').val(id)
            $('#id_title').val(title)
            $('#id_description').val(description)
            $('#id_type').val(type)
            $('#id_creator').val(creator)
        })
        
    })(window,document);
})