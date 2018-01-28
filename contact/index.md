---
layout: page
title: Contact
tags: [contact, ariesmooncandles]
date: 2017-01-01
comments: false
---
{% include form.html %}

<script>
			$("#contact-form").validate({
				submitHandler: function (form) {
					$.ajax({
						url: "//formspree.io/lulamcervantes@gmail.com",
						method: "POST",
						data: {
							_replyto: $(form).find("input[name='_replyto']").val(),
							message: $(form).find("textarea[name='message']").val()
						},
						dataType: "json",
						success: function() {
						$("#submit-success").fadeIn();
						$("#contact-form").fadeOut();
						$("#cText").fadeOut();
					},
					error: function() {
						$("#submit-errors").fadeIn();        
					}
					});
				}
			});
		</script>
<script>