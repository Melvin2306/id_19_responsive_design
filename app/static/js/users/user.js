// DELETE CONFIRMATION
const delete_button_user = document.getElementById("delete_user");

delete_button_user.addEventListener("click", (e) => {
    e.preventDefault()
    if (confirm("Are you sure that you want to delete your account?\nPress OK to continue or Cancel to cancel")) {
        window.location.replace(window.location.href + "/deleteuser");
    }
});

const delete_button_company = document.getElementById("delete_company");

delete_button_company.addEventListener("click", (e) => {
    e.preventDefault()
    if (confirm("Are you sure that you want to delete this account?\nPress OK to continue or Cancel to cancel")) {
        window.location.replace(window.location.href + "/deleteuser");
    }
});

