import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer[] scores = new Integer[8];
        int[] sort = new int[8];
        int[] index = new int[5];
        int total = 0;
        
        for(int i=0;i<8;i++) {
            scores[i] = sc.nextInt();
            sort[i] = scores[i];
        }

        Arrays.sort(sort);

        for(int i=7;i>2;i--) {
            total += sort[i];
            index[7-i] = Arrays.asList(scores).indexOf(sort[i]);
        }

        Arrays.sort(index);

        System.out.println(total);
        for(int item : index) System.out.print(item+1 + " ");
    }
}
