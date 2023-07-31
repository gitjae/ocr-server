const board_number = window.location.pathname.split('/board/')[1]
var langs = [];

$('#ocr-container').hide();
$('#ocr-btn').prop("disabled", true);

$.ajax({
    "url": `/api/v1/boards/board/${board_number}`,
    "method": "GET",
    "timeout": 0,
}).done(function (board) {
    console.log(board);
    $('#author').text(board.username === null ? 'anonymous' : board.username.username);
    $('#title').val(board.title);
    $('#contents').val(board.contents);
    $('#loaded_file').attr('src', board.file);
    $('#created_at').val(board.created_time);
    $('#modified_at').val(board.updated_time);

    if($('#loaded_file').attr('src') != null){
        $('#ocr-container').show();
    }
});

$(document).ready(function(){
    const checks = $('input[name="lang"]')

    checks.on('change', function(){
        if($(this).is(':checked')){
            langs.push($(this).val());
        } else {
            let index = langs.indexOf($(this).val());
            if(index !== -1){
                langs.splice(index, 1);
            }
        }
        console.log(langs)

        if(langs.length > 0){
            $('#ocr-btn').prop("disabled", false);
        } else {
            $('#ocr-btn').prop("disabled", true);
        }
    })
})

function ocr(){
    const file = $('#loaded_file').attr('src');
    console.log(file)

    data = {
        file:file,
        langs:JSON.stringify(langs)
    };

    $.ajax({
        method:'GET',
        url:`/ocr?file=${file}`
    })
}