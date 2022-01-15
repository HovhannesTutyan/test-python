// console.log('hello world')
const helloWorldBox = document.getElementById('hello-world')
const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const endBox = document.getElementById('end-box')

const postForm = document.getElementById('post-form')
const title = document.getElementById('id_title')
const body = document.getElementById('id_body')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
//console.log(csrf[0].value)

alertBox = document.getElementById('alert-box')

const url = window.location
console.log(url)


const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const deleted = localStorage.getItem('title') // taken from detail.js
if (deleted){
    handleAlerts('danger', `The "${deleted}" post was deleted`)
    localStorage.clear()
    setTimeout(()=>{
        alertBox.classList.add('not-visible')
    }, 2000)
}


const likeUnlikePosts = function(){
    const likeUnlikeForms = [...document.getElementsByClassName('like-unlike-forms')] // spread operator adds in the list to previous values
    // console.log(likeUnlikeForms)  [ form.like-unlike-forms, form.like-unlike-forms, form.like-unlike-forms, form.like-unlike-forms, form.like-unlike-forms, form.like-unlike-forms ]
    likeUnlikeForms.forEach(function(form){
        form.addEventListener('submit', function(e){
            e.preventDefault()
            const clickedId = e.target.getAttribute('data-form-id') // get the id of the clicked form
            const clickedBtn = document.getElementById(`like-unlike-${clickedId}`)
            $.ajax({
                type: 'POST',
                url: "like-unlike/",
                data: {
                    'csrfmiddlewaretoken':csrftoken,
                    'pk':clickedId,
                },
                success: function(response){
//                    console.log(response)
                    clickedBtn.textContent = response.liked ? `Unlike (${response.count})` : `Like (${response.count})`
                },
                error: function(err){
                    console.log(err)
                }
            })
        })
    })
}

//helloWorldBox.textContent = 'Hello world'

//$.ajax ({
//    type: 'GET',
//    url: '/hello-world/',
//    success: function(response){
//        console.log('success', response.text)
//        helloWorldBox.textContent = response.text
//    },
//    error: function(error){
//        console.log('error', error)
//    }
//})


// ${url}${el.id} takes the url of the page and adds id of the "details" button and passes it to post_detail view.

let visible = 3

const getData = function(){
    $.ajax ({
    type: 'GET',
    url: `/data/${visible}/`,
    success: function(response){
//        console.log('success', response)  django serialized data returns a string, Json.parse need to convert it to an object
//        const data = JSON.parse(response.data)
            const data = response.data
            // console.log(data)
            setTimeout(()=>{
                spinnerBox.classList.add('not-visible')
                data.forEach(function(el){
                postsBox.innerHTML += `
                    <div class="card mb-2">
                      <div class="card-body">
                        <h5 class="card-title">${el.title}</h5>
                        <p class="card-text">${el.body}</p>
                      </div>
                      <div class="card-footer">
                        <div class="row">
                            <div class="col-2">
                                <a href="${url}${el.id}" class="btn btn-primary">Details</a>
                            </div>
                            <div class="col-2">
                                <form class="like-unlike-forms" data-form-id="${el.id}">
                                    <button href="#" class="btn btn-primary" id="like-unlike-${el.id}">${el.liked ? `Unlike ${el.count}`:`Like ${el.count}`}</button>
                                </form>
                            </div>
                        </div>

                      </div>

                    </div>
                `
                });
                likeUnlikePosts()
            }, 200)
            // console.log(response.size)
            if (response.size == 0){
                endBox.textContent = "No posts added yet..."
            }
            else if (response.size <= visible) {
                 loadBtn.classList.add('not-visible')
                 endBox.textContent = 'No more posts to load...'
            }
        },
        error: function(error){
            console.log('error', error)
        }
    })
}


loadBtn.addEventListener('click', function(){
    spinnerBox.classList.remove('not-visible')
    visible += 3
    getData()
})

postForm.addEventListener('submit', function(e){
    e.preventDefault()

    $.ajax({
        type: 'POST',
        url: '',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'title': title.value,
            'body': body.value
        },
        success: function(response){
            postsBox.insertAdjacentHTML('afterbegin', `
                <div class="card mb-2">
                  <div class="card-body">
                    <h5 class="card-title">${response.title}</h5>
                    <p class="card-text">${response.body}</p>
                  </div>
                  <div class="card-footer">
                    <div class="row">
                        <div class="col-2">
                            <a href="#" class="btn btn-primary">Details</a>
                        </div>
                        <div class="col-2">
                            <form class="like-unlike-forms" data-form-id="${response.id}">
                                <button href="#" class="btn btn-primary" id="like-unlike-${response.id}">Like (0)</button>
                            </form>
                        </div>
                    </div>
                  </div>
                </div>
            ` )
            likeUnlikePosts()
            $('#addPostModel').modal('hide')
            handleAlerts('success', 'The post was successfully created.')
            postForm.reset()
        },
        error: function (err) {
            console.log(err)
            handleAlerts('danger', 'Something went wrong.')
        }
    })
})
getData()