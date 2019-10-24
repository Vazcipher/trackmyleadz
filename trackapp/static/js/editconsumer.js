function validate() {
    let flag = 0;

    if ($('#fistname').val().length > 0) {
        $('#fistname').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#fistname').css("border-color", "red");
        flag--;
    }

    if ($('#lastname').val().length > 0) {
        $('#lastname').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#lastname').css("border-color", "red");
        flag--;
    }

    if ($('#email').val().length > 0) {
        $('#email').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#email').css("border-color", "red");
        flag--;
    }

    if ($('#address').val().length > 0) {
        $('#address').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#address').css("border-color", "red");
        flag--;
    }

    if ($('#phone').val().length > 0) {
        $('#phone').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#phone').css("border-color", "red");
        flag--;
    }


    if ($("input[name='gender']:checked").length > 0) {
        $('#male').css("color", "black");
        $('#female').css("color", "black");
        flag++;
    } else {
        $('#male').css("color", "red");
        $('#female').css("color", "red");
        flag--;
    }

    if (flag == 6) {
        return true;
    } else {
        return false;
    }
}

function fn_edit_consumer() {
    const isValid = validate()
    if (isValid) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/editconsumer/',
            type: 'POST',
            data: {
                fname: $('#fistname').val(),
                lname: $('#lastname').val(),
                email: $('#email').val(),
                phone: $('#phone').val(),
                address: $('#address').val(),
                gender: $("input[name='gender']:checked").val()
            },
            success: res => {
                $.toast({
                    text: res,
                    heading: 'Note',
                    icon: 'success',
                    showHideTransition: 'fade',
                    allowToastClose: true,
                    hideAfter: 3000,
                    stack: 5,
                    position: 'top-right',
                    textAlign: 'left',
                    loader: true,
                    loaderBg: '#9EC600',
                });
                $('#fistname').val('');
                $('#lastname').val('');
                $('#email').val('');
                $('#phone').val('');
                $('#adddress').val('');
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
