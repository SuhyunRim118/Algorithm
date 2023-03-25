import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int plugNum;
        int num;
        int total = 0;

        plugNum = sc.nextInt();

        for(int i=0;i<plugNum;i++) {
            num = sc.nextInt();

            if(i != plugNum-1) total += num - 1;
            else total += num;
        }
        System.out.println(total);
    }
}