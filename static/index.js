function check_server() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.status != 200) {
            alert("Nginx not found! Install & restart the UI.")
            window.top.close();
        }
    };
    xhttp.open("GET", "/server-status", true);
    xhttp.send();
}