async function check_server() {
    const resp = await fetch('/server-status')
    if (resp.status != 200) {
        swal( "Oops","NGINX not found. Please install and refresh this page" ,"error" )
    }
    else if (resp.status == 200) {
        await list_folders()
        await list_folders_modal()
    }
}
async function list_folders_modal() {
    const resp = await fetch('config/list/folder')
    if (resp.status == 200) {
        var jsonResponse = await resp.json()
        for (var i = 0; i < jsonResponse.folders.length; i++) {
            var sel = document.getElementById("select-folder-modal")
            var op = document.createElement("option")
            op.value, op.text = jsonResponse.folders[i]
            sel.appendChild(op)
        }
    }
}
async function list_folders() {
    const resp = await fetch('config/list/folder')
    if (resp.status == 200) {
        var jsonResponse = await resp.json()
        for (var i = 0; i < jsonResponse.folders.length; i++) {
            var sel = document.getElementById("select-folder")
            var op = document.createElement("option")
            op.value, op.text = jsonResponse.folders[i]
            sel.appendChild(op)
        }
    }
}
async function folder_files() {
    var selfolder = document.getElementById("select-folder")
    var foldername = selfolder.value;
    var selfile = document.getElementById("select-file")
    selfile.options.length=1
    var resp
    if(foldername=="/")
    {
        resp = await fetch('config/list/file')
    }
    else{
        resp = await fetch('config/list/file?folder_name='+foldername)
    }
    if (resp.status == 200) {
        var jsonResponse = await resp.json()
        for (var i = 0; i < jsonResponse.files.length; i++) {
            var op = document.createElement("option")
            op.value, op.text = jsonResponse.files[i]
            selfile.appendChild(op)
        }
    }
}
async function get_file() {
    var sel = document.getElementById("select-file")
    var filename = sel.value;
    var selectfolder = document.getElementById("select-folder")
    var folder_name = selectfolder.value
    let url = "/config/i/" + filename
    if(folder_name !="/")
    {
        url = "/config/i/" + filename+"?folder_name="+folder_name
    }
    const resp = await fetch(url)
    if (resp.status == 200) {
        var editor = document.getElementById("editor")
        editor.value = await resp.text()
    }
}
async function file_save() {
    var sel = document.getElementById("select-file")
    var filename = sel.value;
    var selectfolder = document.getElementById("select-folder")
    var folder_name = selectfolder.value
    let url = "/config/i/" + filename
    if(folder_name !="/")
    {
        url = "/config/i/" + filename+"?folder_name="+folder_name
    }
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
        swal("Success","Your file has been saved", "success")
    }
    else {
    swal ( "Oops" ,  "Something went wrong!" ,  "error" )
    }
}
async function test_conf() {
    const resp = await fetch('/config/test')
    if (resp.status == 200) {
        var msg = await resp.json()
        swal("",msg.msg,"info")
    }
}
async function create_config()
{
    var selectfolder = document.getElementById("select-folder-modal")
    var folder_name = selectfolder.value
    var new_file = document.getElementById("file_input").value
    var file_content = {}
    file_content["content"] = editor.value.split("\n")
    let url ="/config/i/" + new_file
    if(folder_name !="/")
    {
        url = "/config/i/" + new_file+"?folder_name="+folder_name
    }
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(file_content)
    })
    if (response.status == 200) {
        swal("Success","Your file has been saved", "success")
    }
    else {
    swal ( "Oops" ,  "Something went wrong!" ,  "error" )
    }
}


