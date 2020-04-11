import java.util.Arrays;

/**
 * CTCI chapter 8 problems
 */
public class Recursion {

    /**
     * Main method
     * @param args command line arguments
     */
    public static void main(String[] args){
        System.out.println(stepCount(3));
        int[][] arr = new int[5][5];
        arr[0][1] = 1;
        arr[1][1] = 1;
        arr[3][1] = 1;
        arr[4][1] = 1;
        robotInGrid(arr, 0, 0, "");
    }

    /**
     * 8.1 - step count
     * @param n number of steps remaining
     * @return the number of ways a staircase can be ascended with steps of 1, 2, 3
     */
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

    /**
     * 8.2 - robot in grid
     * @param mat the matrix
     * @param r row index
     * @param c col index
     * @param path the current path of the robot
     */
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
