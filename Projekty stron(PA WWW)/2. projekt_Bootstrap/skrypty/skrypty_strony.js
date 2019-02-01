
/* Funkcja popover ze słownika pojęć */
$(document).ready(function(){
    $('[class="pojecie"]').popover();
});

/* Funkcja ukrywajaca popovery i pokazujaca liste pojec*/
function hideAll() {
    var x = document.getElementsByClassName("ukrywanie");
    var el = document.getElementById("ukrywacz");
    for (i = 0; i < x.length; i++) {
        if (x[i].style.display === "none") {
            x[i].style.display = "block";
        } else {
            x[i].style.display = "none";
        }
    }

    /* faza pokazania pojec z listy */
    var y = document.getElementById("pelnaLista");

    if (y.style.display === "none") {
        y.style.display = "block";
        el.firstChild.data = "Ukryj wszystkie pojęcia";
    } else {
        y.style.display = "none";
        el.firstChild.data = "Pokaż wszystkie pojęcia za pomocą listy";
    }
}

/* Funkcja dla galerii zdjęć */
$(document).ready(function(){
    $(".fancybox").fancybox({
        openEffect: "none",
        closeEffect: "none"
    });

    $(".zoom").hover(function(){

        $(this).addClass('transition');
    }, function(){

        $(this).removeClass('transition');
    });
});