class WhoLikesIt{
    public static String whoLikesIt(String... names) {
        //Do your magic here
        //If one name exists, return that name + likes it
        //If no name exists, return no one likes it
        //If two names exists, return name[0] and name[1] like this
        //If three names exists, return name[0], name[1] and name[2] like this
        //If more than three names exist return name[0], name[1] and names.length - 2 others like this
        
        if(names.length == 0){
            return "no one likes this";
        }
        else if (names.length == 1){
            return names[0] + " likes this";
        }
        else if(names.length == 2){
            return names[0] + " and " + names[1] + " like this";
        }
        else if(names.length == 3){
            return names[0] + ", " + names[1] + " and " + names[2] + " like this";
        }
        else{
            return names[0] + ", " + names[1] + " and "  + Integer.toString(names.length - 2) + " others like this";
        }
    }

    public static void main(String[] args) {
        String[] name = {"Jacob", "Alex", "Max", "Simon", "Bert"};
        System.out.println(whoLikesIt(name));
    }
}