var p=document.querySelector('p');
var button = document.querySelector("button");
var loadData_user = document.getElementById("loadData_user")
var table = document.getElementById("table")
var search = document.getElementById("search")



button.onclick = function(){
// 1   console.log("Button Clicked")
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
// 2           console.log(this.responseText)
            p.textContent = this.responseText
        }
    }
    ajax.open("GET", "data.txt", true)
    ajax.send();
}

loadData_user.onclick = function(){
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
           console.log(this.responseText)
           var json_data=JSON.parse(this.responseText)
           console.log(json_data)
           var html_data="<tr><td>ID</td><td>Name</td><td>Email</td></tr>";
           for(var user of json_data){
                html_data += "<tr>" + "<td>" +user["title"]+"</td>" + "<td>" +user["page_count"]+"</td>" + "<td>" +user["pub_date"]+"</td>" + "</tr>"
                table.innerHTML=html_data
           }
        }
    }
    ajax.open("GET", "test.php", true)
    ajax.send();
}

search.onkeyup=function(){
    var ajax = new XMLHttpRequest();
        ajax.onreadystatechange=function(){
            if(this.readyState==4 && this.status==200){
               var json_data=JSON.parse(this.responseText)
               var html_data="<tr><td>ID</td><td>Name</td><td>Email</td></tr>";
               for(var user of json_data){
                    html_data += "<tr>" + "<td>" +user["title"]+"</td>" + "<td>" +user["page_count"]+"</td>" + "<td>" +user["pub_date"]+"</td>" + "</tr>"
                    table.innerHTML=html_data
               }
            }
        }
        ajax.open("GET", "test.php?name="+search.value, true)
        ajax.send();
}
