window.onload = initAll;

function initAll(){
    var saveBookButton = document.getElementById('save_book');
    saveBookButton.onclick= saveBook;

}

function showallBooks() {
     var req = new XMLHttpRequest();
     var url = '/getAllBooks'
        req.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200) {
                var data = eval(req.responseText);
//                print(data[0].name)
                var div = document.getElementById('nav-profile');
                var table = document.createElement('TABLE');

                var row = table.insertRow(0);
                var name = row.insertCell(0);
                var price = row.insertCell(1);
                var deleteb = row.insertCell(2)
                name.innerHTML = "Book Name";
                price.innerHTML = "Book Price";
                deleteb.innerHTML = "Delete";

                for (var i = 0; i < data.length; i++) {
                    var row = table.insertRow(i+1);
                    var name = row.insertCell(0);
                    var price = row.insertCell(1);
                    var deleteBook = row.insertCell(2);

                    name.innerHTML = data[i].name;
                    price.innerHTML = data[i].price;
                    deleteBook.innerHTML = "&times;";
                    deleteBook.className = 'text-danger text-center'
                    deleteBook.style.fontSize = '25px'
                    deleteBook.style.cursor = 'pointer'
                    deleteBook.id = data[i].id;
                    deleteBook.className = 'deleteButton';

                    deleteBook.onclick = function(){
                        var obj = this;
                        var id = this.id;
                        var url = '/deletebook?id=' + id;
                        var req = new XMLHttpRequest();
                        req.onreadystatechange = function() {
                            if (this.readyState == 4 && this.status == 200) {
                                if (req.responseText == 'true') {
                                    table.deleteRow(obj.parentNode.rowIndex);
                                }
                            }
                        };
                        req.open("GET", url, true);
                        req.send();
                    }
                }
                table.className = 'table text-center table-striped';
                div.appendChild(table);
            }
        };
        req.open("GET", url, true);
        req.send();
}

function saveBook(){
    var name = document.getElementById('book_name').value;
    var price = document.getElementById('book_price').value;
//    var pages = document.getElementById('book_pages').value;
//    alert(name)
//    alert(price)
//    alert(pages)
    var url = '/save_book?name='+name+'&price=' + price;
//    alert(url)
    var req = new XMLHttpRequest();
        req.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200) {
                if (req.responseText == 'true') {
                    document.getElementById('book_name').value = '';
                    document.getElementById('book_price').value = '';
                    document.getElementById('book_pages').value = '';
                }
            }
        };
        req.open("GET", url, true);
        req.send();
}