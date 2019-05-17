$(document).ready(function () {
    // Limitare text din casute pe baza de randuri, cu ellipsis la final
    var modules = document.getElementsByClassName("js-text-clamp");

    $.each(modules, function (index, module) {
        $clamp(module, {clamp: 6});
    });
});