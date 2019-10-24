function fn_update_enquiery(lead_id, csrfmiddlewaretoken) {

    $.ajax({
        url: 'http://127.0.0.1:8000/trackapp/editenquiry/',
        type: 'POST',
        data: {
            lead_id,
            csrfmiddlewaretoken,
            lead_stage: $('#lead_stage').val(),
            lead_source: $('#lead_source').val(),
            product: $('#product').val(),
            employee: $('#employee').val(),
            desc: $('#desc').val(),
            email: $('#email').val(),
            phone: $('#phone').val()
        },
        success: res => {
            console.log(res);
        },
        error: err => {
            console.log(err);
        }
    });

}