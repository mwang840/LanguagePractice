import java.util.ArrayList;
// import java.util.Arrays;
import java.util.Collections;

public class SpeedControl {
    public static int gps(int s, double[] x) {
        if (x.length <= 1) {
            return 0;
        }
        ArrayList<Double> allSpeeds = new ArrayList<Double>(x.length + 1);
        // double[] listOfSpeeds = new double[x.length];
        for (int i = 0; i < x.length - 1; i++) {
            allSpeeds.add((3600 * (x[i + 1] - x[i])) / s);
            // listOfSpeeds[i] = (3600 * (x[i] + x[i - 1])) / s;
        }
        // your code
        double maximumSpeed = Collections.max(allSpeeds);
        return (int) (maximumSpeed);
        // double maxSpeed = (Arrays.stream(listOfSpeeds).max().getAsDouble());
        // return (int) (maxSpeed);
    }

    public static void main(String[] args) {
        double[] exampleSpeeds = { 0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25 };
        int exampleSpeed = 15;
        System.out.println(gps(exampleSpeed, exampleSpeeds));
        double[] exampleSpeeds2 = { 0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61 };
        int exampleSpeed2 = 41;
        System.out.println(gps(exampleSpeed2, exampleSpeeds2));
    }
}