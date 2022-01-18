const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const endBox = document.getElementById('end-box')
let visible=3

const url = window.location
console.log(url)

const getData = function(){

    $.ajax({
        type: 'GET',
        url: `/get_data/${visible}/`,
        success: function(response){
            const data = response.data
            console.log(data)
            setTimeout(()=>{
                spinnerBox.classList.add('not-visible')
                data.forEach(function(el){
                postsBox.innerHTML += `
                    <div class="card mb-2">
                        <div class="card-body">
                            <h5 class="card-title">${el.name}</h5>
                            <p class="card-text">${el.email}</h5>
                        </div>
                        <div class="card-footer">
                            <div class="row">
                                <div class="col-2">
                                    <a href="${url}${el.id}" class="btn btn-primary">Details</a>
                                </div>
                            </div>
                        </div>
                    </div>
                `
                })
            }, 200)
             if (response.size == 0){
                loadBtn.classList.add('not-visible')
                endBox.testContent = 'No posts are available...'
             }
             else if (response.size <= visible){
                loadBtn.classList.add('not-visible')
                endBox.textContent = "No more posts to load..."
             }
        },
        error: function(error){
            console.log(error)
        }
    })
}
getData()

loadBtn.addEventListener('click', function(){
    spinnerBox.classList.remove('not-visible');
    visible+=3;
    getData()
})