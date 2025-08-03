function duplicateCount(text){
    const lower = text.toLowerCase()
    const textMap = {}
    const resultCt = 0

    for(let lo in lower){
        if(textMap[lo]){
            textMap[lo]++
        }
        else{
            textMap[lo] = 1
        }
    }

    for (let char in textMap) {
    if (textMap[char] > 1) {
      resultCt++;
    }
  }
  return resultCt
}