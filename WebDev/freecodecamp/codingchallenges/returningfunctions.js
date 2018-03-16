//https://www.freecodecamp.org/challenges/arguments-optional

function addTogether() {
  if (arguments.length==2)
  {
    if (typeof(arguments[0])!='number' || typeof(arguments[1])!='number')
      return undefined;
    return arguments[0]+arguments[1];
  }
  if (typeof(arguments[0])!='number')
    return undefined;
  var outerfirst=arguments[0];
  function singleadd(second)
  {
    if (typeof(second)!='number')
      return undefined;
     return outerfirst+second;
  }
  return singleadd;
}

addTogether(2)(3);
