$(document).ready(() => {

    $("#table").hide();

    $("#New").click(() => {
        $("#view_cons").hide();
        $("#table").show();
    });

    $("#view").click(() => {
        $("#view_cons").show();
        $("#table").hide();
    });

});

function validate() {
    let flag = 0;

    if ($('#fn').val().length > 0) {
        $('#fn').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#fn').css("border-color", "red");
        flag--;
    }

    if ($('#ln').val().length > 0) {
        $('#ln').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#ln').css("border-color", "red");
        flag--;
    }

    if ($('#em').val().length > 0) {
        $('#em').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#em').css("border-color", "red");
        flag--;
    }

    if ($('#ad').val().length > 0) {
        $('#ad').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#ad').css("border-color", "red");
        flag--;
    }

    if ($('#ph').val().length > 0) {
        $('#ph').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#ph').css("border-color", "red");
        flag--;
    }


    if ($("input[name='gender']:checked").length > 0) {
        $('#g1').css("color", "black");
        $('#g2').css("color", "black");
        flag++;
    } else {
        $('#g1').css("color", "red");
        $('#g2').css("color", "red");
        flag--;
    }

    if (flag == 6) {
        return true;
    } else {
        return false;
    }
}

function fn_save_consumer() {
    const isValid = validate()
    if (isValid) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/createConsumer/',
            type: 'POST',
            data: {
                fname: $('#fn').val(),
                lname: $('#ln').val(),
                email: $('#em').val(),
                phone: $('#ph').val(),
                address: $('#ad').val(),
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
                $('#fn').val('');
                $('#ln').val('');
                $('#em').val('');
                $('#ph').val('');
                $('#ad').val('');
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

function fn_delete_consumer(consumer_id) {
    const check = confirm('Are you sure you want to delete this consumer')
    if (check) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/delete_consumer/',
            type: 'POST',
            data: {
                consumer_id: consumer_id
            },
            success: del => {
                $.toast({
                    text: del,
                    heading: 'Note',
                    icon: 'success',
                    showHideTransition: 'fade',
                    allowToastClose: true,
                    hideAfter: 3000,
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
                    gender: $("input[name='e_gender']:checked").val()
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
                    $('#address').val('');
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
}