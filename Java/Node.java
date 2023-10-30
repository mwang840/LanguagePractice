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

  public static List<Integer> treeByLevels(Node node) {
    // off ya go!
    List<Integer> sortTree = new LinkedList<Integer>();
    if (node == null) {
      return sortTree;
    }
    Queue<Node> queue = new LinkedList<>();
    queue.add(node);
    while (!queue.isEmpty()) {
      Node temp = queue.poll();
      sortTree.add(temp.value);
      if (temp.left != null) {
        queue.add(temp.left);
      } else if (temp.right != null) {
        queue.add(temp.right);
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