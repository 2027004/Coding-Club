let mySubmit;
let myName;
nameSub = document.getElementById("nameSub");
biogSub = document.getElementById("biogSub");
form1 = document.getElementById("form1");
form2 = document.getElementById("form2");
dropdown1 = document.getElementById("dropdown1");
write = document.getElementById("write");
    write.style.display="none";
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

function closeColor(){
    dropdown1.style.display = "none";
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

function nameCloser(){
    write.style.display= "none";
}