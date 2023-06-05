import java.util.List;

public class PaginationHelper<I> {

  /**
   * The constructor takes in an array of items and a integer indicating how many
   * items fit within a single page
   */
  int totalItemCount;
  int itemsPerPage;

  public PaginationHelper(List<I> collection, int itemsPerPage) {
    this.totalItemCount = collection.size();
    this.itemsPerPage = itemsPerPage;
  }

  /**
   * returns the number of items within the entire collection
   */
  public int itemCount() {
    return totalItemCount;
  }

  /**
   * returns the number of pages
   */
  public int pageCount() {
    return (totalItemCount - 1) / itemsPerPage + 1;
  }

  /**
   * returns the number of items on the current page. page_index is zero based.
   * this method should return -1 for pageIndex values that are out of range
   */
  public int pageItemCount(int pageIndex) {
    // If out of the index, return -1
    int totalPages = pageCount();
    if (pageIndex < 0 || pageIndex >= totalPages) {
      return -1;
    }
    // Else, if the index is the remainder of the initial page items, return the
    // remaining items
    else if (pageIndex == totalPages - 1) {
      return totalItemCount % itemsPerPage;
    } else {
      return itemsPerPage;
    }

  }

  /**
   * determines what page an item is on. Zero based indexes
   * this method should return -1 for itemIndex values that are out of range
   */
  public int pageIndex(int itemIndex) {
    if (itemIndex < 0 || itemIndex > totalItemCount) {
      return -1;
    } else {
      return (itemIndex - 1) / itemsPerPage;
    }
  }

}