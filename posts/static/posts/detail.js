const backBtn = document.getElementById('back-btn')
backBtn.addEventListener('click', function(){
//    history.back()
    window.location.href = window.location.origin
})
const postBox = document.getElementById('post-box')
const spinnerBox = document.getElementById('spinner-box')
const url = window.location.href + "data/"
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const updateBtn = document.getElementById('update-btn')
const deleteBtn = document.getElementById('delete-btn')

const titleInput = document.getElementById('id_title')
const bodyInput = document.getElementById('id_body')

const updateUrl = window.location.href + "update/"
const deleteUrl = window.location.href + "delete/"

const updateForm = document.getElementById('update-form')
const deleteForm = document.getElementById('delete-form')

const alertBox = document.getElementById('alert-box')

 // if logged in user is the same as the author, he can edit and delete the post

$.ajax({
    type: 'GET',
    url: url,
    success: function(response){
        console.log(response)

        const data = response.data

        if (data.logged_in != data.author){
            console.log('different')
        }
        else {
            console.log('the same')
            updateBtn.classList.remove('not-visible')
            deleteBtn.classList.remove('not-visible')
        }

        const titleEl = document.createElement('h3')
        titleEl.setAttribute('class', 'mt-3')
        titleEl.setAttribute('id', 'title')

        const bodyEl = document.createElement('p')
        bodyEl.setAttribute('class', 'mt-1')
        bodyEl.setAttribute('id', 'body')

        titleEl.textContent = data.title // drawing title and body in the page
        bodyEl.textContent = data.body
        postBox.appendChild(titleEl)
        postBox.appendChild(bodyEl)

        titleInput.value = data.title // putting title and body in modal
        bodyInput.value = data.body

        spinnerBox.classList.add('not-visible')
    },
    error: function(err){
        console.log(err)
    }
})

updateForm.addEventListener('submit', function(e){
    e.preventDefault()
    const title = document.getElementById('title')
    const body = document.getElementById('body')

    $.ajax({
        type: 'POST',
        url: updateUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'title' : titleInput.value,
            'body': bodyInput.value,
        },
        success: function(response){
            handleAlerts('success', 'post has been updated')
            title.textContent = response.title
            body.textContent = response.body
            updateForm.reset()
        },
        error: function(error){
            console.log(error)
        }
    })
})

deleteForm.addEventListener('submit', function(e){
    e.preventDefault()

    $.ajax({
        type: 'POST',
        url: deleteUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
        },
        success: function(response){
            window.location.href = window.location.origin
            localStorage.setItem('title', titleInput.value) // used in  main.js for popup message
        },
        error: function(error){

        }
    })
})