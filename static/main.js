const alertBox = document.getElementById('alert-box')
const imgBox = document.getElementById('img-box')
const form = document.getElementById('p-form')

const name = document.getElementById('id_name')
const description = document.getElementById('id_description')
const image = document.getElementById('id_image')

const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

const url = ""

const handleAlerts = function(type, text){
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
                        ${text}</div>`
}

image.addEventListener('change', function(){
    const img_data = image.files[0]
    const url = URL.createObjectURL(img_data)
    console.log(url)
    imgBox.innerHTML = `<img src="${url}" width="100%">`
})

form.addEventListener('submit', function(e){
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('name', name.value)
    fd.append('description', description.value)
    fd.append('image', image.files[0])

    $.ajax({
        type: 'POST',
        url: '{% url "photos:main-view" %}',
        data: {
                fd:fd,
                csrfmiddlewaretoken: csrf,
        },
        success: function(response){
            console.log(response)
            handleAlerts('success','Success' )
        },
        error: function(error){
            console.log(error)
            handleAlerts('danger', 'something went wrong...')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

