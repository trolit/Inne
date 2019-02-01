$(document).ready(function(){
    $( ".f-item-1" ).hover(function() {
        $('.menu').css("background-color", "#E94B3C");
    }, function(){
        $('.menu').css("background-color", "#BC70A4");
    });
    // f-item-2
    $( ".f-item-2" ).hover(function() {
        $('.menu').css("background-color", "#2E4A62");
    }, function(){
        $('.menu').css("background-color", "#BC70A4");
    });
    // f-item-3
    $( ".f-item-3" ).hover(function() {
        $('.menu').css("background-color", "#672E3B");
    }, function(){
        $('.menu').css("background-color", "#BC70A4");
    });
    // f-item-4
    $( ".f-item-4" ).hover(function() {
        $('.menu').css("background-color", "#838487");
    }, function(){
        $('.menu').css("background-color", "#BC70A4");
    });
    // f-item-5
    $( ".f-item-5" ).hover(function() {
        $('.menu').css("background-color", "#006E51");
    }, function(){
        $('.menu').css("background-color", "#BC70A4");
    });
});

// WSTRZYKIWANIE AJAXEM STRON
$(document).ready(function() {
    $('a').on('click', function() {
        var url=$(this).attr('href');
        $('#info').load(url+'#newsItem');

        return false;
    }); //koniec funkcji click
}); // koniec funkcji ready


// STRONA GLOWA - WCZYTAJ
function GoMainPage(){
    window.location="index.html";
}

// POKAZ O FUNKCJI
function DisplayText(id){
    var x = document.getElementById(id);

    if(x.style.display === 'none') {
        x.style.display = 'block';
    }
    else {
        x.style.display = 'none';
    }
}