let visible = 3

const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')

const handleGetData = function(){
    $.ajax ({
    type: 'GET',
    url: `/posts-json/${visible}/`,
    success: function(response){
        max_size = response.max // false if not the last post
        const data = response.data
        spinnerBox.classList.remove('not-visible')
        setTimeout(function(){
            spinnerBox.classList.add('not-visible')
            data.map(function(post){
            console.log(post.id)
            postsBox.innerHTML += `<div class="card p-3 mt-3 mb-3">
                                        ${post.name}
                                        <br>
                                        ${post.body}
                                    </div>`
            })
        },500)
        if (max_size){
//            console.log('done')
            loadBox.innerHTML = "<h4>No more posts to load</h4>"
        }
    },
    error: function(e){
        console.log(e)
        }
    })
}

handleGetData()
loadBtn.addEventListener('click', function(){
    visible += 3
    handleGetData()
})