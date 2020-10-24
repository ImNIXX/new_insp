$(document).ready(function(){
	$("#nav-toggle").click(function(){
		if($(window).width() >= 1200){
			if($("#nav-toggle").text() == 'Collapse'){
				$("#nav-container").css("width","7%");
				$("#nav-container").css("transition" , "0.5s");
				$('.main-content-nav').css("width","0%");
				$(".main-content-nav-list-icons").animate({width: "toggle"});
				$("ul.main-content-nav-list li .main-content-nav-list-anchor-text").toggle();
				$("#nav-toggle").text(">");

				$("#main-container").css("width","87%");
				$("#main-container").css("transition" , "0.5s");
			}
			else{
				$("#nav-container").css("width","18%");
				$("#nav-container").css("transition" , "0.5s");
				$('.main-content-nav').css("width","100%");
				$(".main-content-nav-list-icons").toggle();
				$("ul.main-content-nav-list li .main-content-nav-list-anchor-text").animate({width: "toggle"});
				$("#nav-toggle").text("Collapse");

				$("#main-container").css("width","76%");
				$("#main-container").css("transition" , "0.5s");
			}
		}
		else{
			if($("#nav-toggle").text() == 'Collapse'){
				$("#nav-container").css("width","9%");
				$("#nav-container").css("transition" , "0.5s");
				$(".main-content-nav-list-icons").toggle();
				$("ul.main-content-nav-list li .main-content-nav-list-anchor-text").toggle();
				$("#nav-toggle").text(">");

				$("#main-container").css("width","87%");
				$("#main-container").css("transition" , "0.5s");
			}
			else{
				$("#nav-container").css("width","0%");
				$("#nav-container").css("transition" , "0.5s");
				$(".main-content-nav-list-icons").toggle();
				$("ul.main-content-nav-list li .main-content-nav-list-anchor-text").toggle();
				$("#nav-toggle").text("Collapse");

				$("#main-container").css("width","76%");
				$("#main-container").css("transition" , "0.5s");
			}
		}
	});
});

//NAVBAR

(function($) { "use strict";

	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {
			var scroll = $(window).scrollTop();

			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});

	//Animation

	$(document).ready(function() {
		$('body.hero-anime').removeClass('hero-anime');
	});

	//Menu On Hover

	$('body').on('mouseenter mouseleave','.nav-item',function(e){
			if ($(window).width() > 750) {
				var _d=$(e.target).closest('.nav-item');_d.addClass('show');
				setTimeout(function(){
				_d[_d.is(':hover')?'addClass':'removeClass']('show');
				},1);
			}
	});


  })(jQuery);

$('body').on('click','.safe-tab-btn',function(){
	var class_name = $(this).data('name');
	$('.common_tab').addClass('dis_none');
	$('.'+class_name).removeClass('dis_none');
})

// SIGNUP FORM

$('#sign_up_form').validate({
    rules: {
        name:{
            required: true,
        },
        username:{
            required: true,
        },
        email:{
            required: true,
            email: true,
        },
        password:{
            required: true,
            minlength: 8,
        },
        cpassword:{
            equalTo: "#reg_pass",
        },
        zipcode:{
            required: true,
        },
    },
    focusInvalid: false,
    invalidHandler: function(form, validator) {
        if (!validator.numberOfInvalids())
            return;
        $('html, body').animate({
            scrollTop: $(validator.errorList[0].element).offset().top
        }, 1000);
    },
    submitHandler: function(form){
        var username = $('input[name="username"]').val();
        var url_ = $('input[name="username"]').data('url');
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: 'POST',
            url: url_,
            data: {username:username, csrfmiddlewaretoken:csrfmiddlewaretoken},
            success: function(response){
                if(response == 'exist'){
                    $('.username_exist').remove();
                    $('#reg_username').after('<p class="error username_exist">Username already exist</p>')
                    $('html, body').animate({
                        scrollTop: $('.username_exist').offset().top - 50
                    }, 1000);
                }else if(response == 'not exist'){
                    form.submit();
                }
            }
        })
    },
})

// LOGIN FORM

$('#login_form').validate({
    rules: {
        username:{
            required: true,
        },
        password:{
            required: true,
        },
    },
    submitHandler: function(form){
        form.submit();
    },
})


// INSPECTION DATA INSERTION AND VALIDATIONS

