import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;

public class Main { 
    public static void main(String[] args) { 
        int[] num = new int[8];

        int checkA = 0;
        int checkD = 0;

        Scanner sc = new Scanner(System.in);
        for(int i=0;i<8;i++) {
            num[i] = sc.nextInt();
        }

        for(int i=0;i<8;i++) {
            if(num[i] == i+1) checkA++;
            else if(num[i] == 8-i) checkD++;
        }

        if(checkA == 8) System.out.println("ascending");
        else if(checkD == 8) System.out.println("descending");
        else System.out.println("mixed");
    } 
}
