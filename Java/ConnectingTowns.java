import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;



public class ConnectingTowns {

    /*
     * Complete the 'connectingTowns' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY routes
     */

    public static int connectingTowns(int n, List<Integer> routes) {
     // Have a variable containing the results of the routes multiplied by each other   
    // Loop from 1 to n - 1 in the array list
    // From there have the modulo operator mod the 1234567
    //return that number
    int totalRoads = 1;
    for(int i = 0; i < n -1; i++){
        totalRoads = (routes.get(i) * totalRoads) % 1234567;
    }
        return totalRoads;
    }

   public static void main(String[] args) {
    List<Integer>testOne = new ArrayList<Integer>();
    testOne.add(2);
    testOne.add(2);
    testOne.add(2);
    int num = 4;
    System.out.print(connectingTowns(num, testOne));

   }

}