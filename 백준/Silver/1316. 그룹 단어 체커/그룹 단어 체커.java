import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Character> list = new ArrayList<>();

        int testcase = sc.nextInt();
        String word;
        int check = 0;
        int totalGroup = 0;
        int previousIndex = 0;;

        for(int i=0;i<testcase;i++) {
            word = sc.next();
            for(int j=0;j<word.length();j++) {
                if(!list.contains(word.charAt(j))) {
                    list.add(word.charAt(j));
                    previousIndex = j;
                    check++;
                }
                else {
                    if(word.charAt(previousIndex)!=word.charAt(j)) break;
                    else check++;
                }
            }

            if(check==word.length()) totalGroup++;
            list.clear();
            previousIndex = 0;
            check = 0;
        }

        System.out.println(totalGroup);
    }
}
