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

}