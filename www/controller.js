
$(document).ready(function () {



    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $('.siri-message li:first').text(message);
        $('.siri-message').textillate('start');
    }
    eel.expose(Showhood)
    function Showhood() {
        $("#oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }
}
);
