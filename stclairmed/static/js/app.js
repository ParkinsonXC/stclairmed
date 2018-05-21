$(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;
  
      var winTop = $(window).scrollTop();
      if (pos < winTop + 600) {
        $(this).addClass("slide");
      }
    });
  });

  $(document).ready(function(){
    // Add smooth scrolling to all links in navbar + footer link
    $(".navbar a, footer a[href='#myPage']").on('click', function(event) {
  
     // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
  
      // Prevent default anchor click behavior
      event.preventDefault();
  
      // Store hash
      var hash = this.hash;
  
      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
  
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
        });
      } // End if
    });


    $(".btn-rsvp").on("click", function(event) {
      // Use overlay functionality to dynamically produce an RSVP form per event
      e1 = document.getElementById("overlay");
      //Toggle visibility of overlay div
      e1.style.visibility = (e1.style.visibility == "visible") ? "hidden": "visible";

      eventDivId = $(this).parent().attr("id");
      eventId = eventDivId.replace("event-", ""); // Event PK 

      $(".rsvp-submit").attr("href", eventId)
    });
  })