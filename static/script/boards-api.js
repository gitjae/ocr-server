$.ajax({
    "url": "/api/v1/boards",
    "method": "GET",
}).done(function (list) {
    list.forEach(board => {
        image_url = 'media/noimage.jpeg';
        image_url = board.image_link === "" ? image_url : board.image_link;
        
        $('#boards-container').append(`
        <div class="board">
                <img src="${image_url}">
                <div>
                    <a href="/board/${board.post_no}"><h4>${board.title}</h4></a>
                    <span>${board.username.username}</span>
                </div>
            </div>
        `)
    })
});