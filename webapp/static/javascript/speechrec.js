function startDictation() {

  if (window.hasOwnProperty('webkitSpeechRecognition')) {

    var recognition = new webkitSpeechRecognition();

    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.lang = "en-US";
    recognition.start();
/*
    recognition.onspeechstart = function(e) {
      var cur_value = document.getElementById('textbox').value
    };*/
    var cur_value = "";
    recognition.onresult = function(e) {
      document.getElementById('textbox').value
                               = cur_value + e.results[0][0].transcript;
      cur_value = document.getElementById('textbox').value;
      //recognition.stop();
    };

    recognition.onerror = function(e) {
      recognition.stop();
    }

  }
}
