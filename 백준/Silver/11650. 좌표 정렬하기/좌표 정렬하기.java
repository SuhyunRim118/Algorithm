import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int points = sc.nextInt();
        int[][] lists = new int[points][2];

        for(int i=0;i<points;i++) {
            List<Integer> list = new ArrayList<>();
            lists[i][0] = sc.nextInt();
            lists[i][1] = sc.nextInt();
        }

        Arrays.sort(lists,new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if(o1[0] == o2[0])
					return o1[1]-o2[1];
				else
					return o1[0]-o2[0];
			}
		});

        for(int i=0;i<points;i++) {
            System.out.println(lists[i][0] + " " + lists[i][1]);
        }
    }
}