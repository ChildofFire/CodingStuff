//https://www.freecodecamp.org/challenges/smallest-common-multiple
function hcf(a,b)
{
  if (b==0)
    return a;
  return hcf(b,a%b);
}

function smallestCommons(arr) {
  var factors=[],min=Math.min(arr[0],arr[1]),max=Math.max(arr[0],arr[1]);
  for (var i=max;i>=min;i--)
    factors.push(i);
  var curr_lcm=factors[0];
  for (var i=1;i<=max-min;i++)
    {
      var curr_hcf=hcf(curr_lcm,factors[i]);
      curr_lcm=Math.floor((curr_lcm*factors[i])/curr_hcf);
    }
  return curr_lcm;
}


smallestCommons([1,13]);
