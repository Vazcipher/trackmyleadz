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

    if ($('#un').val().length > 0) {
        $('#un').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#un').css("border-color", "red");
        flag--;
    }

    if ($('#pw').val().length > 0) {
        $('#pw').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#pw').css("border-color", "red");
        flag--;
    }

    if ($('#em').val().length > 0) {
        $('#em').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#em').css("border-color", "red");
        flag--;
    }

    if ($('#ph').val().length > 0) {
        $('#ph').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#ph').css("border-color", "red");
        flag--;
    }

    if ($('#dd').val().length > 0) {
        $('#dd').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#dd').css("border-color", "red");
        flag--;
    }

    if ($('#loc').val().length > 0) {
        $('#loc').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#loc').css("border-color", "red");
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

    if ($('#role').val().length > 0) {
        $('#role').css("border-color", "#ced4da");
        flag++
    } else {
        flag--;
        $('#role').css("border-color", "red");
    }

    if (flag == 10) {
        return true;
    } else {
        return false;
    }
}


function fn_save_employee() {
    const isValid = validate();
    if (isValid) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/createEmployee/',
            type: 'POST',
            data: {
                fname: $('#fn').val(),
                lname: $('#ln').val(),
                uname: $('#un').val(),
                password: $('#pw').val(),
                email: $('#em').val(),
                phone: $('#ph').val(),
                dob: $('#dd').val(),
                location: $('#loc').val(),
                gender: $("input[name='gender']:checked").val(),
                role: $('#role').val()
            },
            success: res => {
                $.toast({
                    text: res,
                    heading: 'Note', // Optional heading to be shown on the toast
                    icon: 'warning', // Type of toast icon
                    showHideTransition: 'fade', // fade, slide or plain
                    allowToastClose: true, // Boolean value true or false
                    hideAfter: 3000, // false to make it sticky or number representing the miliseconds as time after which toast needs to be hidden
                    stack: 5, // false if there should be only one toast at a time or a number representing the maximum number of toasts to be shown at a time
                    position: 'bottom-left', // bottom-left or bottom-right or bottom-center or top-left or top-right or top-center or mid-center or an object representing the left, right, top, bottom values
                    textAlign: 'left',  // Text alignment i.e. left, right or center
                    loader: true,  // Whether to show loader or not. True by default
                    loaderBg: '#9EC600',  // Background color of the toast loader
                });
            },
            error: e => {
                $.toast({
                    text: res,
                    heading: 'Note', // Optional heading to be shown on the toast
                    icon: 'warning', // Type of toast icon
                    showHideTransition: 'fade', // fade, slide or plain
                    allowToastClose: true, // Boolean value true or false
                    hideAfter: 3000, // false to make it sticky or number representing the miliseconds as time after which toast needs to be hidden
                    stack: 5, // false if there should be only one toast at a time or a number representing the maximum number of toasts to be shown at a time
                    position: 'bottom-left', // bottom-left or bottom-right or bottom-center or top-left or top-right or top-center or mid-center or an object representing the left, right, top, bottom values
                    textAlign: 'left',  // Text alignment i.e. left, right or center
                    loader: true,  // Whether to show loader or not. True by default
                    loaderBg: '#9EC600',  // Background color of the toast loader
                });
            }
        });
    } else {
        console.log('not valid')
    }
}
