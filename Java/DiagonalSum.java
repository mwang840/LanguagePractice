import java.util.List;

class DiagonalSum {
    public static int diagonalDifference(List<List<Integer>> arr) {
        // Write your code here
        int leftRightSum = 0;
        int rightLeftSum = 0;
        int size = arr.size();
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i == j) {
                    leftRightSum += arr.get(i).get(j);
                }
                if (i == size - j - 1) {
                    rightLeftSum += arr.get(i).get(j);
                }
            }
        }
        return Math.abs(leftRightSum - rightLeftSum);

    }

    public static void main(String[] args) {
        System.out.print("Hi");
    }
}