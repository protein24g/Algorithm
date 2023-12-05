import java.io.*;
import java.util.*;

public class Main {
    public static int n;
    public static int[] ary;
    public static int[] operator;
    public static int result_min = Integer.MAX_VALUE;
    public static int result_max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        ary = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            ary[i] = Integer.parseInt(st.nextToken());
        }

        operator = new int[4];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < 4; i++) {
            operator[i] = Integer.parseInt(st.nextToken());
        }

        dfs(1, ary[0]);
        System.out.println(result_max);
        System.out.println(result_min);
    }

    public static void dfs(int depth, int sum) {
        if(depth == n) {
            result_min = Math.min(result_min, sum);
            result_max = Math.max(result_max, sum);
            return;
        }else{
            for(int i = 0; i < 4; i++){
                if(operator[i] > 0){
                    operator[i]--;
                    switch(i){
                        case 0:
                            dfs(depth+1, sum + ary[depth]);
                            break;
                        case 1:
                            dfs(depth+1, sum - ary[depth]);
                            break;
                        case 2:
                            dfs(depth+1, sum * ary[depth]);
                            break;
                        case 3:
                            dfs(depth+1, sum / ary[depth]);
                            break;
                    }
                    operator[i]++;
                }
            }
        }
    }

}