$('#inspection_form').validate({
    rules: {
        title:{
            required: true,
        },
        facility:{
            required: true,
        },
        stakeholders:{
            required: true,
        },
        type:{
            required: true,
        },
        location:{
            required: true,
        },
        category:{
            required: true,
        },
        operating_area:{
            required: true,
        },
        supervisor:{
            required: true,
        },
    },
    focusInvalid: false,
    invalidHandler: function(form, validator) {
        if (!validator.numberOfInvalids())
            return;
        $('html, body').animate({
            scrollTop: $(validator.errorList[0].element).offset().top
        }, 1000);

    },
    submitHandler: function(form){
        var ins_insert_url = $('#inspection_form').data('url');
        var csrfmiddlewaretoken =  $('#inspection_form input[name="csrfmiddlewaretoken"]').val();
        var title = $('#inspection_form input[name="title"]').val();
        var facility = $('#inspection_form select[name="facility"]').val();
        var stakeholders = $('#inspection_form input[name="stakeholders"]').val();
        var type = $('#inspection_form select[name="type"]').val();
        var location = $('#inspection_form input[name="location"]').val();
        var category = $('#inspection_form select[name="category"]').val();
        var operating_area = $('#inspection_form input[name="operating_area"]').val();
        var supervisor = $('#inspection_form select[name="supervisor"]').val();
        $.ajax({
            type: 'POST',
            url: ins_insert_url,
            data: {inspection_title:title,facility:facility,stakeholders:stakeholders,inspection_type:type,location:location,category:category,operating_area:operating_area,supervisor:supervisor ,csrfmiddlewaretoken:csrfmiddlewaretoken},
            success: function(response){
                if(response){
                    $('#inspection_form .inspection_submit').after('<p class="text-success w-100 inspection-success">Inspection added successfully</p>');
                    setTimeout(function(){
                        $('.inspection-success').fadeOut('slow',function(){
                            $(this).remove();
                        });
                    }, 10000)
                    var draft_id = response.type;
                    var inspection_id = response.id;
                    var insp_id = (inspection_id*9304);
                    var date = response.date;
                    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                    let current_datetime = new Date(date);
                    let new_date = current_datetime.getDate() + "-" + months[current_datetime.getMonth()] + "-" + current_datetime.getFullYear();
                    $('#ins_draft_tbl').append('<tr class="ins_draft_'+insp_id+'"><td>'+new_date+'</td><td><a class="ins_draft_title">'+response.title+'</a></td><td class="draft_name"></td></tr><tr><td colspan="3" class="p-0"><div style="display:none" class="add-inspection upd_ins_'+insp_id+'"></div></td></tr>');
                    var ins_action_length = $('#ins_action_tbl tr').length + 1;
                    $('#ins_action_tbl').append('<tr class="ins_action_'+insp_id+'"><td>'+ins_action_length+' </td><td>'+response.title+'</td><td class="draft_name"></td><td></td><td></td><td><i class="fa fa-trash ins_delete"></i></td><td>Not Approved</td></tr>');
                    table = $('#ins_report_table').DataTable();
                    table.row.add(['<td>'+response.title+'</td>','<td>'+new_date+'</td>','<td>'+response.location+'</td>','<td class="draft_name"></td>','<td>Click Here</td>']).draw(false);
                    $('#ins_report_table tr').not('.report-inspection-common').addClass('report_insp_common ins_report_'+insp_id);
                    $.ajax({
                        type: 'POST',
                        url : 'inspection-draft/',
                        data: {draft_id:draft_id, csrfmiddlewaretoken:csrfmiddlewaretoken},
                        success: function(response){
                            if(response){
                                $('.modal-body').before('<form>');
                                $('.modal-body').prepend(response.draft_html);
                                $('.draft-save-btn').attr('data-id',insp_id);
                                $('.draft-save-btn').attr('data-name',response.draft_slug);
                                $('.draft-save-btn').attr('data-draftname',response.draft_name);
                                $('input[name="draft_slug"]').val(response.draft_slug);
                                $('.modal-content input[name="inspection_id"]').val(insp_id/9304);
                                $('#exampleModalCenter').css('display','block');
                                $('#exampleModalCenter').addClass('show');
                            }
                        }
                    })
                }else{
                    $('.inspection_submit').after('<p class="text-danger w-100 inspection-error">Error while inserting the Inspection</p>');
                    setTimeout(function(){
                        $('.inspection-error').fadeOut('slow',function(){
                            $(this).remove();
                        });
                    }, 10000)
                }
            }
        })
    }
})

// DRAFT SAVE

