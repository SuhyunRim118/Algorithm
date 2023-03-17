import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		List<Integer> list = new ArrayList<>();
		int total = 0;
		
		int testcase = sc.nextInt();
		
		for(int i=0;i<testcase;i++) {
			int number = sc.nextInt();
			list.add(number);
		}
		
		for(int i=0;i<list.size();i++) {
			if(list.get(i)==0) {
				list.remove(i);
				list.remove(i-1);
				i-=2;
			}
		}
		
		for(int i=0;i<list.size();i++) {
			total += list.get(i);
		}
		System.out.println(total);
    }
}