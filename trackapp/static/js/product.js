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

    if($('#pr_desc').val().length > 0) {
        flag++;
        $('#pr_desc').css("border-color", "#ced4da");
    } else {
        flag--;
        $('#pr_desc').css("border-color", "red");
    }

    if($('#pr_cost').val().length > 0) {
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
                console.log(res);
            },
            error: err => {
                console.log(err);
            }
        })
    }
}
