$(document).ready( () => {
	
    $("#table").hide();

    $("#New").click( () => {
        $("#view_enq").hide();
        $("#table").show();
    });

    $("#view").click( () => {
        $("#view_enq").show();
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
            success: res => console.log(res),
            error: e => console.log(e)
        });
    } else {
        console.log('not valid')
    }
}
