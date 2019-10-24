function fn_save_password() {
    
    let flag = 0;
    
    if ($('#old').val().length > 0) {
        $('#old').css("border-color",'#ced4da');
        flag++;
    } else {
        $('#old').css("border-color",'red'); 
    }

    if ($('#new').val().length > 0) {
        $('#new').css("border-color",'#ced4da');
        flag++;
    } else {
        $('#new').css("border-color",'red'); 
    }

    if ($('#confirm').val().length > 0) {
        $('#confirm').css("border-color",'#ced4da');
        if ($('#new').val() == $('#confirm').val()) {
            $('#confirm').css("border-color",'#ced4da');
            flag++;
        } else {
            $('#confirm').css("border-color",'red'); 
        }
    } else {
        $('#confirm').css("border-color",'red'); 
    }


    if (flag == 3) {

        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/changePassword/',
            type: 'POST',
            data: {
                oldpass: $('#old').val(),
                newpass: $('#new').val(),
            },
            success: res => {
                $('#myModal').modal('hide');
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
        return false;
    }
}