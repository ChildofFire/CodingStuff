$(document).ready(function(){

	var select=$("#select");
	var main=$("#main");
	var playO=$("#playO");
	var playX=$("#playX");
	var buttons=document.querySelectorAll("#main button");
	var player='', computer='';
	var unclickedbuttons=['0','1','2','3','4','5','6','7','8'];
	var winslots=[
	    [0, 1, 2],
	    [3, 4, 5],
	    [6, 7, 8],
	    [0, 3, 6],
	    [1, 4, 7],
	    [2, 5, 8],
	    [0, 4, 8],
	    [6, 4, 2] ];																//slots that form horizontal, vertical or diagonal rows.

	main.hide();

	playX.click(function(){
		player='X';
		computer='O';
		select.hide();
		$("#turn").html("Player's Turn");
		main.show();
	});

	playO.click(function(){
		player='O';
		computer='X';
		select.hide();
		$("#turn").html("Player's Turn");
		main.show();
	});

	for(var i=0;i<buttons.length;i++)
	{
		buttons[i].onclick=function(){
			$(this).html(player);
			$(this).prop('disabled',true);												//disables the button after it's clicked
			unclickedbuttons.splice(unclickedbuttons.indexOf($(this).attr('id')),1);	//removes the currently clicked button from the 'unclickedbuttons' list.
			if(unclickedbuttons.length===0){											//if no unclicked buttons left, then it's a draw
				setTimeout(function(){													//setTimeout pauses execution
					main.hide();
					$("#turn").html('');
					$("#winner").html("It's a draw!");
				},1000);
				setTimeout(function(){reset();},2000);
			}
			else if(winner(player)){
				setTimeout(function(){
					main.hide();
					$("#turn").html('');
					$("#winner").html("Player Wins!!!");
				},1000);
				setTimeout(function(){reset();},2000);
			}
			else{
					$("#turn").html("Computer's Turn");
					setTimeout(function(){
						var randomslot=Math.floor(Math.random()*unclickedbuttons.length);	//picks a random slot for the computer to take its turn.
						$("#"+unclickedbuttons[randomslot]).html(computer);
						$("#"+unclickedbuttons[randomslot]).prop('disabled',true);
						unclickedbuttons.splice(randomslot,1);								//removes the computer's slot from the 'unclickedbuttons' list.
						if(winner(computer)){
							setTimeout(function(){
								main.hide();
								$("#turn").html('');
								$("#winner").html("Computer Wins!!!");
							},1000);
							setTimeout(function(){reset();},2000);
						}
						else
							$("#turn").html("Player's Turn");
					},1000);
			}
		}
	}

	function reset(){															
		select.show();
		main.hide();
		player='';
		computer='';
		$("#winner").html('');
		$("#turn").html('');
		for(var i=0;i<9;i++)
		{
			$("#"+i.toString()).html('');
			$("#"+i.toString()).prop('disabled',false);
		}
		unclickedbuttons=['0','1','2','3','4','5','6','7','8'];
	}

	function winner(symbol){
		for(var i=0;i<8;i++)
		{	
			var flag=true;
			for(var j=0;j<3;j++)
				if($("#"+winslots[i][j].toString()).html()!=symbol){
					flag=false;
					break;
				}
			if(flag)
				return true;
		}
		return false;
	}
});