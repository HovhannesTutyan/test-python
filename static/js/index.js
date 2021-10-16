window.onload = initAll;

function initAll(){
    var saveBookButton = document.getElementById('save_book');
    saveBookButton.onclick= saveBook;
}

function saveBook(){
    var name = document.getElementById('book_name').value;
    var price = document.getElementById('book_price').value;
    var pages = document.getElementById('book_pages').value;
//    alert(name)
//    alert(price)
//    alert(pages)
    var url = '/save_book?name='+name+'&price=' + price + '&pages='+pages;
//    alert(url)
    var req = new XMLHttpRequest();
        req.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200) {
                alert(req.responseText);
            }
        };
        req.open("GET", url, true);
        req.send();
}