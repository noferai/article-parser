$('#preview').on('click', function (event) {
    event.preventDefault();
    let csrftoken = $('[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        headers: {
            "X-CSRFToken": csrftoken,
        },
        data: $('form').serialize(),
        success: (response) => {
            Object.entries(response).forEach(([key, value]) => $('#preview-' + key + ' .card-body').text(value))
        },
        error: (response) => alert(response.responseText)
    });
});


