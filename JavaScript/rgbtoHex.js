function rgb(r, g, b){
 return convertRGB(r) + convertRGB(g) + convertRGB(b);
}


function convertRGB(number){
    if(number <= 0){
        return "00";
    }
    else if(number >= 255){
        return "FF";
    }
    let firstHex = parseInt(number / 16)
    let secondHex = ((number / 16) - firstHex) * 16
    return toHexVal(firstHex) + toHexVal(secondHex)
}

const toHexVal = (number) =>{
    const rgbValToHex = {
    '0': '0',  
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F',
    }

    return rgbValToHex[number.toString()]
}




function main(){
    console.log(rgb(0, 0, -20));
    console.log(rgb(0, 0, 0));
    console.log(rgb(173,255,47));
    console.log(rgb(300,255,255));
}

main();