$(document).ready(function () {
    $.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function({hello}) {
        $("#hello").text(hello);
    });
});