$('body').on('click','.draft-save-btns',function(){
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
	var inspection_id = $(this).attr('data-id');
	var inspection_type = $(this).attr('data-name');
	var draftname = $(this).attr('data-draftname');
	var csrfmiddlewaretoken =  $('input[name="csrfmiddlewaretoken"]').val();
	$('.modal-body').append('<div class="container-category"><button type="button" class="btn btn-primary draft-update-btn" data-id="'+inspection_id+'">Update</button></div>')
	var draft_html = $('.modal-body').html();
	$.ajax({
	    type: 'POST',
	    url: 'insert-draft/',
	    data: {inspection_id:inspection_id, draft_html:draft_html, csrfmiddlewaretoken:csrfmiddlewaretoken, inspection_type: inspection_type, draftname: draftname},
	    success: function(response){
	        if(response){
                var csrf = $('input[name="csrfmiddlewaretoken"]').val();
                $('.modal-body').html('<input type="hidden" name="csrfmiddlewaretoken" value="'+csrf+'">');
	            $('#exampleModalCenter').css('display','none');
                $('#exampleModalCenter').removeClass('show');
                $('#ins_draft_tbl .ins_draft_'+inspection_id+' .draft_name').append('<a target="_blank" href="/media/insp_draft_dir/'+response.draft_dir+'/'+response.draft_slug+'">'+response.draft_name+'</a>');
                $('#ins_action_tbl .ins_action_'+inspection_id+' .draft_name').append(draftname);
                $('#ins_report_tbl .ins_report_'+inspection_id+' .draft_name').append(draftname);
                $('.draft_tab').trigger('click');
	        }
	    }
	})
})

// UPDATE INSPECTION FORM

$('body').on('click','#update_insp_form button',function(){
    $('#update_insp_form').validate({
        rules: {
            title:{
                required: true,
            },
            facility:{
                required: true,
            },
            stakeholders:{
                required: true,
            },
            type:{
                required: true,
            },
            location:{
                required: true,
            },
            category:{
                required: true,
            },
            operating_area:{
                required: true,
            },
            supervisor:{
                required: true,
            },
        },
        submitHandler: function(form){
            var insp_data =  $('#update_insp_form').serialize();
            var csrfmiddlewaretoken =  $('input[name="csrfmiddlewaretoken"]').val();
            var inspection_id = $('#update_insp_form').data('id');
            var inspection_title = $('#update_insp_form input[name="title"]').val();
            var facility = $('#update_insp_form select[name="facility"]').val();
            var stakeholders = $('#update_insp_form input[name="stakeholders"]').val();
            var inspection_type = $('#update_insp_form select[name="type"]').val();
            var location = $('#update_insp_form input[name="location"]').val();
            var category = $('#update_insp_form select[name="category"]').val();
            var operating_area = $('#update_insp_form input[name="operating_area"]').val();
            var supervisor = $('#update_insp_form select[name="supervisor"]').val();
            $.ajax({
                type: 'POST',
                url: 'update-inspection/',
                data: {inspection_id:inspection_id,title:inspection_title,facility:facility,stakeholders:stakeholders,type:inspection_type,location:location,category:category,operating_area:operating_area,supervisor:supervisor ,csrfmiddlewaretoken:csrfmiddlewaretoken},
                context: this,
                success: function(response){
                    if(response != '' && response.status == 'inspection update'){
                        var insp_id = response.id*9304;
                        $('.ins_draft_'+insp_id).find('.ins_draft_title').html(response.title);
                        $('.ins_action_'+insp_id).find('.insp_title').html(response.title);
                        $('.ins_report_'+insp_id).find('.insp_title').html(response.title);
                        $('.ins_report_'+insp_id).find('.insp_location').html(response.location);
                        $('#update_insp_form .inspection-success').remove();
                        $('#update_insp_form .inspection_submit').after('<p class="text-success w-100 inspection-success">Inspection Updated successfully</p>');
                        setTimeout(function(){
                            $('#update_insp_form .inspection-success').fadeOut('slow',function(){
                                $(this).remove();
                            });
                        }, 10000);
                        if(response.insp_type_status == 1){
                            $.ajax({
                                type: 'POST',
                                url: 'inspection-draft/',
                                data: {draft_id:response.inspection_type, csrfmiddlewaretoken:csrfmiddlewaretoken},
                                success: function(response){
                                    if(response){
                                        $('.modal-body').prepend(response.draft_html);
                                        $('.draft-save-btn').attr('data-id',insp_id);
                                        $('.draft-save-btn').attr('data-name',response.draft_slug);
                                        $('.draft-save-btn').attr('data-draftname',response.draft_name);
                                        $('#exampleModalCenter').css('display','block');
                                        $('#exampleModalCenter').addClass('show');
                                    }
                                }
                            })
                        }
                    }else{
                        $('#update_insp_form .inspection-success').remove();
                        $('#update_insp_form .inspection_submit').after('<p class="text-danger w-100 inspection-success">Inspection has approved, can\'t update</p>');
                        setTimeout(function(){
                            $('#update_insp_form .inspection-success').fadeOut('slow',function(){
                                $(this).remove();
                            });
                        }, 10000);
                        alert("Inspection has approved, you can\'t update this Inspection");
                    }
                }
            })
        }
    });
})


