$(document).ready( function() {
    $('.assign-to-me').click(function (event) {
        $.ajax({
            type : 'POST',
            url : $( this ).attr("data-target"),
            data : {
                'csrfmiddlewaretoken' : $( this ).attr("token"),
                new_holder : $( this ).attr("target-user"),
                device_pk : $( this ).attr("device_pk")
            },
            success : function(result) {
            },
            failure: function(result) {
                alert('Something went wrong');
            }
        });
    });

    $('.return-to-base').click(function (event) {
        $.ajax({
            type : 'POST',
            url : $( this ).attr("data-target"),
            data : {
                'csrfmiddlewaretoken' : $( this ).attr("token"),
                device_pk : $( this ).attr("device_pk")
            },
            success : function(result) {
            },
            failure: function(result) {
                alert('Something went wrong');
            }
        });
    });
});
