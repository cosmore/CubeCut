var openMenu = null;
var restApi = ""

function setRestApi(ip, port, app) {
     restApi = "http://" + ip + ":" + port + "/" + app + "/command/"
}

function init() {

    $('.button-menu').hide();

    $('.menu').click(

        function(e) {

            var menu = "#" + $(this).data('menu');
            var m = $(menu)

            if(m.css("visibility") == 'visible')
            {
                m.css("visibility", 'collapse')
                m.css("display", 'none')
                openMenu = null;
            }
            else                
            {
                console.log("vis")
                if (openMenu != null) {
                    openMenu.css("visibility", 'collapse')
                    openMenu.css("display", 'none')
                }
                openMenu = m;
                openMenu.css("visibility", 'visible')
                m.css("display", 'flex')
            }            
        }
    );

    $('[data-command]').click(
        function(e) {
            var cmd = $(this).data('command');
            var url = restApi + cmd;
            jQuery.get( url, function(response) { console.log(response)} );
    } );

}

$( document ).ready( init )
