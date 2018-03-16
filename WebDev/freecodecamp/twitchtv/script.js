$(document).ready(
		function()
		{
			var api_url='https://wind-bow.glitch.me/twitch-api/';
			var users=["esl_csgo","blizzheroes","ESL_SC2", "OgamingSC2", "cretetion", "freecodecamp", "storbeck", "habathcx", "RobotCaleb", "noobs2ninjas"];
			var profilelinks=[];
			var logolinks=[];
			var statuses=[];
			var games=[];

			for (var i=0;i<users.length;i++)
			{
				profilelinks.push('https://www.twitch.tv/'+users[i]);
				$.ajax({
					url:api_url+'users/'+users[i],
					async:false,
					dataType:'json',
					success: function(data){
						logolinks.push(data.logo);
					}
				});

				$.ajax({
					url:api_url+'streams/'+users[i],
					async: false,
					dataType:'json',
					success: function(data){
						if (!(data.stream))
							{
								statuses.push("Offline");
								games.push("NA");
							}
						else
							{
								statuses.push("Online");
								games.push(data.stream.game);
							}
					}
				});
			}
			$("#main").removeClass("loader");
			$("#main").addClass("main");

			var html='<h1>TWITCH.TV Streaming Status</h1><br>';			
			for (var i=0;i<logolinks.length;i++)
				{
					html+='<div class="row channel"><div class="col-xs-2"><img src="'+logolinks[i]+'" style="width:100px; height:100px;"></div>';
					html+='<div class="col-xs-10 info"><a target="_blank" href="'+profilelinks[i]+'">Channel Name: '+users[i].toUpperCase()+'</a><br><span>Status: '+statuses[i]+' <br>Game: '+games[i]+'</span></div></div><br>';
				}
			$(".main").html(html);
		}
	);