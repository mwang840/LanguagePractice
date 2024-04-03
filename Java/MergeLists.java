public class MergeLists{
    int val;
    MergeLists next;
    public MergeLists(){}
    public MergeLists(int val){
        this.val = val;
    }

     public MergeLists(int val, MergeLists next){
        this.val = val;
        this.next = next;
    }

    public MergeLists mergeTwoLists(MergeLists list1, MergeLists list2) {
        MergeLists sortedList = new MergeLists(0);
        MergeLists current = sortedList;
        while(list1 != null && list2 !=null){
            if(list1.val < list2.val){
                current.next = list1;
                list1 = list1.next;
            }
            else if(list1.val > list2.val){
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }
        if(list1 != null){
            current.next = list1;
        }
        else if(list2 != null){
            current.next = list2;
        }

        return sortedList.next;
    }
}