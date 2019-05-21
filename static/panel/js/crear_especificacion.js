function crear_item() {
    swal({
        text: 'Añadir nuevo item',
        content: "input",
        button: {
            text: "Guardar!",
            closeModal: false,
        },
    }).then(valor => {

        if (!valor) throw null;
        var url = '/panel/tienda/item/crear/';
        var data = { item: valor };
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
                $('#id_esp_item').append($('<option>', {
                    value: data.obj_list[0].item,
                    text: data.obj_list[0].item_nombre
                }));
                swal.stopLoading();
                swal.close();
                $('#id_esp_item').val(data.obj_list[0].item)
            }else{
                swal("Oh!", data.type.item_nombre[0], "error");
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