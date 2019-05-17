function crear_categoria() {
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
                $("#tabla_categoria tbody").append(
                    "<tr>" +
                      "<td>"+data.cat_list[0].cat+"</td>" +
                      "<td>"+data.cat_list[0].cat_nombre+"</td>" +
                      '<td><a href=""><i class="fa fa-trash-o"></i></a></td>' +
                    "</tr>"
                );
                swal.stopLoading();
                swal.close();
                
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
function Update_categoria(id) {
    swal({
        text: 'Actualizar Categoria',
        content: "input",
        button: {
            text: "Guardar!",
            closeModal: false,
        },
    }).then(valr => {

        if (!valr) throw null;
        var url = '/panel/tienda/categoria/update/';
        var data = { valor: valr, ID:id};
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
                $("#tabla_categoria tbody").append(
                    "<tr>" +
                      "<td>"+data.cat_list[0].cat+"</td>" +
                      "<td>"+data.cat_list[0].cat_nombre+"</td>" +
                      '<td><a href=""><i class="fa fa-trash-o"></i></a></td>' +
                    "</tr>"
                );
                swal.stopLoading();
                swal.close();
                
            }else{
                swal("Oh!", data.type, "warning");
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
