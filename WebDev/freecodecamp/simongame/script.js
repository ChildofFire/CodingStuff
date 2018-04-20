var on=false, running=false,strict=false, masterstring=[], usermasterstring=[],interval;
$(document).ready(function(){
	$(".wintext").hide();
	$("#gamereset").hide();
	$(".switch-panel").on('click',powerOnOff);
});

function powerOnOff(){	//function to toggle the on/off switch and power the simon board.
if (!on){
		on=true;
		$("#switch").css({'background-color':'blue','float':'right'});
		$("#simon-text").css('color','red');
		$("#count").css('color','red');	
		$("#count").html(masterstring.length);	//masterstring stores the randomly generated sequence
		$("#start").on('click',changeStart);
	}

	else{
		on=false;
		if(running)
			changeStart();
		//"off()" unbinds click handlers to prevent multiple handlers, and to render the buttons unresponsive when the simon board is switched off.
		$("#start").off();	
		$("#strict").off();
		$(".simon-buttons").off();
		masterstring=[]; usermasterstring=[];	//usermasterstring stores the sequence of the user's key presses.
		$("#count").html('--');
		$("#switch").css({'background-color':'#31278a','float':'left'});
		$("#simon-text").css('color','black');
		$("#count").css('color','#840416');
	}
	
}

//changeStart toggles the start/strict switch and runs the simon sequence.
function changeStart(){	
	if(!running){
				running=true;
				$("#start").html('RESET');
				$("#start").css('background-color','red');
				$("#strict").off().on('click',function(){
					if(strict){
						strict=false;
						$("#strict").css('background-color','#add412');
					}
					else{
						strict=true;
						$("#strict").css('background-color','yellow');
					}
				});
				masterstring.push(Math.floor(Math.random()*4));
				startSimon();
	}
	else{
				running=false;
				$("#start").html('START');
				$("#start").css('background-color','#b5060f');
				if(strict){
						strict=false;
						$("#strict").css('background-color','#add412');
					}
				$("#strict").off();
				masterstring=[];
				usermasterstring=[];
				$("#count").html(0);
	}
}

//startSimon starts the simon sequence
function startSimon(){
	$(".simon-buttons").off(); //so the user can't press buttons while the sequence is being displayed.
	$("#count").html(masterstring.length);
	var counter=0;
	interval=setInterval(function(){	//setInterval runs the sequence of buttons one after the other every second...
			if(counter===masterstring.length)	//keeps track of the number of buttons blinked...
				clearInterval(interval);
			var num=masterstring[counter];
			blinkPanels(num,500);
			counter++;	
	},1000);
	userTurn();
}

//userTurn processes the user's key presses.. also reports victory or error.
function userTurn(){
	$(".simon-buttons").off().on('click',function(){
		var id=parseInt($(this).attr('id'));
		usermasterstring.push(id);
		blinkPanels(id,200);
		
		if(usermasterstring[usermasterstring.length-1]!=masterstring[usermasterstring.length-1])	//user presses the wrong panel
		{
			usermasterstring=[];
			setTimeout(function(){
				$("#count").html("!!");
				$("#error")[0].play();},500);
			if(strict)			//if strict mode is on, then reset the simon sequence if user presses the wrong panel.
			{
				masterstring=[];
				masterstring.push(Math.floor(Math.random()*4));
			}
			setTimeout(function(){
					startSimon();
				},1000);
		}
		//user selects right panel and sequence is fully matched...
		else if(usermasterstring.length===masterstring.length){
			usermasterstring=[];
			//if sequence is of length 20 then user has won the game!
			if(masterstring.length===20){
				$(".instructions").hide();
				$(".gameboard").hide();
				$(".wintext").show();
				$("#gamereset").show();
				blinkWintext();
				setTimeout(function(){$("#victory")[0].play();},500);
				$("#gamereset").off().on('click',function(){
					powerOnOff();
					$(".instructions").show();
					$(".gameboard").show();
					$(".wintext").hide();
					$("#gamereset").hide();
				});
			}
			//else start the next sequence
			else{
				masterstring.push(Math.floor(Math.random()*4));
				setTimeout(function(){
					startSimon();
				},1000);
			}
		}
	});
}

//changes the color of panels to give the illusion of blinking.
function blinkPanels(color,duration){
	if(color===0){
				$(".green").css('background-color','green');
				$("#greensound")[0].play();
				setTimeout(function(){
					$(".green").css('background-color','lime');
				},duration);
			}
			else if(color===1){
				$(".red").css('background-color','#b5060f');
				$("#redsound")[0].play();
				setTimeout(function(){
					$(".red").css('background-color','red');
				},duration);
			}
			else if(color===2){
				$(".blue").css('background-color','#31278a');
				$("#bluesound")[0].play();
				setTimeout(function(){
					$(".blue").css('background-color','blue');
				},duration);
			}
			else if(color===3){
				$(".yellow").css('background-color','#add412');
				$("#yellowsound")[0].play();
				setTimeout(function(){
					$(".yellow").css('background-color','yellow');
				},duration);
			}
}

//blinks the winning text 10 times in succession...
function blinkWintext(){
	var blinkcount=10;
	var interval=setInterval(function(){
		if(blinkcount<0) clearInterval(interval);
		if(blinkcount%2)
			$(".wintext").css('color','blue');
		else
			$(".wintext").css('color','lime');
		blinkcount--;
	},300);
}