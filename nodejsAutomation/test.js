// Test File

var expect = require('chai').expect;
var request = required('request');

it('Main page content', function(done) {
    request('http://localhost:8080' , function(error, response, body) {
        expect(body).to.equal('Hello World');
    });

});
