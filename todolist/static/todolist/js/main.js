$(document).ready(function () {
    $('button').click(function () {
        $(this).parent().remove();
        let id = $(this).data('id')
        $.ajax({
            method: 'DELETE',
            url: 'delete/'+ id ,
            beforeSend: function(xhr){
                xhr.setRequestHeader('x-CSRFToken',csrf_token)
            },
        })
    })

    $('html').niceScroll({
        cursorcolor: '#067e7e',
        cursorborder: 'none',
        scrollspeed: '100'
    });
})