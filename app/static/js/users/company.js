const delete_button_company = document.getElementById("delete_company");

delete_button_company.addEventListener("click", (e) => {
    e.preventDefault()
    if (confirm("Are you sure that you want to delete this company?\nPress OK to continue or Cancel to cancel")) {
        window.location.replace(window.location.href + "/deletecompany");
    }
});