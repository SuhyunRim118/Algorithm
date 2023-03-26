import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int begin = sc.nextInt();
        int end = sc.nextInt();
        int count = 1;
        int check = 0;
        int index = 1;
        int total = 0;

        while(index-1!=end) {
            if(check!=count) {
                check++;
            }
            else {
                check = 1;
                count++;
            }

            if(begin<=index && index<=end) {
                total += count;
            }
            index++;
        }

        System.out.println(total);
    }
}
