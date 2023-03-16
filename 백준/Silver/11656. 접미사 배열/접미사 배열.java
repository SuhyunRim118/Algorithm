import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String s = sc.next();
        String[] strings = new String[s.length()];

        for(int i=0;i<s.length();i++) {
            strings[i] = s.substring(i);
        }

        Arrays.sort(strings);

        for(int i=0;i<strings.length;i++) {
            System.out.println(strings[i]);
        }
    }
}
