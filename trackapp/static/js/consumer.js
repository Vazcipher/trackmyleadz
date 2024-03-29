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

    if (flag > 0) {
        return true;
    } 
}
function mvalidate(){
    var mobile = document.getElementById("ph").value;
    var email =document.getElementById("em").value;
    var pattern = /^\d{10}$/;
    var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (pattern.test(mobile) && regex.test(email)) {
        //alert("Your mobile number : " + mobile);
        
         return true;
        }
        else if (pattern.test(mobile) == false) {
            //alert("It is not valid mobile number.input 10 digits number!");
            alert("enter valid mobile");
            $('#ph').css("border-color", "red");
            
            return false;
        }
        else{
            alert("enter valid email");
            $('#em').css("border-color", "red");
        }

}

function edit_validate() {
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

    if ($("input[name='c_gender']:checked").length > 0) {
        $('#male').css("color", "black");
        $('#female').css("color", "black");
        flag++;
    } else {
        $('#male').css("color", "red");
        $('#female').css("color", "red");
        flag--;
    }

    if (flag > 0) {
        return true;
    } 
}
function editm_validate(){
    var mobile = document.getElementById("phone").value;
    var email1 =document.getElementById("email").value;
    var pattern = /^\d{10}$/;
    var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (pattern.test(mobile) && regex.test(email1)) {
        //alert("Your mobile number : " + mobile);
        
         return true;
        }
        else if (pattern.test(mobile) == false) {
            //alert("It is not valid mobile number.input 10 digits number!");
            alert("enter valid mobile");
            $('#phone').css("border-color", "red");
            
            return false;
        }
        else{
            alert("enter valid email");
            $('#email').css("border-color", "red");
        }

}

function fn_save_consumer() {
    const isValid = validate()
    const isValid1 = mvalidate();
    if (isValid && isValid1) {
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
                    hideAfter: 1500,
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
                $("input[name='gender']").prop('checked', false);
                setTimeout(() => {
                    location.reload(true);
                }, 1500)
                
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
                setTimeout(() => {
                    location.reload(true);
                }, 1500)

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


}

function fn_edit_consumer(consumer_id, csrfmiddlewaretoken) {
    const isValid = edit_validate();
    const isValid1 =editm_validate();
    if (isValid && isValid1)  {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/editconsumer/',
            type: 'POST',
            data: {
                consumer_id,
                csrfmiddlewaretoken,
                fname: $('#fistname').val(),
                lname: $('#lastname').val(),
                email: $('#email').val(),
                phone: $('#phone').val(),
                address: $('#address').val(),
                gender: $("input[name='c_gender']:checked").val()
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
                $('#fistname').val(""),
                $('#lastname').val(""),
                $('#email').val(""),
                $('#phone').val(""),
                $('#address').val(""),
                $("input[name='c_gender']:checked").val("")
                setTimeout(() => {
                    location.reload(true);
                }, 1500)

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
}