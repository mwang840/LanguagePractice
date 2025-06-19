export class Kata {
  word: string;

  constructor(word: string){
    this.word = word;
  }

  static disemvowel(str: string): string {
    const vowelsArray = ["a", "e", "o","i","u", "A", "E", "I", "O", "U"];
    const words = str.split("");
    return words.filter((word: string): boolean=> (word !== vowelsArray[0] && word !==vowelsArray[1] && word !== vowelsArray[2] && word !==vowelsArray[3] && word !==vowelsArray[4] && word !==vowelsArray[5] && word !==vowelsArray[6] && word !==vowelsArray[7] && word !==vowelsArray[8] && word !==vowelsArray[9])).join("");
  }
  
}

function main(){
    const example = new Kata("example");
  }