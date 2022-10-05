

public class ContainerClass {
boolean sortAscending;
public Comparator createComparator(final boolean sortAscending){
    Comparator comparator = new Comparator<Integer>() {

        public int compare(Integer o1, Integer o2) {
            if (sortAscending || ContainerClass.this.sortAscending) {
                return o1 - o2;
            } else {
                return o2 - o1;
            }
        }

    };
    return comparator;
}
}
