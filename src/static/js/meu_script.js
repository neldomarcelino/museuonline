/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 * */
function menu_destacar__(link, list){
                
    var tag_ul = document.getElementsByClassName(list);
    for(j=0;j<tag_ul.length;j++)
    {
        var tag_li = tag_ul[j].getElementsByTagName("li");
        for(i=0;i<tag_li.length;i++)
        {
            tag_li[i].style.backgroundColor = "";
            tag_li[i].style.borderRadius = "";
            tag_li[i].style.boxShadow = "";
            tag_li[i].style.color="";
            tag_li[i].getElementsByTagName("a")[0].style.color="";
        } 
        document.getElementById(link).style.color="#0099ff";
        document.getElementById(link).style.backgroundColor="#ffffff";
        document.getElementById(link).style.borderRadius="4px";
        document.getElementById(link).style.boxShadow="0px 0px 2px #0099ff";
        document.getElementById(link).getElementsByTagName("a")[0].style.color="#0099ff";
        
        window_url(link);

    }
}
function window_url(link){
    var path = "http://localhost:"+window.location.port+window.location.pathname+"#".concat(document.getElementById(link).innerText);
    window.location.href = path;
}
function window_frame(){
                
    var frame = window.frames.location.href.split('/');
    var final;
    for (i=0;i<frame.length;i++){
        final = frame[i];
    }
    var value = final.split('.');
    final = value[0];
    
    var path = "http://localhost:"+window.top.location.port+window.top.location.pathname+"#".concat(final);
    window.top.location.href= path;


}
function modify_db_insert(id){
    if (!confirm("Sera Inserido Um Novo Registo Na Base De Dados")){
        document.getElementById(id).setAttribute("type", "reset"); 
    }else{
        document.getElementById(id).setAttribute("type", "submit");
    }
}
function alterar_especie(){
    button_save = document.getElementById("ul-edit");
    button_save.removeAttribute("hidden");

}
function hide_especie(){
    button_save = document.getElementById("ul-edit");
    button_save.setAttribute("hidden","");
}

//Busca ajax
function clearTable() {
    var t = document.getElementById("tb_data");
    if (t.getElementsByTagName("tr").length > 0) {
        for (loop = t.childNodes.length - 1; loop >= 0; loop--) {
            t.removeChild(t.childNodes[loop]);
        }
    }
}

function pesquisa_especie() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        clearTable();
        if (this.readyState == 4 && this.status == 200) {
            myFunction(this);
        }
    };
    var url = "pesquisa/"+$("#pesquisa").val();
    xhttp.open("POST", url, true);
    xhttp.send();
    if($("#pesquisa").val().length<=0){
        $("#idDivBusca").css("display","none");
    }else{
        $("#idDivBusca").css("display","block");
    }
}

function pesquisa_utilizador() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        clearTable();
        if (this.readyState == 4 && this.status == 200) {
            myFunctionUtilizador(this);
        }
    };
    if ($("#pesquisa").val().length <= 0){
        var url = "pesquisa/-*.M21#digio!@#"
    }else{
        var url = "pesquisa/"+$("#pesquisa").val();
    }
    xhttp.open("POST", url, true);
    xhttp.send();

}

function myFunctionUtilizador(xml) {

    parser = new DOMParser();
    xmlDoc = parser.parseFromString(xml.responseText, "text/xml");
    var x = xmlDoc.getElementsByTagName("c_utilizador");

    for (i = 0; i < x.length; i++) {

        var row = document.getElementById("tb_data").insertRow();

        c = row.insertCell();
        c.innerHTML = x[i].getElementsByTagName("email")[0].childNodes[0].nodeValue;

        c = row.insertCell();
        c.innerHTML = '<input type="password" value="'+x[i].getElementsByTagName("password")[0].childNodes[0].nodeValue+'" disabled>';

        c = row.insertCell();
        c.innerHTML = x[i].getElementsByTagName("idtipo")[0].childNodes[0].nodeValue;

        var idespecie = x[i].getElementsByTagName("idutilizador")[0].childNodes[0].nodeValue;
        c = row.insertCell();

        c.innerHTML = '<a class="link_a_1" href="especie/completa/'+idespecie+'">'+
        'Editar </a>';

        c = row.insertCell();

        c.innerHTML = '<a class="link_a_1" href="especie/completa/'+idespecie+'">'+
        'Eliminar </a>';

    }
}
function myFunction(xml) {

    parser = new DOMParser();
    xmlDoc = parser.parseFromString(xml.responseText, "text/xml");
    var x = xmlDoc.getElementsByTagName("c_especie");

    for (i = 0; i < x.length; i++) {

        var row = document.getElementById("tb_data").insertRow();
        row.setAttribute("class", "tr-0");

        c = row.insertCell();
        c.innerHTML = x[i].getElementsByTagName("especie")[0].childNodes[0].nodeValue;
        c.setAttribute("class", "neldo_td_0");

        c = row.insertCell();
        c.innerHTML = x[i].getElementsByTagName("nomecomum")[0].childNodes[0].nodeValue;
        c.setAttribute("class", "neldo_td_0");

        c = row.insertCell();
        c.innerHTML = x[i].getElementsByTagName("habitat")[0].childNodes[0].nodeValue;
        c.setAttribute("class", "neldo_td_0");

        var idespecie = x[i].getElementsByTagName("idespecie")[0].childNodes[0].nodeValue;
        c = row.insertCell();

        c.innerHTML = '<a class="link_a_1" href="especie/completa/'+idespecie+'">'+
        'Ver mais </a>';
        c.setAttribute("class", "neldo_td_0");

    }
}


function div_show(id){
    $("#vid").addClass("mult-none");
    $("#video").removeClass("active");

    $("#som").addClass("mult-none");
    $("#audio").removeClass("active");

    $("#image").addClass("mult-none");
    $("#imagem").removeClass("active");

    $("#"+id).removeClass("mult-none");

    if(id=="image")
        $("#imagem").addClass("active");
    else if(id=="som")
        $("#audio").addClass("active");
    else if(id=="vid")
        $("#video").addClass("active");

}

