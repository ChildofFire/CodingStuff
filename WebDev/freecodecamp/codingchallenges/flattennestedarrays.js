//https://www.freecodecamp.org/challenges/steamroller
function steamrollArray(arr) {
  
  var newarr=[];
  for(var i=0;i<arr.length;i++)
    {
      if (Array.isArray(arr[i]))
        newarr=newarr.concat(steamrollArray(arr[i]));
      else
        newarr.push(arr[i]);
    }
  return newarr;
}

steamrollArray([1, [2], [3, [[4]]]]);
