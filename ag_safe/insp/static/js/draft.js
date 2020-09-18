$('body').on('click','.draft-update-btn',function(){
    $("input").each(function(){
        $(this).attr("value", $(this).val());
	    var $input = $( this );
	    if($input.prop("checked"))
	    {
	    	this.setAttribute("checked", "checked");
	    }
	});
	$("textarea").each(function(){
		$(this).text($(this).val());
	});
    var draft_html = $('html').html();
    var inspection_id = $(this).data('id');
	var csrfmiddlewaretoken =  $('input[name="csrfmiddlewaretoken"]').val();
	$.ajax({
	    type: 'POST',
	    url: '../../../update-draft/',
	    data: {inspection_id:inspection_id, draft_html:draft_html, csrfmiddlewaretoken:csrfmiddlewaretoken},
	    success: function(response){
	        if(response == 'update'){
	            alert("Draft Updated Successfully");
	        }else{
	            alert("Inspection Approved");
	        }
	    }
	})
})