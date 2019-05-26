var id;

function menu_destacar(ancora){

    id = ancora;
    var links = $('a');
    i = 0;
    while(i<links.length)
    {
        $(links[i]).removeClass("active-1")
        i++;
    }
    $("#"+ancora).addClass("active-1");

}

function destaque(){
    var path = window.location.pathname.split("/")[1];

    var links = $('a');
    i = 0;
    while(i<links.length)
    {
        $(links[i]).removeClass("active-1");
        i++;
    }

    if(path=="especies"){
        $("#especie").addClass("active-1");
    }else
    if(path=="generos"){
        $("#genero").addClass("active-1");
    }else
    if(path=="familias"){
        $("#familia").addClass("active-1");
    }else
    if(path=="ordems"){
        $("#ordem").addClass("active-1");
    }else
    if(path=="classes"){
        $("#classe").addClass("active-1");
    }else
    if(path=="filos"){
        $("#filo").addClass("active-1");
    }else
    if(path=="reinos"){
        $("#reino").addClass("active-1");
    }else
    if(path=="utilizadores"){
        $("#utilizadores").addClass("active-1");
    }else
    if(path=="" || path=="home"){
        $("#home").addClass("active-1");
    }

}