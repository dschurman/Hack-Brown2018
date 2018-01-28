//var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

$(function() {
  var submit_form = function(e) {
    $.getJSON('/_add_numbers', {
      a: $('#textbox').val(),
    }, function(data) {
      $('#result').html(data.result);
      //$('input[name=a]').focus().select();
    });
    return false;
  };
  var submit_pdf = function(e) {
    $.getJSON('/pdf', {
      p: $('#filepathbox').val(),
    }, function(data) {
      $('#result').html(data.result);
    });
    return false;
  }
  $('#calculate').bind('click', submit_form);
  $('#pdf').bind('click', submit_pdf);
  //$('input[name=a]').focus();
});
