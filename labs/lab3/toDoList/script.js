let addBtn = document.getElementById("addBtnid");
let inputBox = document.getElementById("inputBox");
let listContainer = document.getElementById("listContainer");

function addTask() {
    if(inputBox.value === '' || inputBox.value === null) {
        alert("You must write something!");
    }
    else {
        let newTask = document.createElement('div');
        newTask.innerHTML = '<div class = "listElement"><input type = "checkbox"><label for="task1">' + inputBox.value + '</label><span>&times;</span></div>';
        listContainer.appendChild(newTask);
        inputBox.value = "";
    }
}




listContainer.addEventListener("click", function(elem){
    let checkbox = elem.target.querySelector('input[type="checkbox"]');
    if (elem.target.tagName === "SPAN") {
        elem.target.parentElement.remove();
    }
    else if (elem.target.tagName === "DIV") {
        if (elem.target.classList.contains("listElementChecked")) {
            elem.target.classList.remove("listElementChecked");
            elem.target.classList.add("listElement");
            checkbox.checked = false;
        }
        else {
            elem.target.classList.toggle("listElementChecked");
            checkbox.checked = true;
        }
    }
    else if (elem.target.tagName === "INPUT") {
        let parentElement = elem.target.parentElement;
        if (elem.target.checked == true || parentElement.classList.contains("listElement")) {
            parentElement.classList.toggle("listElementChecked");
        }
        else if (elem.target.checked == false || parentElement.classList.contains("listElementChecked")) {
            parentElement.classList.remove("listElementChecked");
            parentElement.classList.toggle("listElement");
        }
    }
    else if (elem.target.tagName === "LABEL") {
        let parentElement = elem.target.parentElement;
        if (parentElement.classList.contains("listElement")) {
            parentElement.classList.toggle("listElementChecked");
        }
        else if (parentElement.classList.contains("listElementChecked")) {
            parentElement.classList.remove("listElementChecked");
            parentElement.classList.toggle("listElement");
        }
    }
}, false);
