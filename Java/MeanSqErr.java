import java.util.ArrayList;

public class MeanSqErr{
    public static double solution(int[] arr1, int[] arr2) {
        //Initialize a sun first
        double sum = 0;
        //store it in a list (array list)
        ArrayList<Double> sums = new ArrayList<>();
        for(int i = 0; i < arr1.length; i++){
            sum = Math.pow(Math.abs((arr1[i] - arr2[i])), 2);
            sums.add(sum);
        }
        double totalVal = 0;
        double average = 0;
        for(Double i: sums){
            totalVal += (double)i;
        }
        average = totalVal / arr1.length;
        return average;
    }

    public static void main(String[] args) {
        int[] a1 = {1, 2, 3};
        int[] a2 = {4, 5, 6};
        int[] b1 = {10, 20, 10, 2};
        int[] b2 = {10, 25, 5, -2};
        int[] c1 = {0, -1};
        int[] c2 = {-1, 0};
        System.out.println(solution(a1, a2));
        System.out.println(solution(b1, b2));
        System.out.println(solution(c1, c2));
    }
}
