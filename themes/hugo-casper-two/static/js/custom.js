$(document).ready(function () {
    var modules = document.getElementsByClassName("js-text-clamp");

    $.each(modules, function (index, module) {
        $clamp(module, {clamp: 6});
    });
});