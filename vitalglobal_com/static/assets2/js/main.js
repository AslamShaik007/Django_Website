
(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 0
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 0) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function (e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function (e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function (e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });


  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function (e) {
        e.preventDefault();
        portfolioFilters.forEach(function (el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function () {
          AOS.refresh()
        });
      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
  });

  /**
   * Initiate Pure Counter 
   */
  new PureCounter();

})()

var video = document.getElementById("myVideo");
var btn = document.getElementById("myBtn");

function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}

//slider
var image = document.getElementById("image");

var images = ["static/assets2/img/dashboard_1.webp", "static/assets2/img/dashboard_2.webp", "static/assets2/img/dashboard_3.webp"];

var index = 0;

function updateImage() {
  image.src = images[index];

  index = (index + 1) % images.length;

}

setInterval(updateImage, 2000);




// VALIDATIONS FOR FORMS

function getDate() {
  var todaysDate = new Date();
  var year = todaysDate.getFullYear();
  var month = ("0" + (todaysDate.getMonth() + 1)).slice(-2);
  var day = ("0" + todaysDate.getDate()).slice(-2);
  var maxDate = (year + "-" + month + "-" + day);
  console.log(maxDate)
  document.getElementById("date").setAttribute("min", maxDate)

}

getDate();

// refresh for captcha
$(function () {

  // Add refresh button after field (this can be done in the template as well)
  $('#id_captcha_1').after($('<a href="#void" class="captcha-refresh bg-white"><svg width="26" height="26" fill="none" stroke="#1c1c1c" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20 19v-4h-4"></path><path d="M4 13a8.1 8.1 0 0 0 15.5 2"></path><path d="M4 5v4h4"></path><path d="M20 11A8.1 8.1 0 0 0 4.5 9"></path></svg></a>'));

  // Click-handler for the refresh-link
  $('.captcha-refresh').click(function () {
    var $form = $(this).parents('form');
    var url = location.protocol + "//" + window.location.hostname + ":"
      + location.port + "/captcha/refresh/";

    // Make the AJAX-call
    $.getJSON(url, {}, function (json) {
      $form.find('input[name="captcha_0"]').val(json.key);
      $form.find('img.captcha').attr('src', json.image_url);
    });

    return false;
  });
});

$(function () {

  // Add refresh button after field (this can be done in the template as well)
  $('#id_captcha_2').after($('<a href="#void" class="captcha-refresh"><svg width="26" height="26" fill="none" stroke="#1c1c1c" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20 19v-4h-4"></path><path d="M4 13a8.1 8.1 0 0 0 15.5 2"></path><path d="M4 5v4h4"></path><path d="M20 11A8.1 8.1 0 0 0 4.5 9"></path></svg></a>'));

  // Click-handler for the refresh-link
  $('.captcha-refresh').click(function () {
    var $form = $(this).parents('form');
    var url = location.protocol + "//" + window.location.hostname + ":"
      + location.port + "/captcha/refresh/";

    // Make the AJAX-call
    $.getJSON(url, {}, function (json) {
      $form.find('input[name="captcha_0"]').val(json.key);
      $form.find('img.captcha').attr('src', json.image_url);
    });

    return false;
  });
});


$(window).bind("pageshow", function () {
  var form = $('form');
  form[0].reset();
});
$('#otherstext').on("keyup", function () {
  $('#errorother').css('display', 'none')
  $("#otherstext").removeAttr('style');
});
$('#kickStartreset').click(function () {


  $('#error1').css('display', 'none');
  $('#error2').css('display', 'none');
  $('#error3').css('display', 'none');
  $('#error4').css('display', 'none');
  $("#fname").removeAttr('style');
  $("#phoneno").removeAttr('style');
  $("#email").removeAttr('style');
  $("#comp").removeAttr('style');
})
$('#fname').on("keyup", function () {
  $('#error1').css('display', 'none');
  $("#fname").removeAttr('style');
});
$('#phoneno').on("keyup", function () {
  $('#error4').css('display', 'none')
  $("#phoneno").removeAttr('style');
});
$('#email').on("keyup", function () {
  $('#error3').css('display', 'none')
  $("#email").removeAttr('style');
});

$('#comp').on("keyup", function () {
  $('#error5').css('display', 'none')
  $("#comp").removeAttr('style');
});
$('#control_01, #control_02, #control_03, #control_04').on("change", function () {
  $('#error6').css('display', 'none')
});


