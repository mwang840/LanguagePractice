// See https://aka.ms/new-console-template for more information
using System;
using System.Text;
namespace CSharp{
    class CSharp{
    static void Main(){
        Console.WriteLine(BreakCamelCase("camelCasing"));
        Console.WriteLine(AlphabetPosition("The sunset sets at twelve o' clock."));
        Console.WriteLine(AlphabetPosition("I solved this problem"));
    }

    public static string BreakCamelCase(string str){
        if (string.IsNullOrEmpty(str)){
            return str;
        }
        StringBuilder sb = new StringBuilder();
        foreach (var c in str) {
        if (char.IsUpper(c))    
        sb.Append(' ');
        
        sb.Append(c);
        }
        return sb.ToString();
    }

    public static string AlphabetPosition(string text)
    {
        //Add a string builder that holds the length of the text
        return String.Join(" ", text.Where(letter=>char.IsLetter(letter)).Select(letter=>(int)letter % 32));
    }
}
}
