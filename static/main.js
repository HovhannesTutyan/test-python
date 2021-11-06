const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
//console.log(csrf)

const sendSearchData = function(game){
    $.ajax({
        type:'POST',
        url:'search/',
        data: {
            'csrfmiddlewaretoken':csrf,
            'game':game,
        },
        success: function(response){
//            console.log(response.dt)
            const data = response.dt
            if(Array.isArray(data)) {
//                console.log('we have an array')
                resultsBox.innerHTML = ""
                data.forEach(function(item){
                    resultsBox.innerHTML += `
                        <a href="${url}${item.pk}" class="item" >
                            <div class="row mt-2 mb-2">
                                <div class="col-2">
                                    <img src="${item.image}" class="game-img">
                                </div>
                                <div class="col-10">
                                    <h5>${item.name} </h5>
                                    <p class="text-muted">${item.studio}</p>
                                </div>
                            </div>
                        </a>
                    `
                })
            } else {
                if(searchInput.value.length > 0) {
                    resultsBox.innerHTML = `<b>${data}</b>`
                }
                else {
                    resultsBox.classList.add('not-visible')
                }
            }
        },
        error: function(err){
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup', function(e){
    console.log(e.target.value) //The read-only target property of the Event interface is a reference to the object onto which the event was dispatched. It is different from Event.currentTarget when the event handler is called during the bubbling or capturing phase of the event.
    if(resultsBox.classList.contains('not-visible')){
        resultsBox.classList.remove('not-visible')
    }
    sendSearchData(e.target.value)
})






//const ul = document.createElement('ul');
//document.body.appendChild(ul);
//
//const li1 = document.createElement('li');
//const li2 = document.createElement('li');
//ul.appendChild(li1);
//ul.appendChild(li2);
//
//function hide(evt) {
//  // e.target refers to the clicked <li> element
//  // This is different than e.currentTarget, which would refer to the parent <ul> in this context
//  evt.target.style.visibility = 'hidden';
//}
//
//// Attach the listener to the list
//// It will fire when each <li> is clicked
//ul.addEventListener('click', hide, false);