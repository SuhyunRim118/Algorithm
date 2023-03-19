import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        int number;

        for(int i=0;i<10;i++){
            number = sc.nextInt();
            if(i==0) list.add(number%42);
            else {
                if(!list.contains(number%42)) list.add(number%42);
            }
        }

        System.out.println(list.size());
    }
}
