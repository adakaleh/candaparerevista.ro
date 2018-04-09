$(document).ready(function () {
    var modules = document.getElementsByClassName("js-text-clamp");

    $.each(modules, function (index, module) {
        if(index > 0){
            $clamp(module, {clamp: 6});
        }
    });
});