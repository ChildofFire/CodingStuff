$(document).ready(function(){

	var buttons=document.querySelectorAll(".calculator button");	//get all button elements
	var ops=['/','*','+','-'];									//array to store all operations
	var decimal=false, operand_begin=true;	//booleans to identify presence of the decimal point and the start of a new operand
	for(var i=0;i<buttons.length;i++)
		{
			buttons[i].onclick=function(){			//onclick function for each button
				var $display=document.getElementById("display");
				var current=$display.innerHTML;		//string storing the expression string
				var curr_input=this.innerHTML;		//string storing the current input value

				if(curr_input==='=')
				{
					try 							//checking for errors in eval()
					{
						current=eval(current);
					}
					catch(e)
					{
						if( e instanceof SyntaxError || e instanceof TypeError || e instanceof ReferenceError)
							current="error!";
					}
					if(current!="error!")
					{
						var value=parseFloat(current);
						if (value>999999999999)
							current="overflow!";
						else if(value<-99999999999)
							current="underflow!";
						else if(Math.floor(value)!=Math.ceil(value))
						{
							var abs=Math.abs(value);
							var integerpart=Math.floor(Math.log(abs)/Math.log(10))+1;
							var decimalpart=12-integerpart-1;	//12 digits is the width of the display, 'integerpart' is the number of digits to the
							//left of the decimal in 'value', '+1' is for one place of the decimal point itself and 'decimalpart' is the decimal precision to be displayed.
							current=Math.round(value*Math.pow(10,decimalpart))/Math.pow(10,decimalpart).toString();
						}
					}
					decimal=false;					//reset decimal and leading zero booleans for new inputs
					operand_begin=true;
				}
				else if(curr_input==='.')
				{
					if(!decimal)					//if decimal not present, append it
					{
						decimal=true;
						operand_begin=false;
						current+='.';
					}
				}
				else if(curr_input==='Backspace')
					current=current.slice(0,-1);	//remove the last character from expression string
				else if(curr_input==='C')
				{
					current='';						//reset/clear everything
					decimal=false;
					operand_begin=true;
				}
				else if(ops.indexOf(curr_input)!=-1)	//current input is an operation
				{
					if (current.length>0)				//if current input is not the first character in the string,
					{
						if(ops.indexOf(current[current.length-1])!=-1)	//then check if the last character is an operation.
						{	
							if(current.length>1 || (current.length===1 && (curr_input==='-' || curr_input==='+')))	//too long to explain!
							{
								var newstr=current.slice(0,-1)+curr_input;		//replace the last operation with the current operation
								current=newstr;
							}
						}
						else
							current+=curr_input;		//if last char of expression string is not an operation, then simply append current operation to expression string
					}
					else if(curr_input==='-' || curr_input==='+')		//if first char of expr string would be an operation, then it can only be '+' or '-'
						current+=curr_input;
					decimal=false;						//reset decimal point for new operand
					operand_begin=true;					//reset begin flag for new operand
				}
				else if(ops.indexOf(curr_input)===-1)		//digit input
				{
					if(operand_begin)						//if this is the first digit of the current operand or the first digit after a leading zero
					{
						if(ops.indexOf(current[current.length-1])!=-1)	//if the last character was an operation
						{ 
							current+=curr_input;						//then simply append the new digit to the expr string.
							if(curr_input!='0')							//if the new digit was non-zero, then unset the 'operand_begin' boolean to prevent coming into
																		//this 'if' again.
								operand_begin=false;
						}
						else 											//if the last character was not an operation, then it has to be a leading zero.
						{
							current=current.slice(0,-1)+curr_input;		//simply replace the leading zero with the new digit
							if(curr_input!='0')
								operand_begin=false;					//if the new digit was non-zero then unset 'operand_begin'.
						}
					}
					else
						current+=curr_input;				//if this isn't the first digit of the current operand, then simply append whatever it is to the expr string
				}

				$display.innerHTML=current;					//finally, write the updated expression string to the display area.
			}
		}

});