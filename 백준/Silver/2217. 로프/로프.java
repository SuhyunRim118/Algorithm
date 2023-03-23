import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int[] ropes = new int[number];
        int min=0;

        for(int i=0;i<number;i++) {
            ropes[i] = sc.nextInt();
        }
        
        Arrays.sort(ropes);

        int max = ropes[number-1];

        for (int i = 0; i < number; i++) {
            max = Math.max(max, ropes[i] * (number - i));
        }

        System.out.println(max);
    }
}