$(document).ready(() => {

    let hidden = true;
    $('#collapse-btn').click(() => {
        if (hidden) {
            $('#collapse-btn').html('- Collapse');
            hidden = false;
        } else {
            $('#collapse-btn').html('+ Add follow ups');
            hidden = true;
        }
    });

});

function fvalidate() {
    let flag = 0 ;
    if ($('#fdatePickerId').val().length > 0) {
        $('#fdatePickerId').css("border-color", "#ced4da");
        flag++;
    } 
    else {
        $('#fdatePickerId').css("border-color", "red");
        flag--;
    }
    if ($('#tdatePickerId').val().length > 0) {
        $('#tdatePickerId').css("border-color", "#ced4da");
        flag++;
    } 
    else {
        $('#tdatePickerId').css("border-color", "red");
        flag--;
    }
    if (flag == 2) {
        return true;
    } 
    else {
        return false;
    }

}



function fn_delete_followup(followup_id) {
    $.ajax({
        url: 'http://127.0.0.1:8000/trackapp/removeFollowup/',
        type: 'POST',
        data: {
            followup_id
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
            setTimeout(() => {
                window.location.reload();
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
    });
}


function fn_finish_followup(followup_id) {
    $.ajax({
        url: 'http://127.0.0.1:8000/trackapp/finishFollowup/',
        type: 'POST',
        data: {
            followup_id 
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
            $('#Plan').val('');
            setTimeout(() => {
                window.location.reload();
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
    });
}


function fn_save_followup(lead_id) {

    if ($('#Plan').val().length > 0) {

        $('#Plan').css("border-color", "#ced4da");
        $.ajax({
            url: 'http://127.0.0.1:8000/trackapp/savefollowup/',
            type: 'POST',
            data: {
                lead_id: lead_id,
                desc: $('#Plan').val(),
                title: $('#name').val()
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
                $('#Plan').val('');
                setTimeout(() => {
                    window.location.reload();
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
        });
    } else {
        $('#Plan').css("border-color", "red");
    }

}