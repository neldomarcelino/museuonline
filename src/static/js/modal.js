/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function window_modal_add()
{
    document.getElementById("modal-head").style.display = 'block';
    document.getElementById("modal-content-regiter").style.display = 'block';
    document.getElementById("modal-content-edit").style.display = 'none';

}
function window_modal_delete(id)
{
    document.getElementById("modal-head").style.display = 'block';
    document.getElementById("modal-delete").style.display = 'block';
    document.getElementById("modal-content-regiter").style.display = 'none';
    document.getElementById("modal-content-edit").style.display = 'none';



}
function window_modal_edit(id, data)
{
    document.getElementById("modal-head").style.display = 'block';
    document.getElementById("modal-content-regiter").style.display = 'none';
    document.getElementById("modal-content-edit").style.display = 'block';
    insert_data_in_form(id, data);
}

function window_modal_cadastro()
{
    document.getElementById("modal-head-sign").style.display = 'block';
    document.getElementById("modal-content-login").style.display = 'none';
    document.getElementById("modal-content-cadastro").style.display = 'block';
}
function window_modal_login()
{
    document.getElementById("modal-head-sign").style.display = 'block';
    document.getElementById("modal-content-login").style.display = 'block';
    document.getElementById("modal-content-cadastro").style.display = 'none';

}
function cancelar_sign()
{
    document.getElementById("modal-head").style.display = 'none';
    document.getElementById("modal-head-sign").style.display = 'none';
    document.getElementById("modal-content-login").style.display = 'none';
    document.getElementById("modal-content-cadastro").style.display = 'none';
}



function insert_data_in_form(id, data)
{
    $("#text-input-1").val(data);
    var action = document.getElementById("form-1").action+""+id;
    document.getElementById("form-1").action = action;

}
function cancelar()
{
    document.getElementById("modal-head").style.display = 'none';
    document.getElementById("modal-content-regiter").style.display = 'none';
    document.getElementById("modal-content-edit").style.display = 'none';
}


var timer;
var _id=0;
var cont=0;
var _delete = false;
function deleta(id){
    _delete = false;
    cont++;
    $("#cancel-js").css("display","block"); //Mostra o botao de cancelar
    $("#"+id).css("display","none"); //Ocultar o registor do delete.
    if(cont>1 && _id!=-1){
        _delete = true;
        _id = delete_data();
    }

    _id = id;
    timer = setInterval(delete_data, 5000); //programa o botao de cancelar para fechar
}
function delete_data()
{
    clearInterval(timer);
    if(!_delete)
        $("#cancel-js").css("display","none") //fecha o botao de cancelar o delete do registo
    document.getElementById("apagar"+_id).removeAttribute("onclick");
    //document.getElementById("apagar"+_id).click();
    eliminar_db();
    return -1
}
function cancel_deleta(){
    $("#"+_id).css("display","block"); //Mostra o registo deletado
    $("#cancel-js").css("display","none"); // Oculta o botao cancel
    _id = 0;
    clearInterval(timer);

}
function eliminar_db() {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            _delete = false;
        }
    };
    _url = "delete/"+_id;
    xhttp.open("POST", _url, true);
    xhttp.send();
}
























function adicionar(){
    document.getElementById("my_div_js").style.display = 'none';
    document.getElementById("my_div_js2").style.display = 'block';
    
}
function sucess(){
    document.getElementById("form_1").submit();
    if(document.getElementById("my_div_js2")!=null)
        document.getElementById("my_div_js2").style.display = 'none';
}

function removerLinha_1() {
    var t = document.getElementById(_tr);                                      
    document.getElementById(_tb).removeChild(t);
    eliminar_db();
    adicionar();
    
}






function erro_eliminar(){
    document.getElementById("my_div_js").style.display = 'none';
    document.getElementById("my_div_js3").style.display = 'block';
}

function verficar_menu(){
    
    var ul=null;
    var distr = document.getElementById("insert_js");
    var v=true;
    var i =0;
    if(document.getElementById("menu_script")!=null){
        ul = document.getElementById("menu_script");
        verficar1 = true;
    }else if(window.top.document.getElementById("menu_script")!=null){
        verficar1 = true;
        ul = window.top.document.getElementById("menu_script");
    }
    if(ul!=null){
        
        if (ul.getElementsByTagName("li").length > 0) {
            for (i = ul.childNodes.length - 1; i > 0; i--) {

                if (ul.childNodes[i].id == distr.value) {
                    //alert(distr.value);
                    erro_eliminar();
                    v = false;
                }
            }
        }
        
        if(v){
            adicionar();
        }
    }
}



var distrito="distrito9";
var cont=0;
var source1 = new EventSource("");
source1.onmessage = function(event){
    var dis = event.data;
    var verfica = false;
    if(dis != distrito || _delete){
        cont++;
        if(document.getElementById("menu_script")!=null){
            distrito = document.getElementById("menu_script");
            verfica = true;
        }else if(window.top.document.getElementById("menu_script")!=null){
            verfica = true;
            distrito = window.top.document.getElementById("menu_script");
        }
        if(verfica){
            if(document.getElementById(_id)!=null){
                distrito.removeChild(document.getElementById(_id));
            }
            else if(window.top.document.getElementById(_id)!=null){
                distrito.removeChild(window.top.document.getElementById(_id));
            }
        }
        
        distrito = dis;
        
    }
};
function pesquisaMenu(){
    var xmhttp = new XMLHttpRequest();
    xmhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            mymenu(this);
        }
    };
    var url_path = "PesquisaDestrito";
    xmhttp.open("POST", url_path, true);
    xmhttp.send();
};



function mymenu(xml){
    var xmlDoc = xml.responseXML;
    var row;
    var t = xmlDoc.getElementsByTagName("distrito");
    for(i=0; i<t.length; i++){
        if(document.getElementById("menu_script")!=null)
            row = document.getElementById("menu_script").insertRow();
        else if(document.top.getElementById("menu_script")!=null)
            row = document.top.getElementById("menu_script");
        
         if (row.getElementsByTagName("li").length > 0) {
            for (loop = row.childNodes.length - 1; loop > 0; loop--) {
                row.removeChild(row.childNodes[loop]);
            }
        }
    }
}