function fn_save_enquiery() {
    const isValid = validate()
    console.log(isValid);
    if (isValid) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/createEnquiry/',
            type: 'POST',
            data: {
                consumer: $('#consumer').val(),
                email: $('#email').val(),
                phone: $('#phone').val(),
                lead_stage: $('#lead_stage').val(),
                lead_source: $('#lead_source').val(),
                product: $('#product').val(),
                assigned: $('#assigned').val(),
                description: $('#des').val()

            },
            success: res => {
                $.toast({
                    text: res,
                    heading: 'Note',
                    icon: 'success',
                    showHideTransition: 'fade',
                    allowToastClose: true,
                    hideAfter: 1500,
                    stack: 5,
                    position: 'top-right',
                    textAlign: 'left',
                    loader: true,
                    loaderBg: '#9EC600',
                });
                $('#consumer').val('');
                $('#email').val('');
                $('#phone').val('');
                $('#lead_stage').val('');
                $('#lead_source').val('');
                $('#product').val('');
                $('#assigned').val('');
                $('#des').val('');
            },
            error: e => {
                $.toast({
                    text: e,
                    heading: 'Note',
                    icon: 'error',
                    showHideTransition: 'fade',
                    allowToastClose: true,
                    hideAfter: 3000,
                    stack: 5,
                    position: 'top-right',
                    textAlign: 'left',
                    loader: true,
                    loaderBg: '#9EC600',
                });
            }
        });
    } else {
        console.log('not valid')
    }
}

function fn_delete_enquiry(lead_id) {
    $.ajax({
        url: 'http://127.0.0.1:8000/trackapp/delete_enquiry/',
        type: 'POST',
        data: {
            lead_id: lead_id
        },
        success: del => {
            $.toast({
                text: del,
                heading: 'Note',
                icon: 'success',
                showHideTransition: 'fade',
                allowToastClose: true,
                hideAfter: 2000,
                stack: 5,
                position: 'top-right',
                textAlign: 'left',
                loader: true,
                loaderBg: '#9EC600'
            });
        },
        error: e => {
            $.toast({
                text: e,
                heading: 'Note',
                icon: 'error',
                showHideTransition: 'fade',
                allowToastClose: true,
                hideAfter: 3000,
                stack: 5,
                position: 'top-right',
                textAlign: 'left',
                loader: true,
                loaderBg: '#9EC600',
            });
        }

    });

}