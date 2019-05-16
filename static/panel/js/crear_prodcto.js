function crear_categoria(token) {
    swal({
        text: 'Añadir nueva categoria',
        content: "input",
        button: {
            text: "Guardar!",
            closeModal: false,
        },
    }).then(categoria => {

        if (!categoria) throw null;
        var url = '/panel/tienda/categoria/crear/';
        var data = { cat_nombre: categoria };
        return fetch(url, {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data),
            headers: {
                //   'Accept': 'application/json',
                'Content-Type': 'application/json',
                "X-CSRFToken": Cookies.get('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            },
            credentials: 'include'
        });


    }).then(res => res.json())
        .then(data => {
            if (data.status) {
                $('#id_prod_categoria').append($('<option>', {
                    value: data.cat_list[0].cat,
                    text: data.cat_list[0].cat_nombre
                }));
                swal.stopLoading();
                swal.close();
                $('#id_prod_categoria').val(data.cat_list[0].cat)
            }else{
                swal("Oh!", data.type.cat_nombre[0], "error");
                swal.stopLoading();
                swal.close();
            }


        })
        .catch(err => {
            console.log(err)
            if (err) {
                swal("Oh!", "Al parecer a ocurrido un error!", "error");
            }
        })

}

// var frm = $('#Form-oducto');
// console.log(frm.serialize())
