//https://www.freecodecamp.org/challenges/binary-agents
function binary(str)
{
  var pow=0,num=0;
  for(var i=str.length-1;i>=0;i--)
    {
      if(str[i]==='1')
        num+=Math.pow(2,pow);
      pow++;
    }
  return num;
}

function binaryAgent(str) {
  var array=str.split(' '),newstr='';
  for (var i=0;i<array.length;i++)
    {
      newstr+=String.fromCharCode(binary(array[i]));
    }
  return newstr;
  
}

binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111");
