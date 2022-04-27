let passwordInput = document.querySelector('input[type="password"]');

let showHide = document.querySelector('#showHide');
showHide.onclick = function(){showHidePassword()}
function showHidePassword(){
    if(passwordInput.type == "password"){
        passwordInput.type = "text";
        showHide.textContent = "HIDE";
        showHide.style.color = "green";
    }
    else{
    passwordInput.type = "password";
    showHide.textContent = "SHOW";
    showHide.style.color = "red";
    }
}