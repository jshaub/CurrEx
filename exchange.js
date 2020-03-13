const api_url = 'https://api.exchangeratesapi.io/latest';
var base, currencies, rates;

let demo = () => {
	let rate = fx(1).from("GBP").to("USD");
	alert("£1 = $" + rate.toFixed(4));
}

fetch(api_url)
  .then(response => response.json())
  .then(data => {
  	base = data.base;
  	currencies = data.rates;
  }).then(demo);

// Allow only numbers and '.' to be entered in textareas
function checkValidChar(event) {
    var code = event.keyCode;

    //alert(e.keyCode);

    if(code < 48 || code > 57) {
    	if(code != 46) {
    		event.preventDefault();
    	}
    }
}