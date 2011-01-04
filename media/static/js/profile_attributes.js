var Profile;
(function($){
    Profile = {

        toggleEdit: function(id, url) {
            $.getJSON(url, function(data, textStatus){
                if (textStatus == 'success') {
                    $('#text_'+id).html(data.html);
                }
            });
        },

        toggleSave: function(id) {
            var form = $('#form_'+id);
            $.post($(form).attr('action'), $(form).serialize(), function(data, textStatus) {
                if (textStatus == 'success') {
                    $('#text_'+id).html(data.html);
                }
            }, 'json');
        }

    };
})(jQuery);

