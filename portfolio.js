let mySubmit;
let myName;

biog = document.getElementById("biog");
user = document.getElementById("user");

nameSub = document.getElementById("nameSub");
biogSub = document.getElementById("biogSub");
form1 = document.getElementById("form1");
form2 = document.getElementById("form2");
bgColor = document.getElementById("bgColor");

write = document.getElementById("write");
    write.style.display="none";
colors = document.getElementById("colors")
    colors.style.display="none";
nameClose = document.getElementById("nameClose");

nameSub.onclick = function(){
    myName = document.getElementById("nameText").value;
    document.getElementById("user").textContent = `${myName}'s Portfolio`;
}

biogSub.onclick = function(){
    myBio = document.getElementById("bio").value;
    document.getElementById("biog").textContent = myBio;
}

function changeColor(color){
    document.body.style.backgroundColor = color;
}
function changeNameColor(textColor){
    window.user.style.color = textColor;
}
function changeBiogColor(textColor){
    window.biog.style.color = textColor;
}


function showMenu(){
    menuArrow = document.getElementById("menuArrow");
    menu = document.getElementById("menu");
    menuLoadOut = document.getElementById("menuLoadOut");
    if(getComputedStyle(menu).top == "0px"){
        menu.style.top = "200px";
        menuLoadOut.style.display = "block";
        menuArrow.textContent = "/\\"
    }
    else if(getComputedStyle(menu).top == "200px"){
        menu.style.top = "0px";
        menuLoadOut.style.display = "none";
        menuArrow.textContent = "\\/"
    }
}

function writePop(){
    write.style.display = "block";
}
function colorsPop(){
    colors.style.display = "block";
}



function nameCloser(){
    write.style.display= "none";
}

function colorCloser(){
    colors.style.display = "none";
}


//Make the DIV element draggagle:
dragElement(document.getElementById("write"));

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById("headbar")) {
    /* if present, the header is where you move the DIV from:*/
    document.getElementById("headbar").onmousedown = dragMouseDown;
  } else {
    /* otherwise, move the DIV from anywhere inside the DIV:*/
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
