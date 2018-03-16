$(document).ready(
		function()
		{
			$("#submit").click(
				function()
				{
					var api_path='https://en.wikipedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=0&gsrlimit=10&prop=pageimages|extracts&pilimit=max&exintro&explaintext&exsentences=1&exlimit=max&gsrsearch=';
					var callback_path='&callback=JSON_CALLBACK';
					var string=document.getElementById("search").value;
					var fullpath=api_path+string+callback_path;
					var wikisearchurl='https://en.wikipedia.org/?curid=';
					var html="<ul>";

					$.ajax(
						{
							url:fullpath,
							dataType:'jsonp',
							success: function(data){
									for(var pageid in data.query.pages)
									{
										console.log(pageid,pageid.title,pageid.extract);
										html+="<li><h4><a href=\""+wikisearchurl+pageid+"\" target=\"_blank\">"+data.query.pages[pageid].title+'</a></h4><h6>'+data.query.pages[pageid].extract+"</h4></li>";
									}
									html+="</ul>";
									$('#para').html(html);	
							}
						});
				}
			);
		}
	);