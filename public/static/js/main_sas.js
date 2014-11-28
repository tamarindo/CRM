/* basi js */
function sendAjax(url, params, myCallback, args) {
    if (typeof args === "undefined") {
        load_elem = "#load";
    } else {
        load_elem = args.load_elem;
    }
    /*$(load_elem).show().html('<img src="/static/img/load16.gif" />');*/
    $(load_elem).show().html('Cargando...');
    if (typeof args === "undefined" || args.met === "get") {
        $.get(url, params)
                .done(function(data) {
            myCallback(data);
            $(load_elem).fadeOut();
        }).fail(function(error) {
            console.log(error);
        });
    } else if (args.met === "post") {
        $.post(url, params)
                .done(function(data) {
            myCallback(data);
            $(load_elem).fadeOut();
        }).fail(function(error) {
            console.log(error);
        });
    }
}



