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
        $('$pr_name').css("border-color", "red");
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


