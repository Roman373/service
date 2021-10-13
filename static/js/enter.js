function btn() {
    var inputLogin = document.getElementById("myLogin").value;
    var inputPassword = document.getElementById("myPassword").value;
    if (inputLogin === '' || inputPassword === "") {
        document.getElementById('nullExit').innerHTML="Вы должны что-то написать!";
    }
    else {
        window.location.href='index.html';
    }
}