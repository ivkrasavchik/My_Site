console.log(window.screen.width);

jQuery(document).ready(function ($) {
    $('#project-link').click(show_projects);
    $('#project-link-hide').click(hide_projects);
    $('#verse-link').click(show_verse);
    $('#verse-link-hide').click(hide_verse);
    $('.div_link_list').click(diary_title_link);
    
    
    
    function show_projects() {
        $(".hidden_home_bloc").hide();
        $("#project-list").show();
    }
    function hide_projects() {
        $("#project-list").hide();
    }
    function show_verse() {
        $(".hidden_home_bloc").hide();
        $("#verse-list").show();
    }
    function hide_verse() {
        $("#verse-list").hide();
    }
    function diary_title_link() {
        $("#diary-description").empty();
        var data = {};
        data.diary_id = $(this).attr('data-id_diary');
        var csrf_token = $('#diary-list-block [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        $.ajax({
            type: "POST",
            url: "note_content",
            data: data,

            success: function (arv) {
                $('#diary-text-block > p ').append(arv)
            }
        })
    }
    
});
