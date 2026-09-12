export function friend(friends: string[]): string[] { 
  let realFriend: string[] = [];
  for(let i = 0; i < friends.length; i++){
    if(friends[i].length === 4){
      realFriend.push(friends[i]);
    }
  }
  return realFriend;
}

console.log(friend(["Ryan", "Kieran", "Jason", "Yous"]))