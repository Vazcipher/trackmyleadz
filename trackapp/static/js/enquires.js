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
