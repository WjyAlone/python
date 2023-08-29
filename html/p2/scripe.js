function addBtn(){
    var list = document.getElementById("list");
    var eleNew = "<li><select><option value='room'>房间</option><option value='toilet'>厕所</option><option value='outter'>阳台</option></select><input type='text'></li>"
    list.insertAdjacentHTML("beforeend", eleNew)
}