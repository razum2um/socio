var Profile;
(function($){

    $('a.attr-edit-link').live('click', function() {
        $(this).css('display', 'none');
    });

    Profile = {

        edit: function(id, url) {
            $.getJSON(url, function(data, textStatus){
                if (textStatus == 'success') {
                    $('#attr_'+id+'>p.text').after(data.html);
                    $('#attr_'+id+'>p.text').css('display','none');
                }
            });
        },

        save: function(id) {
            var form = $('#attr_'+id+' .form');
            $.post($(form).attr('action'), $(form).serialize(), function(data, textStatus) {
                if (textStatus == 'success') {
                    $(form).remove();
                    $('#attr_'+id+'>p.text').html(data.html);
                    $('#attr_'+id+'>p.text').css('display','');
                    $('a.attr-edit-link').css('display','');
                }
            }, 'json');
        },

        cancel: function(id) {
            $('#attr_'+id+' .form').remove();
            $('a.attr-edit-link').css('display','');
            $('#attr_'+id+'>p.text').css('display','');
        },

        declension: function(url, sex, type, id2change) {
            $.getJSON(url, $.param({"sex": sex, "type": type}), function(data, textStatus) {
                if (textStatus == 'success') {
                    $(id2change + ' option').each(function(i){
                        $(this).text(data.declension[i][1]);
                    });
                }
            });
        }

    };
})(jQuery);

