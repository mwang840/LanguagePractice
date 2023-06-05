// See https://aka.ms/new-console-template for more information
using System;
using System.Text;
namespace CSharp
{
    class CSharp
    {


        public static string BreakCamelCase(string str)
        {
            if (string.IsNullOrEmpty(str))
            {
                return str;
            }
            StringBuilder sb = new StringBuilder();
            foreach (var c in str)
            {
                if (char.IsUpper(c))
                    sb.Append(' ');

                sb.Append(c);
            }
            return sb.ToString();
        }

        public static string AlphabetPosition(string text)
        {
            //Add a string builder that holds the length of the text
            return String.Join(" ", text.Where(letter => char.IsLetter(letter)).Select(letter => (int)letter % 32));
        }

        //Helper factorial function
        public static int factorial(int n)
        {
            if (n == 0 || n == 1)
            {
                return 1;
            }
            else
            {
                return n * factorial(n - 1);
            }
        }

        public static int findFactorial(int n, int k)
        {
            return factorial(n) / (factorial(k) * factorial(n - k));
        }

        public static List<int> PascalsTriangle(int n)
        {
            List<int> pascal = new List<int>();
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    pascal.Add(findFactorial(i, j));
                }
            }

            return pascal;
        }

        static void Main()
        {
            Console.WriteLine(BreakCamelCase("camelCasing"));
            Console.WriteLine(AlphabetPosition("The sunset sets at twelve o' clock."));
            Console.WriteLine(AlphabetPosition("I solved this problem"));
            int pascalOne = 2;
            Console.WriteLine(string.Join(",", PascalsTriangle(pascalOne)));

        }
    }
}
