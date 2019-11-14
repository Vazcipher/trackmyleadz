
$(document).ready(() => {

    $("#table").hide();

    $("#New").click(() => {
        $("#view_emp").hide();
        $("#table").show();
    });

    $("#View").click(() => {
        $("#view_emp").show();
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

    if ($('#un').val().length > 0) {
        $('#un').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#un').css("border-color", "red");
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

    if ($('#pw').val().length > 0) {
        $('#pw').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#pw').css("border-color", "red");
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
    
    if(flag > 0) {
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
    if ($('#firstname').val().length > 0) {
        $('#firstname').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#firstname').css("border-color", "red");
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
        $('#emai').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#email').css("border-color", "red");
        flag--;
    }

    if ($('#mobile').val().length > 0) {
        $('#mobile').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#mobile').css("border-color", "red");
        flag--;
    }

    if ($('#address').val().length > 0) {
        $('#address').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#address').css("border-color", "red");
        flag--;
    }

    if ($("input[name='e_gender']:checked").length > 0) {
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
function editm_validate(){
    var mobile1 = document.getElementById("mobile").value;
    var email1 =document.getElementById("email").value;
    var pattern = /^\d{10}$/;
    var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (pattern.test(mobile1) && regex.test(email1)) {
        //alert("Your mobile number : " + mobile);
        
         return true;
        }
        else if (pattern.test(mobile1) == false) {
            //alert("It is not valid mobile number.input 10 digits number!");
            alert("enter valid mobile");
            $('#mobile').css("border-color", "red");
            
            return false;
        }
        else{
            alert("enter valid email");
            $('#email').css("border-color", "red");
        }
}


function fn_save_employee() {
    const isValid = validate();
    const isValid1= mvalidate();
    if (isValid && isValid1) {
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
                    heading: 'Note',
                    icon: 'success',
                    showHideTransition: 'fade',
                    allowToastClose: true,
                    hideAfter: 2000,
                    stack: 5,
                    position: 'top-right',
                    textAlign: 'left',
                    loader: true,
                    loaderBg: '#9EC600',
                });
                $('#fn').val("");
                $('#ln').val("");
                $('#un').val("");
                $('#pw').val("");
                $('#em').val("");
                $('#ph').val("");
                $('#dd').val("");
                $('#loc').val("");
                $("input[name='gender']").prop('checked', false);
                $('#role').val("")
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

function fn_edit_employee(id, csrfmiddlewaretoken) {
    const isValid = edit_validate();
    const isValid1 =editm_validate();
    if (isValid && isValid1) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/editemployee/',
            type: 'POST',
            data: {
                id,
                csrfmiddlewaretoken,
                firstname: $('#firstname').val(),
                lastname: $('#lastname').val(),
                email: $('#email').val(),
                mobile: $('#mobile').val(),
                location: $('#address').val(),
                gender: $("input[name='e_gender']:checked").val()
            },
            success: res => {
                $.toast({
                    text: res,
                    heading: 'Note',
                    icon: 'success',
                    showHideTransition: 'fade',
                    allowToastClose: true,
                    hideAfter: 2000,
                    stack: 5,
                    position: 'top-right',
                    textAlign: 'left',
                    loader: true,
                    loaderBg: '#9EC600',
                });
                $('#firstname').val("");
                $('#lastname').val("");
                $('#email').val("");
                $('#mobile').val("");
                $('#address').val("");
                $("input[name='e_gender']").prop('checked', false);
                $('#role').val("")
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

function fn_delete_employee(user_id) {
    const check = confirm('Are you sure you want to delete this employee')
    if (check) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/delete_employee/',
            type: 'POST',
            data: {
                user_id: user_id
            },
            success: del => {
                $.toast({
                    text: del,
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