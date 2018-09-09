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
