function login(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            if (this.responseText=="false"){
                $("#email").addClass("form-input-error");
                $("#password").addClass("form-input-error");
            }else
            {
                $("#button_submit").removeAttr("onclick");
                $("#button_submit").click();
            }
        }
    };
    var url = "../utilizadores/login";
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("email="+$("#email").val()+"&password="+$("#password").val());

}
$("#email").click(function(){
    $(this).removeClass("form-input-error");
    $("#password").removeClass("form-input-error");
});
$("#password").click(function(){
    $(this).removeClass("form-input-error");
    $("#email").removeClass("form-input-error");
});
$("#pass_sub_cads").click(function(){
    if($("#password_2").val()!=$("#password_conf").val()){
        $("#password_conf").text = "";
    }
});
