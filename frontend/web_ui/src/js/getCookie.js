var cookies = '; ' + document.cookie; 
var splitCookie = cookies.split('; ' + "SESSIONID" + '='); 
if (splitCookie.length == 2) return splitCookie.pop();