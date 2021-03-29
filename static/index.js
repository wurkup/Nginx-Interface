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
function file_save()
{
    var sel = document.getElementById("select-file")
    var filename = sel.value;
    let url = "/config/i/"+filename
    var xhttp = new XMLHttpRequest();
    var editor = document.getElementById("editor")
    var file_content = {}
    file_content["content"] = editor.value.split("\n")   
    xhttp.onreadystatechange = function () {
        if (this.status == 200) {
            alert("file saved")
        }
    };
    xhttp.open("PUT", url, true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify(file_content));
}
function test_conf()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        var msg = JSON.parse(this.responseText)
        alert(msg.msg)
    };
    xhttp.open("GET", "config/test", true);
    xhttp.send();
}