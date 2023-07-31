$.ajax({
    "url": "/api/v1/boards",
    "method": "GET",
}).done(function (list) {
    list.forEach(board => {
        image_url = 'media/noimage.jpeg';
        image_url = board.file === null ? image_url : board.file;
        
        $('#boards-container').append(`
        <div class="board">
                <img src="${image_url}">
                <p>
                    <a href="/board/${board.post_no}"><h4>${board.title}</h4></a>
                    <span>${board.username.username}</span>
                </p>
            </div>
        `)
    })
});