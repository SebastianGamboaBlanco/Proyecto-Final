
$('#formulario').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: '/',
        data: $('form').serialize(),
        type: 'POST',
        success: function (texto) {
            console.log(texto);
        },
        error: function () {
            console.log('Mal hecho');
        }
    })
});