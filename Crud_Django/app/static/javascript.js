(function(win,doc){

    'use strict';

    // Verifica se realmente o usuário quer deletar o dado
    if (doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll ('.btnDel');
        for (let i = 0; i < btnDel.lenght ; i++){
            btnDel[i].addEventListener('click', function(event){

                if (confirm('Deseja mesmo apagar esse dado!')){
                    return true;
                }else{
                    event.preventDefaut();
                }

        });
     }
    }
}) (window,document);


