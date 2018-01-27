//var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

$(function() {
  var submit_form = function(e) {
    $.getJSON('/_add_numbers', {
      a: $('#textbox').val(),
    }, function(data) {
      $('#result').text(data.result);
      $('input[name=a]').focus().select();
    });
    return false;
  };
  $('#calculate').bind('click', submit_form);
  $('input[type=text]').bind('keydown', function(e) {
    if (e.keyCode == 13) {
      submit_form(e);
    }
  });
  $('input[name=a]').focus();
});
