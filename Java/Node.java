import java.util.*;

public class Node {
  public Node left;
  public Node right;
  public int value;

  public Node(Node l, Node r, int v) {
    left = l;
    right = r;
    value = v;
  }

  // Finds the height of the tree
  public static int calcTreeHeight(Node node) {
    Node root = node;
    if (root == null) {
      return 0;
    }
    return 1 + Math.max(calcTreeHeight(node.left), calcTreeHeight(node.right));
  }

  public static List<Integer> treeByLevels(Node node) {
    // off ya go!
    List<Integer> sortTree = new ArrayList<Integer>();

    Node temp = node;
    // Return am empty list if the root is null
    if (temp == null) {
      return sortTree;

    } // If root is not null we can use a queue method
    else {
      sortTree.add(temp.value);
      while (temp != null) {
        sortTree.add(node.value);
        if (temp.left != null && temp.right != null) {
          System.out.println("Adding Values on this level: ");
          // Check if nodes left val is less then its right val on the same level
          if (temp.left.value < temp.right.value) {
            System.out.println("Value added is: " + temp.left.value);
            sortTree.add(temp.left.value);
          }
          // Else add the right value if the right value is less than the left value on
          // the same level
          else if (temp.right.value < temp.left.value) {
            System.out.println("Value added is: " + temp.right.value);
            sortTree.add(temp.right.value);
          }
        }
        temp = temp.left;
      }
    }
    return sortTree;
  }

  public static void main(String[] args) {
    Node level = new Node(new Node(null, new Node(null, null, 4), 2),
        new Node(new Node(null, null, 5), new Node(null, null, 6), 3), 1);
    System.out.println(treeByLevels(level));
  }
}