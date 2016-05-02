$('#post_review').on('submit', function(event){
		event.preventDefault();
		console.log("form submitted");//sanity check
		createReview()
});
//AJAX for posting
function createReview(){
	var that = $(this);

	console.log("Create review is working!");
	// console.log($('#rate').val());
	// console.log($('#comment').val());
	$.ajax({
		url: that.attr('action'),
		type: 'POST',
		data : {'rate': $('#rate').val(), 'comment': $('#comment').val() },
		//handle a successful response
		success: function(json){
			$('#rate').val('');//remove the val from input
			$('#comment').val('');
			console.log(json);
			console.log("success");//another sanity check
		},
		//handle a non successful response
		error: function(xhf, errmsg, err){
			$('#results').html("<div class = 'alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+"<a href='#' class='close'>&times;</a></div>");
			console.log(xhr.status +": "+ xhr.responseText);
		}

	});

	
};

// $('#likes_button').click(function(){
// 	var review_id;
// 	review_id = $(this).attr("reviewid");
// 	console.log(review_id);

// });
$('#likes').click(function(){
	var review_id;
	review_id = $(this).attr("reviewid");
	$.get('add_like/',{reviewId: review_id}, function(data){
		$('#like_count').html(data + " likes");
	});

});



