import java.util.Arrays;

// Class for chapter 8
public class Recursion {

    public static void main(String[] args){
        System.out.println(stepCount(3));
        int[][] arr = new int[5][5];
        arr[0][1] = 1;
        arr[1][1] = 1;
        //arr[2][1] = 1;
        arr[3][1] = 1;
        arr[4][1] = 1;

        for(int i = 0; i < arr.length; i++){
            System.out.println(Arrays.toString(arr[i]));
        }

        //(0,0), (1,0), (2,0), (2,0), (2,1), (2,2), (3,2), (3,2), (3,3), (3,3), (3,4),

        robotInGrid(arr, 0, 0, "");
    }

    // 8.1 Step count
    public static int stepCount(int n){
        if(n < 0){
            return 0;
        }
        else if(n == 0){
            return 1;
        }
        int a = stepCount(n-1);
        int b = stepCount(n-2);
        int c = stepCount(n-3);

        return a + b + c;
    }

    // 8.2 Robot in grid
    // 0 = free space, 1 = taken space
    public static void robotInGrid(int[][] mat, int r, int c, String path){
        path += "(" + r + "," + c + ")";
        if(r == mat.length - 1 && c == mat[0].length - 1){
            System.out.println("Path Found: " + path);
            return;
        }

        // Can move downward
        String newPath = path + ", ";
        if(r + 1 < mat.length && c < mat.length && mat[r+1][c] != 1){
            robotInGrid(mat, r+1, c, newPath);
        }
        // Can move to the right
        if(c + 1 < mat[0].length && r < mat.length && mat[r][c+1] != 1){
            robotInGrid(mat, r, c + 1, newPath);
        }
    }
}
