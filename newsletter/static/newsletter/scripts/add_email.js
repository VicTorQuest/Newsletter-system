$(document).ready(function() {
    $('#addEmailForm').submit(function(e) {
        e.preventDefault()

        $('.save-btn').html(`<div class='spinner-border spinner-border-sm' role='status'><span class='visually-hidden'>Loading...</span></div>`)
        $('.save-btn').css('pointer-events','none')


        var email = $('#addedMail').val()
        var csrf_token = $(this)[0].csrfmiddlewaretoken.value


        $.ajax({
            type: 'POST',
            url: '/add-email/',
            data: {'csrfmiddlewaretoken': csrf_token, 'email': email},
            success: function(success) {
                $('#addEmailForm').trigger('reset')
                $('#addedMail').css('border', '1px solid #dee2e6')
                $('.save-btn').css('pointer-events','')
                $('.save-btn').html(`Save`)
                $('#allemails').append(`<option value="${success.email_id}">${success.email}</option>`)
                $('.message').html(`<span class='text-success'>${success.message}</span>`)

            },
            
            error: function(error) {
                $('#addedMail').css('border', '1px solid red')
                $('.save-btn').css('pointer-events','')
                $('.save-btn').html(`Save`)
                $('.message').html(`<span class='text-danger'>${error.responseText}</span>`)
            }

        })
    })
})