// var page = require('webpage').create();
// page.open('http://cuiqingcai.com',function  (status) {
// 	console.log("Status:" + status);
// 	if (status == "success"){
// 		page.render('test.png');
// 	}
// 	phantom.exit();
// })

// var page = require('webpage').create(),
//   system = require('system'),
//   t, address;

// if (system.args.length === 1) {
//   console.log('Usage: loadspeed.js <some URL>');
//   phantom.exit();
// }

// t = Date.now();
// address = system.args[1];
// page.open(address, function(status) {
//   if (status !== 'success') {
//     console.log('FAIL to load the address');
//   } else {
//     t = Date.now() - t;
//     console.log('Loading ' + system.args[1]);
//     console.log('Loading time ' + t + ' msec');
//   }
//   phantom.exit();
// });

var page = require('webpage').create();
//viewportSize being the actual size of the headless browser
page.viewportSize = { width: 1024, height: 768 };
//the clipRect is the portion of the page you are taking a screenshot of
page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };
//the rest of the code is the same as the previous example
page.open('http://cuiqingcai.com/', function() {
  page.render('germy.png');
  phantom.exit();
});