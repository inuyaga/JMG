var app = new Vue({
    el: '#app',
    data: {
        imgs: {},
        media_img: [],
        short_name: ''
    },
    delimiters: ["[[", "]]"],

    methods: {
        processFile(event) {
            this.media_img = event.target.files[0]
            this.short_name = event.target.files[0].name
        }, 
        delete_img(id){
            axios.get('/panel/tienda/media/delete/?delete_id='+id)
            .then(function (response) {
                // handle success
                console.log(response.data.imgs);
                app.imgs=response.data.imgs
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .finally(function () {
                // always executed
            });
        }

    },
    mounted() {
        axios.get('/panel/tienda/media/get_list')
            .then(function (response) {
                // handle success
                console.log(response.data.imgs);
                app.imgs=response.data.imgs
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .finally(function () {
                // always executed
            });
    },

    computed: {

    }

})


var frm = $('#Form-media');

frm.submit(function (e) {

    e.preventDefault();
    var formData = new FormData(this);

    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            console.log(data)
            app.short_name = ''
            app.imgs=data.imgs
            $('#Form-media').trigger("reset");
            $( "input:even" ).removeClass( "is-invalid" );
        },
        error: function (data) {
            console.log('An error occurred.');
            // console.log(data.responseJSON['media_img']);
            for (const prop in data.responseJSON) {
                console.log(prop+'='+data.responseJSON[prop]);
                $( "#id_"+prop ).after( '<div class="invalid-feedback">'+data.responseJSON[prop]+'</div>' );
                $("#id_"+prop).addClass( "is-invalid" );
              }
            

        },
    });
});

