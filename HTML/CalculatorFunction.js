
const display = document.getElementById("display")
const tester = ["", "", ""];




function appendToDisplay(input)
{
    if(display.value =="Cannot Compute.")
    {
        display.value = null;
    }
    display.value += input;
}

function clearDisplay()
{
    display.value = null;
}

function calculate()
{
    try{
        display.value = eval(display.value);
    }
    catch(error)
    {
        display.value = "Cannot Compute.";
    }
    
    
}
