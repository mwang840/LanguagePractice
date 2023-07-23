using System;
using System.Text;

namespace AddTwoNum
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }

    public class Solution
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            //My Solution
            //If equal, declare a new listnode object of that list node size (can be one or the other), then have two loops, one over the first list node the other over the second node
            ListNode temp = new ListNode();
            ListNode resultingNode = temp;
            int carryOver = 0;
            //check if both of the linked list size is one then we can get the sum of both and put it in a list
            while (l1 != null || l2 != null)
            {
                int valueOfl1 = (l1 != null) ? l1.val : 0;
                int valueOfl2 = (l2 != null) ? l2.val : 0;
                int sum = valueOfl1 + valueOfl2 + carryOver;
                carryOver = sum / 10;
                int lastDigit = sum % 10;
                resultingNode.next = new ListNode(sum);
                resultingNode = resultingNode.next;
                if (l1 != null)
                {
                    l1 = l1.next;
                }
                if (l2 != null)
                {
                    l2 = l2.next;
                }

            }


            return temp.next;
        }

        //A helper function to get the size of a linked list
        public int getLinkedListSize(ListNode list)
        {
            int totalSize = 0;
            while (list.next != null)
            {
                list = list.next;
                totalSize++;
            }
            return totalSize;
        }
    }


}