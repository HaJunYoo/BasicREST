$(document).ready(function(){
    if($('#result') != null){
        Read();
    }
});
// create
$('#create').on('click', function(){ // { } 안에 들어오는 것이 function
        $title = $('#title').val(); // id title
        $content = $('#content').val();   //id content

        if($title == "" || $content == ""){ // if one of the thing is blank  or excute create
            alert("Please complete the required field");
        }else{
            $.ajax({
                url: 'create/',
                type: 'POST', // post 형식으로 넣는다
                data: {
                    title: $title,
                    content: $content,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    Read(); // refresh
                    $('#title').val('');
                    $('#content').val('');
                }
            });
        }
    });


// edit

$(document).on('click', '.edit', function(){
        $id = $(this).attr('name');
        window.location = "edit/" + $id;
    });


// update
$('#update').on('click', function(){
        $title = $('#title').val();
        $content = $('#content').val();

        if($title == "" || $content == ""){
            alert("Please complete the required field"); //requirement
        }else{
            $id = $('#post_id').val(); // update를 하기 때문에 id가 필요함
            $.ajax({
                url: '../update/' + $id +'/',
                type: 'POST',
                data: {
                    title: $title,
                    content: $content,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    window.location = '../../';
                    alert('Updated!');
                }
            });
        }

    });


// delete

$(document).on('click', '.delete', function(){
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete/' + $id +'/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                alert("Deleted!");
            }
        });
    });


// index.html 내 result id 태그 부분에 read url에서 읽어온 것을 render해준다
function Read(){
    $.ajax({
url: 'read/',
type: 'POST',
async: false,
data:{
res: 1,
csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
},
success: function(response){
$('#result').html(response);
}
    });
}
