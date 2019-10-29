$(document).ready(() => {

    $("#view_product").hide();

    $("#New").click(() => {
        $("#table").show();
        $("#view_product").hide();
    });

    $("#view").click(() => {
        $("#view_product").show();
        $("#table").hide();
    });

});

function validate() {
    let flag = 0;

    if ($('#code').val().length > 0) {
        flag++;
        $('#code').css("border-color", "#ced4da");
    } else {
        flag--;
        $('#code').css("border-color", "red");
    }

    if ($('#pr_name').val().length > 0) {
        flag++;
        $('#pr_name').css("border-color", "#ced4da");
    } else {
        flag--;
        $('#pr_name').css("border-color", "red");
    }

    if ($('#pr_desc').val().length > 0) {
        flag++;
        $('#pr_desc').css("border-color", "#ced4da");
    } else {
        flag--;
        $('#pr_desc').css("border-color", "red");
    }

    if ($('#pr_cost').val().length > 0) {
        flag++;
        $('#pr_cost').css("border-color", "#ced4da");
    } else {
        flag--;
        $('#pr_cost').css("border-color", "red");
    }

    if (flag == 4) {
        return true;
    } else {
        return false;
    }
}

function edit_validate() {
    let flag = 0;

    if ($('#productcode').val().length > 0) {
        $('#productcode').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#productcode').css("border-color", "red");
        flag--;
    }

    if ($('#productname').val().length > 0) {
        $('#productname').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#productname').css("border-color", "red");
        flag--;
    }

    if ($('#cost').val().length > 0) {
        $('#cost').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#cost').css("border-color", "red");
        flag--;
    }

    if ($('#desc').val().length > 0) {
        $('#desc').css("border-color", "#ced4da");
        flag++;
    } else {
        $('#desc').css("border-color", "red");
        flag--;
    }
    if (flag == 4) {
        return true;
    } else {
        return false;
    }
}

function fn_save_product() {
    const isValid = validate();
    if (isValid) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/createProduct/',
            type: 'POST',
            data: {
                pro_code: $('#code').val(),
                pro_name: $('#pr_name').val(),
                pro_cost: $('#pr_cost').val(),
                pro_desc: $('#pr_desc').val()
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
                $('#code').val('');
                $('#pr_name').val('');
                $('#pr_cost').val('');
                $('#pr_desc').val('');
                setTimeout(() => {
                    location.reload();
                }, 1500);
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
        })
    }
}

function fn_delete_product(pro_id) {
    const check = confirm('Are you sure you want to delete this product')
    if (check) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/delete_product/',
            type: 'POST',
            data: {
                pro_id: pro_id
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
}
function fn_edit_product(product_id, csrfmiddlewaretoken) {
    const isValid = edit_validate()
    if (isValid) {
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/editproduct/',
            type: 'POST',
            data: {
                product_id,
                csrfmiddlewaretoken,
                pcode: $('#productcode').val(),
                pname: $('#productname').val(),
                cost: $('#cost').val(),
                desc: $('#desc').val(),
               
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
                $('#productcode').val('');
                $('#productname').val('');
                $('#cost').val('');
                $('#desc').val('');
                
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