function searchOrderFn(table){
    // datatable on search customize url to point to API
    table.on( 'search.dt', function () {
        // console.log( 'Currently applied global search: '+table.search() );
        ajax_url = table.ajax.url();
        table.ajax.url(ajax_url+'&search='+table.search());
        // table.draw();
    });
    // datatble on column ordering 
    table.on( 'order.dt', function () {
        // This will show: "Ordering on column 1 (asc)", for example
        ajax_url = table.ajax.url();
        var order = table.order();
        column_name = table.settings().init().columns[order[0][0]].data;
        if(order[0][1] == 'desc')
            column_name = '-'+column_name;

        table.ajax.url(ajax_url+'&ordering='+column_name);
    })
}