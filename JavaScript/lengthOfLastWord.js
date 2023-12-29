var lengthOfLastWord = function(s) {
    const val = s.trim()
    const toStrArray = val.split(" ");
    if(toStrArray.length === 0){
        return 0;
    }
    return toStrArray[toStrArray.length - 1].length;
};

function main(){
    console.log(lengthOfLastWord("   fly me   to   the moon  "));
}

main()