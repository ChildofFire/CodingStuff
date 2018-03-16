$(document).ready(function(){
			var json;
				$.getJSON('https://raw.githubusercontent.com/4skinSkywalker/Database-Quotes-JSON/master/quotes.json',function(data){
					json=data;
				});
			
			$("#button").on("click",function(){
				var random=Math.floor(Math.random()*1640);
				var r,g,b,r2,g2,b2;
				r=Math.ceil(Math.random()*255);
				g=Math.ceil(Math.random()*255);
				b=Math.ceil(Math.random()*255);
				document.getElementsByTagName("body")[0].setAttribute("style","background-color:rgb("+r.toString()+","+g.toString()+","+b.toString()+");");
				document.getElementById("inner").setAttribute("style","background-color:white; color:rgb("+r.toString()+","+g.toString()+","+b.toString()+");");
				var quote=json[random].quoteText, author=json[random].quoteAuthor;
				if (author=="")
					author="Anonymous";
				document.getElementById("quotetext").innerHTML=' '+quote;
				document.getElementById("quoteauthor").innerHTML='~'+author+'<br>';
				document.getElementById("tweeter").setAttribute('href','https://twitter.com/intent/tweet?text=' + encodeURIComponent('"' + quote + '" ' + author));
			});
		});