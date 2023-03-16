import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        int num = sc.nextInt();

        for(int i=2;i<num+1;i++) {
            if(num==1) break;
            if(num%i==0) {
                num/=i;
                list.add(i);
                i--;
            }
        }

        Collections.sort(list);

        for(int item : list) System.out.println(item);
    }
}
