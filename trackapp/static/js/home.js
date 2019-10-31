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
function validate(){
    let flag = 0;
    if ($('#fname').val().length > 0) {
        $('#fname').css("border-color",'#ced4da');
        flag++;
    }
    else {
        $('#fname').css("border-color",'red'); 
    }
    if ($('#lastname').val().length > 0) {
        $('#lastname').css("border-color",'#ced4da');
        flag++;
    }
    else{
        $('#lastname').css("border-color",'red');
    }
    if ($('#email').val().length > 0) {
        $('#email').css("border-color",'#ced4da');
        flag++;
    } 
    else {
        $('#email').css("border-color",'red'); 
        
    }
    if ($('#address').val().length > 0) {
        $('#address').css("border-color",'#ced4da');
        flag++;
    } 
    else {
        $('#address').css("border-color",'red'); 
    
    }
    if ($('#phone').val().length > 0) {
        $('#phone').css("border-color",'#ced4da');
        flag++;
    } 
    else {
        $('#phone').css("border-color",'red'); 
        
    }
    if ($('#date1').val().length > 0) {
        $('#date1').css("border-color",'#ced4da');
        flag++;
    } 
    else {
        $('#date1').css("border-color",'red'); 
    
    }
    if ($("input[name='gender']:checked").length > 0) {
        $('#g1').css("color", "black");
        $('#g2').css("color", "black");
        flag++;
    } 
    else {
        $('#g1').css("color", "red");
        $('#g2').css("color", "red");
    
    }
     if(flag>0){
         return true;
        }

    }

function fn_save_profile(){

     const isValid =validate()
     if(isValid){

        $.ajax({
        url: 'http://127.0.0.1:8000/trackapp/saveprofile/',
        type: 'POST',
        data: {
            fname: $('#fname').val(),
            lname: $('#lname').val(),
            email: $('#email').val(),
            address: $('#address').val(),
            mobile: $('#phone').val(),
            dob: $('#date1').val(),
            gender:$("input[name='gender']:checked").val()
       },
        success: res => {
            $('#profile').modal('hide');
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
            $('#fname').val();
            $('#lname').val();
            $('#email').val();
            $('#address').val();
            $('#phone').val();
            $('#date1').val();
            $("input[name='gender]:checked").val();

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
    else{
        console.log('not valid')
    }
}
