// var url = 'http://www.baidu.com';
// var page = require('webpage').create();
// page.onConsoleMessage = function (msg) {
//     console.log(msg);
// };
// page.open(url, function (status) {
//     page.evaluate(function () {
//         console.log(document.title);
//     });
//     phantom.exit();
// });

// var page = require('webpage').create();
// page.open('http://github.com/', function() {
//   page.render('github.png');
//   phantom.exit();
// });

// var page = require('webpage').create();
// //viewportSize being the actual size of the headless browser
// page.viewportSize = { width: 1024, height: 768 };
// //the clipRect is the portion of the page you are taking a screenshot of
// page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };
// //the rest of the code is the same as the previous example
// page.open('http://github.com/', function() {
//   page.render('germy.png');
//   phantom.exit();
// });

// var url = 'http://www.cuiqingcai.com';
// var page = require('webpage').create();
// page.onResourceRequested = function(request) {
//   console.log('Request ' + JSON.stringify(request, undefined, 4));
// };
// page.onResourceReceived = function(response) {
//   console.log('Receive ' + JSON.stringify(response, undefined, 4));
// };
// page.open(url);

var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'SpecialAgent';
page.open('http://www.httpuseragent.org', function(status) {
  if (status !== 'success') {
    console.log('Unable to access network');
  } else {
    var ua = page.evaluate(function() {
      return document.getElementById('myagent').textContent;
    });
    console.log(ua);
  }
  phantom.exit();
});