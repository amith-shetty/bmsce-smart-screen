// var mqtt = require('mqtt');
// console.log('Starting subscriber');
// var client  = mqtt.connect('mqtt://farmer.cloudmqtt.com');
// console.log('connecting')
// client.on('connect', function () {
// console.log('connected')
// setInterval(function() {
// client.publish('myTopic', 'Hello this is mqtt');
// console.log('Message Sent');
// }, 5000);
// });



var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://broker.hivemq.com')
client.on('connect', function () {
  // message is Buffer
  client.subscribe('presence', function (err) {
    if (!err) {
    		client.on('message', function(topic, message, packet) {

    			
    			// if(message.value == 'test'){
    				
    				// console.log(message)
    				if(message[0] != 123){
    					console.log("Received '" + message+ " "+ packet + "' on '" + topic + "'");
    				}
    				
    			
    			
      		
    });
    	 }
})
})

