 //validation
 // refresh for captcha
 $(function() {
  // Add refresh button after field (this can be done in the template as well)
  $('#id_feed-captcha_1').after($('<a href="#void" class="captcha-refresh"><svg width="26" height="26" fill="none" stroke="#1c1c1c" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20 19v-4h-4"></path><path d="M4 13a8.1 8.1 0 0 0 15.5 2"></path><path d="M4 5v4h4"></path><path d="M20 11A8.1 8.1 0 0 0 4.5 9"></path></svg></a>'));

  // Click-handler for the refresh-link
  $('.captcha-refresh').click(function(){
      var $form = $(this).parents('form');
      var url = location.protocol + "//" + window.location.hostname + ":"
                + location.port + "/captcha/refresh/";

      // Make the AJAX-call
      $.getJSON(url, {}, function(json) {
          $form.find('input[name="captcha_0"]').val(json.key);
          $form.find('img.captcha').attr('src', json.image_url);
      });

      return false;
  });
});

$('#id_news-captcha_0').parent('div').hide();
$('#newsletteremail').keyup(function(){
  $('#id_news-captcha_0').parent('div').show();
})
 $(window).bind("pageshow", function () {
   var form = $('form');
   if (form[0]) {
     form[0].reset();
   }
   if (form[1]) {
     form[1].reset();
   }
   if (form[2]) {
     form[2].reset();
   }
   if (form[3]) {
     form[3].reset();
   }


 });
 // footer
 $("#timing1, #timing2, #timing3, #timing4, #timing5").click(function () {
   $('#ferror1').css("display", "none");
 })
 $("#starmatch1, #starmatch2, #starmatch3, #starmatch4, #starmatch5").click(function () {
   $("#starmatch1").removeAttr('style');
   $('#ferror2').css("display", "none");
 })
 $('#kcomp').on('keyup', function () {
   $("#kcomp").removeAttr('style');
   $('#ferror3').css("display", "none");
 })
 $('#kinputcomments').on('keyup', function () {
   $("#kinputcomments").removeAttr('style');
   $('#ferror4').css("display", "none");
 })
 $('#newsletteremail').on('keyup', function () {
   $("#newsletteremail").removeAttr('style');
   $('#suberror1').css("display", "none");
 })
 function footer() {
   // alert("I am here");
   var getSelectedValue = document.querySelector(
     'input[name="ktiming"]:checked'
   );
   // alert("this is here " + getSelectedValue);
   if (getSelectedValue == null) {
     document.getElementById("ferror1").style.display = "block";
     document.getElementById("ferror2").style.display = "none";
     document.getElementById("ferror3").style.display = "none";
     document.getElementById("ferror4").style.display = "none";
     document.getElementById("ferror1").innerHTML = "*Selected any one";
     document.getElementById("ferror1").style.color = "red";
     return false;
   }

   var SelectedValue = document.querySelector('input[name="kmatch"]:checked');
   if (SelectedValue == null) {
     document.getElementById("ferror1").style.display = "none";
     document.getElementById("ferror2").style.display = "block";
     document.getElementById("ferror3").style.display = "none";
     document.getElementById("ferror4").style.display = "none";
     document.getElementById("ferror2").innerHTML = "*Selected any one";
     document.getElementById("ferror2").style.color = "red";
     return false;
   }
   var companyName = document.getElementById("kcomp").value;
   var validRegex =
     /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/;
   if (companyName == "") {
     var input = (document.getElementById("kcomp").style.borderColor =
       "orange");
     document.getElementById("ferror1").style.display = "none";
     document.getElementById("ferror2").style.display = "none";
     document.getElementById("ferror3").style.display = "block";
     document.getElementById("ferror4").style.display = "none";
     document.getElementById("ferror3").innerHTML =
       "*Please enter a Email_ID*";
     document.getElementById("ferror3").style.color = "red";
     return false;
   } else if (!companyName.match(validRegex)) {
     var input = (document.getElementById("kcomp").style.borderColor =
       "orange");
     document.getElementById("ferror1").style.display = "none";
     document.getElementById("ferror2").style.display = "none";
     document.getElementById("ferror3").style.display = "block";
     document.getElementById("ferror4").style.display = "none";
     document.getElementById("ferror3").innerHTML =
       "*Please enter valid Email_ID*";
     document.getElementById("ferror3").style.color = "red";
     return false;
   }

   var textarea = document.getElementById("kinputcomments").value;
   if (textarea == "") {
     var input = (document.getElementById("kinputcomments").style.borderColor =
       "orange");
     document.getElementById("ferror1").style.display = "none";
     document.getElementById("ferror2").style.display = "none";
     document.getElementById("ferror3").style.display = "none";
     document.getElementById("ferror4").style.display = "block";
     document.getElementById("ferror4").innerHTML = "*Please enter a Message*";
     document.getElementById("ferror4").style.color = "red";
     return false;
   } else if (/[^0-9a-zA-Z\-=!.()+@:$&%'",.\s/?]/.test(textarea)) {
     var input = (document.getElementById("kinputcomments").style.borderColor =
       "orange");
     document.getElementById("ferror1").style.display = "none";
     document.getElementById("ferror2").style.display = "none";
     document.getElementById("ferror3").style.display = "none";
     document.getElementById("ferror4").style.display = "block";
     document.getElementById("ferror4").innerHTML =
       "*Special Characters & Numbers Not allowed*";
     document.getElementById("ferror4").style.color = "red";
     return false;
   }

   //captcha
   var id_captcha_1 = document.getElementById("id_feed-captcha_1").value;

          if(id_captcha_1 == ""){
            document.getElementById("errorFromCapchefeed").innerHTML =
              "*Please enter captcha";
              return false
          }

 }


 //subscribe

 // refresh for captcha
 $(function() {
  // Add refresh button after field (this can be done in the template as well)
  $('#id_news-captcha_1').after($('<a href="#void" class="captcha-refresh"><svg width="26" height="26" fill="none" stroke="#1c1c1c" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20 19v-4h-4"></path><path d="M4 13a8.1 8.1 0 0 0 15.5 2"></path><path d="M4 5v4h4"></path><path d="M20 11A8.1 8.1 0 0 0 4.5 9"></path></svg></a>'));

  // Click-handler for the refresh-link
  $('.captcha-refresh').click(function(){
      var $form = $(this).parents('form');
      var url = location.protocol + "//" + window.location.hostname + ":"
                + location.port + "/captcha/refresh/";

      // Make the AJAX-call
      $.getJSON(url, {}, function(json) {
          $form.find('input[name="captcha_0"]').val(json.key);
          $form.find('img.captcha').attr('src', json.image_url);
      });

      return false;
  });
});


 //validation
 function subscribe() {
   var subEmail = document.getElementById("newsletteremail").value;

   var validRegex =
     /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/;
   if (subEmail == "") {
     document.getElementById("newsletteremail").style.borderColor = "orange";
     document.getElementById("suberror1").style.display = "block";
     document.getElementById("suberror1").innerHTML = "*Please enter a Email_ID*";
     document.getElementById("suberror1").style.color = "red";
     return false;
   } else if (!subEmail.match(validRegex)) {
     document.getElementById("newsletteremail").style.borderColor = "orange";
     document.getElementById("suberror1").style.display = "block";
     document.getElementById("suberror1").innerHTML =
       "*Please enter valid Email_ID*";
     document.getElementById("suberror1").style.color = "red";
     return false;
   } 

   var id_captcha_1 = document.getElementById("id_news-captcha_1").value;

   if (id_captcha_1 == "") {
     document.getElementById("errorFromCapche").innerHTML =
       "*Please enter captcha";
     return false
   }
 }