$('body').on('click','.ins_draft_title',function(){
    var ins_html = $('.inspection-add-block').html();
    var txt = $(this).parent().parent().attr('class');
    var numb = txt.match(/\d/g);
    insp_id = numb.join("");
    var csrfmiddlewaretoken =  $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: 'POST',
        url: 'get-inspection/',
        data: {csrfmiddlewaretoken: csrfmiddlewaretoken, inspection_id: insp_id},
        context: this,
        success: function(response){
            if(response){
                $('.add-inspection').html('');
                response = Object.entries(response);
                var this_response = response;
                var upd_ins_path_
                $('.upd_ins_'+insp_id).html(ins_html);
                $('.upd_ins_'+insp_id+' label.error').remove();
                $('.upd_ins_'+insp_id).find(':submit').html('Update');
                $('.upd_ins_'+insp_id).find(':reset').remove();
                $('.upd_ins_'+insp_id).find('#inspection_form').attr({'id':'update_insp_form', 'data-id': insp_id});
                $('.upd_ins_'+insp_id).find('input[name="inspection_title"]').attr({'name':'title'});
                var supervisor_html = $('.upd_ins_'+insp_id).find('select.supervisor').html();
                $('.upd_ins_'+insp_id).find('.inspection_submit').prev().html('<label>Select Supervisor</label><select name="supervisor" class="supervisor">'+supervisor_html+'</select>');
                $('.supervisor').select2();
                $.each(response, function(index){
                    var this_ = $(this);
                    $('.upd_ins_'+insp_id).find('input[name="'+this_[0]+'"], select[name="'+this_[0]+'"]').val(this_[1]);
                });
                if(response[9][1] == 'true'){
                   $('.upd_ins_'+insp_id).find('.main-content-inner-box-export-btn').css('display','none');
                   $.each(response, function(index){
                       var this_ = $(this);
                       $('.upd_ins_'+insp_id).find('input[name="'+this_[0]+'"], select[name="'+this_[0]+'"]').attr('disabled','disabled');
                   });
                }else{
                   $('.upd_ins_'+insp_id).find('.main-content-inner-box-export-btn').css('display','block');
                }
                $('.upd_ins_'+insp_id).find('select[name="category"]').attr('disabled','disabled');
                $('.upd_ins_'+insp_id).find('h2').html('Update Inspection');
                $('.add-inspection').slideUp();
                if($('.upd_ins_'+insp_id).css('display') == 'block'){
                }else{
                    $('.upd_ins_'+insp_id).slideDown();
                }
            }
        }
    });
});


// DELETE INSPECTION

$('body').on('click','.ins_delete',function(){
    var insp_id = $(this).parent().parent().attr('class');
    var numb = insp_id.match(/\d/g);
    insp_id = numb.join("");
    var csrfmiddlewaretoken =  $('input[name="csrfmiddlewaretoken"]').val();
    if(confirm('Are you sure')){
        $.ajax({
            type: 'POST',
            url: 'del-insp/',
            data: {csrfmiddlewaretoken: csrfmiddlewaretoken, inspection_id: insp_id},
            context: this,
            success: function(response){
                if(response == 1){
                    $('.ins_action_'+insp_id).remove();
                    $('.ins_draft_'+insp_id).next().remove();
                    $('.ins_draft_'+insp_id).remove();
                    table = $('#ins_report_table').DataTable();
                    table.rows('.ins_report_'+insp_id).remove().draw();
                }else{
                    alert('Inspection has approved, You can\'t delete this Inspection');
                }
            }
        })
    }
})


