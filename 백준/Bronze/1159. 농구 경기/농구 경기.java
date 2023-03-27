import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int member;
        int[] alp = new int[26];
        String player;
        int max = -1;
        List<Character> list = new ArrayList<>();

        member = sc.nextInt();

        for(int i=0;i<member;i++) {
            player = sc.next();
            alp[player.charAt(0)-'a']++;
        }

        for(int i=0;i<26;i++) {
            if(alp[i]>=5) list.add((char)(i+'a'));
        }

        if(list.size()==0) System.out.println("PREDAJA");
        else {
            Collections.sort(list);

            for(int i=0;i<list.size();i++) {
                System.out.print(list.get(i));
            }
        }
    }
}
