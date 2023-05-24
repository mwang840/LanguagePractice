export function duplicateCount(text: string): number{
    let counter = 0;
    let recordOfDuplicates: Record<string, number> = {};
    const allText = text.toLowerCase().split(" ").map(word=>{
        if(!recordOfDuplicates.hasOwnProperty(word)){
            recordOfDuplicates[word] = 0;
        }
        else{
            if(recordOfDuplicates[word] === 0){
                counter+= 1;
            }
            recordOfDuplicates[word] = recordOfDuplicates[word] + 1;
        }
    });
    
    return counter;
}