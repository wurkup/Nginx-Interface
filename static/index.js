function check_server() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.status != 200) {
            alert("Nginx not found! Install & restart the UI.")
            list_files()
        }
    };
    xhttp.open("GET", "/server-status", true);
    xhttp.send();
}
function list_files()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.status == 200) {
            var jsonResponse = JSON.parse(this.responseText);
            for(var i=0;i<jsonResponse.files.length;i++)
            {
                var sel = document.getElementById("select-file")
                var op = document.createElement("option")
                op.value,op.text=jsonResponse.files[i]
                sel.appendChild(op)
            }
        }
    };
    xhttp.open("GET", "/config/list", true);
    xhttp.send();
}
function get_file()
{
    var sel = document.getElementById("select-file")
    var filename = sel.value;
    let url = "/config/i/"+filename
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.status == 200) {
            var editor = document.getElementById("editor")
            editor.textContent = this.responseText
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}