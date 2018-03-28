$(document).ready(function(){

	$(".countdown").hide();

	var minutes=parseInt($("#sessionlength").html())-1;
	var seconds=59;

	$("#minutes").html(minutes<10 ? '0'+minutes: minutes);
	$("#seconds").html(seconds);

	$("#start").click(function(){
		$("#controls").hide();
		$(".countdown").show();
		if ($("#start").html()==="Start")
			{
				$("#start").html("Pause");
				$("#reset").prop('disabled',true);
				timerId=setInterval(countdown,1000);

				function countdown(){
					if (seconds===0)
						if(minutes===0)
							{
								$("#alarm")[0].play();
								if ($("#workorbreak").html()==="Back To Work!")
								{
									$("#workorbreak").html("Break Time!");
									minutes=parseInt($("#breaklength").html())-1;
									seconds=59;
								}
								else
								{
									$("#workorbreak").html("Back To Work!");
									minutes=parseInt($("#sessionlength").html())-1;
									seconds=59;
								}
							}
						else{
							minutes--;
							seconds=59;
						}
					else
						seconds--;
					$("#minutes").html(minutes<10?'0'+minutes:minutes);
					$("#seconds").html(seconds<10?'0'+seconds:seconds);
				}
			}
		else 
			{
				$("#start").html("Start");
				$("#reset").prop('disabled',false);
				clearInterval(timerId);
			}
		
	});

	$("#reset").click(function(){
		$("#controls").show();
		$(".countdown").hide();
		minutes=parseInt($("#sessionlength").html())-1;
		seconds=59;
		$("#start").html('Start');
		$("#workorbreak").html('Back To Work!');
		$("#minutes").html(minutes<10?'0'+minutes:minutes);
		$("#seconds").html(seconds);
	});

	$("#addSessionTime").click(function(){
		if (minutes<39)
		{
			minutes++;
			$("#sessionlength").html(minutes+1);
			$("#minutes").html(minutes<10?'0'+minutes:minutes);
		}
	});

	$("#subSessionTime").click(function(){
		if (minutes>0)
		{
			minutes--;
			$("#sessionlength").html(minutes+1);
			$("#minutes").html(minutes<10?'0'+minutes:minutes);
		}
	});

	$("#addBreakTime").click(function(){
		var breakminutes=parseInt($("#breaklength").html());
		if(breakminutes<20)
		{
			breakminutes++;
			$("#breaklength").html(breakminutes);
		}
	});

	$("#subBreakTime").click(function(){
		var breakminutes=parseInt($("#breaklength").html());
		if(breakminutes>1)
		{
			breakminutes--;
			$("#breaklength").html(breakminutes);
		}
	});
});