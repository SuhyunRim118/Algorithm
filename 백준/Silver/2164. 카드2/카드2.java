import java.util.*;

import javax.swing.text.html.HTMLDocument.HTMLReader.IsindexAction;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> list = new LinkedList<>();

        int number = sc.nextInt();
        int last=0;

        for(int i=0;i<number;i++) {
            list.add(i+1);
        }

        while(list.size()>1) {
            list.remove();
            list.add(list.poll());
        }

        System.out.println(list.peek());
    }
}