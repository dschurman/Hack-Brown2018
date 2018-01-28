//var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    if (evt) {
    	evt.currentTarget.className += " active";
    }
}

$(function() {
  var submit_form = function(e) {
    $.getJSON('/_add_numbers', {
      a: $('#textbox').val(),
      b: $('#summary-limit').val(),
      c: $('#keyword-count').val(),
    }, function(data) {
      $('#result').html(data.result + "<br><br><i>Keywords: " + data.keywords + "</i>");
    });
    return false;
  };
  var submit_pdf = function(e) {
    $.getJSON('/pdf', {
      p: $('#filepathbox').val(),
      b: $('#summary-limit').val(),
      c: $('#keyword-count').val(),
    }, function(data) {
      $('#result').html(data.result+ "<br><br><i>Keywords: " + data.keywords + "</i>");
    });
    return false;
  }
  $('#calculate').bind('click', submit_form);
  $('#pdf').bind('click', submit_pdf);


  openTab(null, 'plaintext-tab');
  document.getElementById("default-button").className += " active";


});



