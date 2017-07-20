//todo - add config for this
var token = "";
var url = "https://slack.com/api/";

var express = require('express');
var bodyParser = require('body-parser');
 
var app = express();
var port = process.env.PORT || 1337;
 
app.use(bodyParser.urlencoded({ extended: true }));
 
app.listen(port, function () {
  console.log('Listening on port ' + port);
});

app.get('/', function (req, res) { res.status(200).send('Hello world!'); });

app.post('/createChannel', function (req, res) 
{
	console.log('POST /createChannel');
    console.log(req.body);
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('thanks');
	
	/*		
		var query = action + "?token=" + token + "&name=" + channelName + "&pretty=1"
		var xmlHttp = new XMLHttpRequest();
		
		$.get(url + query, function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });*/
	
	/*var payload = 
	{
	text : 'test'
	};
	return res.status(200).json(payload);*/
});
/*
app.post('/getChannels', function(req, res)
{
	console.log('POST /getChannels');
    console.log(req.body);
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('thanks');
	
	/*
	var doc = document.testButton;
		$('#cb :checked').each(function() {
		var ta = $('#t');
		var height = 0;
		ta.height(height);
		ta.val("");
		
			var action = "";
			var params = "?token=" + token + "&exclude_members=true&pretty=1";
			if($(this).val() == "Public")
			{
				action = "channels.list";
				var query = action + params;
				console.log(query);
				$.get(url + query, function(data, status){
				var channels = data.channels;
				height = (channels.length + 2) * 16 + 5;
				ta.height(height);
				ta.val("Public Channels: \n\n");
				channels.forEach( function (item)
				{
					ta.val(ta.val() + item.name + "\n");
				});
				ta.val(ta.val() + "\n");
			});
			}
			else if($(this).val() == "Private")
			{
				action = "groups.list";
				var query = action + params;
				console.log(query);
				$.get(url + query, function(data, status){
				var groups = data.groups;
				console.log(groups);
				height = height + ((groups.length + 2) * 16 + 5);
				ta.height(height);
				ta.val(ta.val() + "Private Channels: \n\n")
				console.log(ta.val());
				groups.forEach( function (item)
				{
					ta.val(ta.val() + item.name + "\n");
				});
			});
			}
			else
			{
				alert("wow");
			}
		});
});

app.post('/inviteToTeam')
{
	console.log('POST /inviteToTeam');
    console.log(req.body);
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('thanks');
});

app.post('/inviteToChannel')
{
	console.log('POST /inviteToChannel');
    console.log(req.body);
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('thanks');
});*/