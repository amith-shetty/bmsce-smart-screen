// var mqtt = require('mqtt')
// var client  = mqtt.connect('mqtt://farmer.cloudmqtt.com');
// client.on('connect', function () {
//     client.subscribe('myTopic')
// })
// client.on('message', function (topic, message) {
// context = message.toString();
// console.log(context)
// })






var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://broker.hivemq.com')
 
client.on('connect', function () {
  

  	setInterval(function(){
  		client.publish('presence', 'Hello mqtt')
  		console.log('sent')
  	}, 500);
      
    
 
})
