function decodeMorse(morseCode){
    const MORSE_CODE = {"·−": "A",
         "-...": "B", 
         "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V",
    ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"
    }
    morseCode = morseCode.trim()
    const morseArr = morseCode.split("   ");
    let result = "";
    for(let k = 0; k < morseArr.length; k++){
        let wordResult = "";
        const letter = morseArr[k].split(" ")
        for (let i = 0; i < letter.length; i++) {
            wordResult += MORSE_CODE[letter[i]];
        }
        result += wordResult;

        if (k < morseArr.length - 1) {
            result += " "; // add space between words
        }
    }
    return result
}

function main(){
    const example = "···· · −·−−   ·−−− ··− −·· ·";
    console.log(decodeMorse(example))
}

main()