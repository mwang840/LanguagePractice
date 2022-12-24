// See https://aka.ms/new-console-template for more information
using System;
using System.Text;
namespace CSharp{
    class CSharp{
    static void Main(){
        Console.WriteLine(BreakCamelCase("camelCasing"));
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
}
}
