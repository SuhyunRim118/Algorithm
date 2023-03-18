import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next();
        StringBuilder newword = new StringBuilder(word);

        for(int i=0;i<word.length();i++) {
            if(word.charAt(i)>='D') {
                newword.setCharAt(i, (char)(word.charAt(i)-3));
            }
            else newword.setCharAt(i, (char)(word.charAt(i)+23));
        }
        System.out.println(newword);
    }
}
