const http = require("http");
const fs = require("fs");
http.createServer(function(request,response){
     
    fs.readFile("index.html", (_, data) => response.end(data));
     
}).listen(3000, "127.0.0.1",function(){
    console.log("Сервер начал прослушивание запросов на порту 3000");
});