function setInputFilter(textbox, inputFilter, errMsg) {
  [
    "input",
    "keydown",
    "keyup",
    "mousedown",
    "mouseup",
    "select",
    "contextmenu",
    "drop",
    "focusout",
  ].forEach(function (event) {
    textbox.addEventListener(event, function (e) {
      if (inputFilter(this.value)) {
        if (["keydown", "mousedown", "focusout"].indexOf(e.type) >= 0) {
          this.classList.remove("input-error");
          this.setCustomValidity("");
        }
        this.oldValue = this.value;
        this.oldSelectionStart = this.selectionStart;
        this.oldSelectionEnd = this.selectionEnd;
      } else if (this.hasOwnProperty("oldValue")) {
        this.classList.add("input-error");
        this.setCustomValidity(errMsg);
        this.reportValidity();
        this.value = this.oldValue;
        this.setSelectionRange(
          this.oldSelectionStart,
          this.oldSelectionEnd
        );
      } else {
        this.value = "";
      }
    });
  });
}


// async function logJSONData() {

//   alert("enter in to function")
//     const response = await fetch("http://pss.pranathiss.com:86/captcha-check/", formData, { 'Content-Type': 'application/x-www-form-urlencoded' },);
//     alert("Before response")

//     const jsonData = await response.json();
//     console.log(jsonData);
//     alert("After respnse")
//     return false
//   }
setInputFilter(
  document.getElementById("phoneno"),
  function (value) {
    return /^[0-9()+-\s]*\.?[0-9()+-\s]*$/.test(value);
  },
  "Must be an integer"
);
//validation
// var recaptcha_response = "";
//   function verifyCaptcha(token) {
//     recaptcha_response = token;
//     document.getElementById("g-recaptcha-error").innerHTML = "";
//   }

function LandingPage() {

  var input = (document.getElementById("fname").style.borderColor =
    "#ededed");
  var input2 = (document.getElementById("phoneno").style.borderColor =
    "#ededed");
  var input3 = (document.getElementById("comp").style.borderColor =
    "#ededed");
  var input4 = (document.getElementById("email").style.borderColor =
    "#ededed");
  var firstName = document.getElementById("fname").value;
  if (firstName == "") {
    var input = (document.getElementById("fname").style.borderColor =
      "orange");
    document.getElementById("error1").style.display = "block";
    document.getElementById("error2").style.display = "none";
    document.getElementById("error3").style.display = "none";
    document.getElementById("error4").style.display = "none";
    document.getElementById("error1").innerHTML =
      "*Please enter a Name*";
    document.getElementById("error1").style.color = "red";
    return false;
  } else if (/[^a-zA-Z\-.\s/]/.test(firstName)) {
    var input = (document.getElementById("fname").style.borderColor =
      "orange");
    document.getElementById("error1").style.display = "block";
    document.getElementById("error2").style.display = "none";
    document.getElementById("error3").style.display = "none";
    document.getElementById("error4").style.display = "none";
    document.getElementById("error1").innerHTML =
      "*Special Characters & Numbers Not allowed*";
    document.getElementById("error1").style.color = "red";
    return false;
  }

  var phone = document.getElementById("phoneno").value;
  if (phone == "") {
    var input3 = (document.getElementById("phoneno").style.borderColor =
      "orange");
    document.getElementById("error1").style.display = "none";
    document.getElementById("error2").style.display = "block";
    document.getElementById("error3").style.display = "none";
    document.getElementById("error4").style.display = "none";
    document.getElementById("error2").innerHTML =
      "*Please enter a Mobile Number*";
    document.getElementById("error2").style.color = "red";
    return false;
  } else if (phone.length < 10) {
    var input3 = (document.getElementById("phoneno").style.borderColor =
      "orange");
    document.getElementById("error1").style.display = "none";
    document.getElementById("error2").style.display = "block";
    document.getElementById("error3").style.display = "none";
    document.getElementById("error4").style.display = "none";
    document.getElementById("error2").innerHTML =
      "*Mobile Number must be Min 10*";
    document.getElementById("error2").style.color = "red";
    return false;
  }

  var companyName = document.getElementById("comp").value;
  if (companyName == "") {
    var input4 = (document.getElementById("comp").style.borderColor =
      "orange");
    document.getElementById("error1").style.display = "none";
    document.getElementById("error2").style.display = "none";
    document.getElementById("error3").style.display = "block";
    document.getElementById("error4").style.display = "none";
    document.getElementById("error3").innerHTML =
      "*Please enter a Company Name*";
    document.getElementById("error3").style.color = "red";
    return false;
  }

  var email = document.getElementById("email").value;
  var validRegex = /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/;
  if (email == "") {
    var input2 = (document.getElementById("email").style.borderColor =
      "orange");
    document.getElementById("error1").style.display = "none";
    document.getElementById("error2").style.display = "none";
    document.getElementById("error3").style.display = "none";
    document.getElementById("error4").style.display = "block";
    document.getElementById("error4").innerHTML =
      "*Please enter a Email_ID*";
    document.getElementById("error4").style.color = "red";
    return false;
  } else if (!email.match(validRegex)) {
    var input2 = (document.getElementById("email").style.borderColor =
      "orange");
    document.getElementById("error1").style.display = "none";
    document.getElementById("error2").style.display = "none";
    document.getElementById("error3").style.display = "none";
    document.getElementById("error4").style.display = "block";
    document.getElementById("error4").innerHTML =
      "*Please enter valid Email_ID*";
    document.getElementById("error4").style.color = "red";
    return false;
  }
  else {
    document.getElementById("GetQuoteButton").setAttribute("disabled", true)

  }


  //var id_captcha_1 = document.getElementById("id_captcha_1").value;

  //if(id_captcha_1 == ""){
  //document.getElementById("errorFromCapche1").innerHTML =
  //"*Please enter captcha";
  //return false
  //}

}


