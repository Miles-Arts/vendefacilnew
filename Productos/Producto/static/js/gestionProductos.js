(function(){
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('¿Desea Eliminar el Producto?')

            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();
