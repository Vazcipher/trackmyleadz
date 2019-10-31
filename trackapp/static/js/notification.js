let notifications = []

function fn_get_notification() {
    $.ajax({
        url: 'http://127.0.0.1:8000/trackapp/getNotification',
        type: 'GET',
        success: res => {
            const notification = res['notifications'];
            if (notification.length > notifications.length) {
                notifications = notification
            }
        },
        error: err => {
            $.toast({
                text: 'Network failure',
                heading: 'Error',
                icon: 'error',
                showHideTransition: 'fade',
                allowToastClose: true,
                hideAfter: 3000,
                stack: 1,
                position: 'bottom-left',
                textAlign: 'left',
                loader: false,
                loaderBg: '#9EC600',
            });
        }
    })
}

let x = 0;
setInterval(() => {
    fn_get_notification();
    if (notifications.length > $('#notification').children().length) {
        $('#notification').append(
            "<a class='dropdown-item' href='#'>" + notifications[x].notification_title + "</a>"
        )
        $.toast({
            text: notifications[x].notification_title,
            heading: 'Notification',
            icon: 'info',
            showHideTransition: 'fade',
            allowToastClose: true,
            hideAfter: 3000,
            stack: 5,
            position: 'bottom-left',
            textAlign: 'left',
            loader: false,
            loaderBg: '#9EC600',
        });
        x++;
    }
}, 2000);