setInputFilter(
  document.getElementById("uname"),
  function (value) {
    return /^[a-zA-Z]+$/.test(value);
  },
  "Numbers and special characters are not allowed."
);

setInputFilter(
  document.getElementById("phonenumber"),
  function (value) {
    return /^[0-9()+-\s]*\.?[0-9()+-\s]*$/.test(value);
  },
  "Must be an integer"
);


function RequestDemo() {
  var date = document.getElementById("date").value;
  if (date == "") {
    var input = (document.getElementById("date").style.borderColor =
      "orange");
    document.getElementById("verror1").style.display = "block";
    document.getElementById("verror2").style.display = "none";
    document.getElementById("verror3").style.display = "none";
    document.getElementById("verror4").style.display = "none";
    document.getElementById("verror5").style.display = "none";
    document.getElementById("verror1").innerHTML = "*Please enter a Date*";
    document.getElementById("verror1").style.color = "red";
    return false;
  }
  var time1 = document.getElementById("time1").checked;
  var time2 = document.getElementById("time2").checked;

  if (time1 == time2) {
    // console.log("1",time1);
    // console.log("2",time2);
    document.getElementById("verror1").style.display = "none";
    document.getElementById("verror2").style.display = "block";
    document.getElementById("verror3").style.display = "none";
    document.getElementById("verror4").style.display = "none";
    document.getElementById("verror5").style.display = "none";
    document.getElementById("verror2").innerHTML = "*Please Check one slot*";
    document.getElementById("verror2").style.color = "red";
    return false;
  }

  var uname = document.getElementById("uname").value;
  if (uname == "") {
    var input = (document.getElementById("uname").style.borderColor =
      "orange");
    document.getElementById("verror1").style.display = "none";
    document.getElementById("verror2").style.display = "none";
    document.getElementById("verror3").style.display = "block";
    document.getElementById("verror4").style.display = "none";
    document.getElementById("verror5").style.display = "none";
    document.getElementById("verror3").innerHTML = "*Please Enter a Name*";
    document.getElementById("verror3").style.color = "red";
    return false;
  }

  var phonenumber = document.getElementById("phonenumber").value;
  if (phonenumber == "") {
    var input = (document.getElementById("phonenumber").style.borderColor =
      "orange");
    document.getElementById("verror1").style.display = "none";
    document.getElementById("verror2").style.display = "none";
    document.getElementById("verror3").style.display = "none";
    document.getElementById("verror4").style.display = "block";
    document.getElementById("verror5").style.display = "none";
    document.getElementById("verror4").innerHTML = "*Please Enter a Phone Number*";
    document.getElementById("verror4").style.color = "red";
    return false;
  }

  var email = document.getElementById("demail").value;
  var validRegex = /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/;
  if (email == "") {
    var input = (document.getElementById("demail").style.borderColor =
      "orange");
    document.getElementById("verror1").style.display = "none";
    document.getElementById("verror2").style.display = "none";
    document.getElementById("verror3").style.display = "none";
    document.getElementById("verror4").style.display = "none";
    document.getElementById("verror5").style.display = "block";
    document.getElementById("verror5").innerHTML =
      "*Please enter a Email_ID*";
    document.getElementById("verror5").style.color = "red";
    return false;
  } else if (!email.match(validRegex)) {
    var input = (document.getElementById("demail").style.borderColor =
      "orange");
    document.getElementById("verror1").style.display = "none";
    document.getElementById("verror2").style.display = "none";
    document.getElementById("verror3").style.display = "none";
    document.getElementById("verror4").style.display = "none";
    document.getElementById("verror5").style.display = "block";
    document.getElementById("verror5").innerHTML = "*Please Enter valid Email_ID*";
    document.getElementById("verror5").style.color = "red";
    return false;
  }
  else {
    document.getElementById("liveDemoButton").setAttribute("disabled", true)

  }
  //var id_captcha_2 = document.getElementById("id_captcha_2").value;

  //if(id_captcha_2 == ""){
  //document.getElementById("errorFromCapche2").innerHTML =
  // "*Please enter captcha";
  //return false
  //}

}


