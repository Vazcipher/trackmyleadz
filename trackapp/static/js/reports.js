function validate() {

    let flag = 0;

    if ($('#leadid').val().length > 0) {
        flag++;
        $('#leadid').css("border-color", "#ced4da");
    } else {
        flag--;
        $('#leadid').css("border-color", "red");
    }

    if ($('#fdatePickerId').val().length > 0) {
        flag++;
        $('#fdatePickerId').css("border-color", "#ced4da");
    } else {
        flag--;
        $('#fdatePickerId').css("border-color", "red");
    }

    if ($('#tdatePickerId').val().length > 0) {
        flag++;
        $('#tdatePickerId').css("border-color", "#ced4da");
    } else {
        flag--;
        $('#tdatePickerId').css("border-color", "red");
    }
    if (flag == 3) {
        return true;
    } else {
        return false;
    }
}