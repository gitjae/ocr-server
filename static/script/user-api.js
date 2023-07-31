function user_update(){
    const username = $('#username').val();
    const name = $('#name').val();
    const password = $('#password').val();
    const email = $('#email').val();

    data = {
        username:username,
        name:name
    }
    if(password != ""){
        data.password = password
    }
    if(email != ""){
        data.email = email
    }

    console.log(data)

    
    $.ajax({
        method:"PUT",
        url:`api/v1/users/user/${username}`,
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        data: JSON.stringify(data)
    }).done(result => {
        location.href = `/api/v1/users/user/${username}`;
    })
}