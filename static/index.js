async function check_server() {
    const resp = await fetch('/server-status')
    var finalres = await resp
    if (finalres.status != 200) {
        alert("Nginx not found! Install & restart the UI.")
    }
    else if (finalres.status == 200) {
        await list_files()
    }
}
async function list_files() {
    const resp = await fetch('/config/list')
    var finalres = await resp
    if (finalres.status == 200) {
        var jsonResponse = await resp.json()
        for (var i = 0; i < jsonResponse.files.length; i++) {
            var sel = document.getElementById("select-file")
            var op = document.createElement("option")
            op.value, op.text = jsonResponse.files[i]
            sel.appendChild(op)
        }
    }
}
function get_file() {
    var sel = document.getElementById("select-file")
    var filename = sel.value;
    let url = "/config/i/" + filename
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
function file_save() {
    var sel = document.getElementById("select-file")
    var filename = sel.value;
    let url = "/config/i/" + filename
    var xhttp = new XMLHttpRequest();
    var editor = document.getElementById("editor")
    var file_content = {}
    file_content["content"] = editor.value.split("\n")
    xhttp.open("PUT", url, true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify(file_content));
    xhttp.onreadystatechange = function () {
        if (this.status == 200) {
            alert("file saved")
        }
    };
}
async function test_conf() {
    const resp = await fetch('/config/test')
    var finalres = await resp
    if(finalres.status ==200)
    {
        var msg = await finalres.json()
        alert(msg.msg)
    }
}