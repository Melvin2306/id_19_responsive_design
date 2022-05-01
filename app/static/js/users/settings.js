const delete_button_account = document.getElementById("delete_user");

delete_button_account.addEventListener("click", (e) => {
    e.preventDefault()
    if (confirm("Are you sure that you want to delete your account?\nPress OK to continue or Cancel to cancel")) {
        document.getElementById('hidden_delete').click();
    }
});