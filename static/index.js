async function check_server() {
    const resp = await fetch('/server-status')
    if (resp.status != 200) {
        alert("Nginx not found! Install & restart the UI.")
    }
    else if (resp.status == 200) {
        await list_files()
    }
}
async function list_files() {
    const resp = await fetch('/config/list')
    if (resp.status == 200) {
        var jsonResponse = await resp.json()
        for (var i = 0; i < jsonResponse.files.length; i++) {
            var sel = document.getElementById("select-file")
            var op = document.createElement("option")
            op.value, op.text = jsonResponse.files[i]
            sel.appendChild(op)
        }
    }
}
async function get_file() {
    var sel = document.getElementById("select-file")
    var filename = sel.value;
    let url = "/config/i/" + filename
    const resp = await fetch(url)
    if (resp.status == 200) {
        var editor = document.getElementById("editor")
        editor.textContent = await resp.text()
    }
}
async function file_save() {
    var sel = document.getElementById("select-file")
    var filename = sel.value;
    let url = "/config/i/" + filename
    var editor = document.getElementById("editor")
    var file_content = {}
    file_content["content"] = editor.value.split("\n")
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(file_content)
    })
    if (response.status == 200) {
        alert("file saved")
    };
}
async function test_conf() {
    const resp = await fetch('/config/test')
    if (resp.status == 200) {
        var msg = await resp.json()
        alert(msg.msg)
    }
}