// APPROVE INSPECTIONS
$('body').on('click','.approve-btn',function(){
    var insp_approve = $(this).prop("checked");
    var insp_id = $(this).parent().parent().attr('class');
    var numb = insp_id.match(/\d/g);
    insp_id = numb.join("");
    var csrfmiddlewaretoken =  $('input[name="csrfmiddlewaretoken"]').val();
    if($(this).prop('checked') == true){

    }
    $.ajax({
        type: 'POST',
        url: 'inspection-approve/',
        data: {insp_id : insp_id, insp_approve: insp_approve, csrfmiddlewaretoken : csrfmiddlewaretoken},
        success: function(){

        }
    })
})


// SEARCH INSPECTION
$('body').on('click','.search-btn',function(){
    var search_key = $('#main-content-inner-box-search-label').val();
    search_key = $.trim(search_key);
    var csrfmiddlewaretoken =  $('input[name="csrfmiddlewaretoken"]').val();
    $.post( "inspection-search/", { csrfmiddlewaretoken: csrfmiddlewaretoken, search_key: search_key })
        .done(function( data ) {
        response_length = Object.keys(data).length;
        if(response_length > 0){
            $('#ins_filter_tbl').html('');
            for(i=0; i<response_length; i++){
            let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            let current_datetime = new Date(data[i].date);
            let date_ = current_datetime.getDate() + "-" + months[current_datetime.getMonth()] + "-" + current_datetime.getFullYear();
                $('#ins_filter_tbl').append('<tr><td>'+data[i].title+'</td><td>'+date_+'</td><td>'+data[i].category+'</td><td>'+data[i].draft_name+'</td></tr>');
            }
        }else{
            $('#ins_filter_tbl').html('<tr><td colspan="4">No data found</td></tr>');
        }
        $('html, body').animate({
            scrollTop: $('#ins_filter_tbl').offset().top
        }, 1500);
    });
})

// FILTER INSPECTION

$('body').on('change','.filter-insp',function(){
    var csrfmiddlewaretoken =  $('input[name="csrfmiddlewaretoken"]').val();
    var form_ = $('#filter-form');
    var operating_area = form_.find('select[name="operating-area"]').val();
    var facility = form_.find('select[name="facility"]').val();
    var location = form_.find('select[name="location"]').val();
    var category = form_.find('select[name="category"]').val();
    var type = form_.find('select[name="type"]').val();
    var filter_form_data = $('#filter-form').serialize();
    $.post('inspection-filter/', {csrfmiddlewaretoken: csrfmiddlewaretoken, operating_area: operating_area, facility: facility, location: location, category: category, type: type })
        .done(function(data){
            response_length = Object.keys(data).length;
            if(response_length){
                $('#ins_filter_tbl').html('');
                for(i=0; i<response_length; i++){
                let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                let current_datetime = new Date(data[i].date);
                let date_ = current_datetime.getDate() + "-" + months[current_datetime.getMonth()] + "-" + current_datetime.getFullYear();
                    $('#ins_filter_tbl').append('<tr><td>'+data[i].title+'</td><td>'+date_+'</td><td>'+data[i].category+'</td><td>'+data[i].draft_name+'</td></tr>');
                }
            }else{
                $('#ins_filter_tbl').html('<tr><td colspan="4">No data found</td></tr>');
            }
        });
})

$(document).ready(function(){
   if($('.draft-success-msg')[0]){
        $('.draft_tab').click();
        $('html, body').animate({
            scrollTop: $('.draft-success-msg').offset().top
        }, 1000);
   }
})

document.getElementById("choose-module").onchange = function() {
    if (this.selectedIndex!==0) {
        window.location.href = this.value;
    }
};



// SELECT OPTION

$('.supervisor').select2({
    placeholder: "Select Supervisor",
    allowClear: true
})

 $('#ins_report_table').dataTable({
    	dom: 'Bfrtip',
    	 buttons: [
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: [ 0, 1, 2, 3 ]
                },
                title: 'Inspection Report'
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: [ 0, 1, 2, 3 ]
                },
                title: 'Inspection Report',
                customize: function (doc) {
					doc.content[1].table.widths =
				    Array(doc.content[1].table.body[0].length + 1).join('*').split('');
					doc['styles'].tableHeader = {
						alignment: 'left',
						fillColor: '#2d4154',
						padding: '2px',
						color: '#ffffff',
						fontweight: 'bold'
					}
				}
            },
            {
                extend: 'print',
                exportOptions: {
                    columns: [ 0, 1, 2, 3 ]
                },
                title: 'Inspection Report'
            }
        ]
        // buttons: ['excel', 'pdf','print']
    });