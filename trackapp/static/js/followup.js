// $(document).ready(() => {
//     $("#table1").hide();

//     $("#New").click(() => {
//         $("#view_enq").hide();
//         $("#table").show();
//     });

//     $("#view").click(() => {
//         $("#view_enq").show();
//         $("#table").hide();
//     });
//     $("#add").click(() => {
    
//         $("#table").show();
//         $("#table1").show();
        

//     });
//     $(document).ready( () =>{
//     $("#Collapse").click(() => {
//     	let flag=true;
// 			let f=true;
// 			jQuery('#link2').click( () => {
             
// 				if(flag==true)
// 				{
// 				$('#Collapse').slideUp();
// 				flag=false;
// 			    }
// 			    else
// 			    {
            
// 			    $('#add').slideDown();
// 			    flag=true;
// 			   }
//             });
//         });

             
//              });
// 		});

$(document).ready( ()=>{
    $('#link').click( ()=>{
        $('#table1').show();
    });
    $('#link1').click( ()=>{
        $('#table1').hide();
    })
});


function fn_folowup(){
    $.ajax({
        url: 'http://127.0.0.1:8000/trackapp/savefollowup/',
            type: 'POST',
            data: {
                description: $('#discription').val(),
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
                $('#description').val('');
               
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
