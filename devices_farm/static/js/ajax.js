$(document).ready( function() {
    $('.assign-to-me').click(function (event) {
        var url = $( this ).attr("data-target")
        var user = $( this ).attr("target-user")
        $.ajax({
            type : 'POST',
            url : url,
            data : {
                new_holder : user
            },
            success : function(result) {}
        });
    });

    $('.return-to-base').click(function (event) {
        $.ajax({
            type : 'POST',
            url : "{% url 'devices_farm:change_holder' device.pk %}",
            data : {
                new_holder : '{{ user }}'
            },
            success : function(result) {}
        });
    });
});
