export function parseMolecule(formula:string): Record<string,number> {
    let toAtoms : Record<string, number> = {};
    //Edge case if the formula has nothing (in this case an invalid formula or an empty string)
    if(formula === null){
        return {};
    }
    //Base Case if (string DOES NOT contain [] and does not contain ())
    if((!formula.includes("(") && !formula.includes(")")) && (!formula.includes("[") && !formula.includes("]"))){
        //Check if number does not exist in the formula
        if(/\d/.test(formula) == false){
            for(let i = 0; i < formula.length; i++){
                
            }
        }
    }
    
    for(let i = 0; i < formula.length; i++){
        let tracker = 0;
        
        let charVal = formula.charAt(i);
        let strVal = " ";
        strVal = charVal.valueOf();
        //If an capital A-Z letter occurs
        if(strVal.match("[A-Z]")){

            tracker++;
        }
    }
    
    return {};
}
  